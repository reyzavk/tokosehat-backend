from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from django.db.models import (
    Subquery,
    OuterRef,
    Prefetch,
    Count,
    Sum,
    F,
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from tokosehat.core import models, serializers
from django_filters import rest_framework as filters
# Create your views here.

class RecipeFilter(filters.FilterSet):
    categories = filters.BaseCSVFilter(label='categories', method='filter_categories')

    class Meta:
        model = models.Recipe
        fields = ('title', 'categories',)

    def filter_categories(self, qs, field_name, value, *args, **kwargs):
        categories = models.Category.objects.filter(id__in=value)
        for category in categories:
            qs = qs.filter(
                compositions__material__tags__id__in=category.requirements.all()
            ).exclude(
                compositions__material__tags__id__in=category.requirements.all()
            )

        qs = qs.distinct()
        return qs


class RecipeViewSet(FlexFieldsModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    # filterset_fields = ('title',)
    filterset_class = RecipeFilter
    search_fields = ('title', 'description', 'instruction', 'tools')

    @action(detail=False, methods=['get',])
    def recent(self, request, *args, **kwargs):
        self.queryset = models.Recipe.objects.exclude(
            purchases=None
        ).order_by('-datetime')

        return self.list(request)

    @action(detail=True, methods=['post',])
    def buy_ready(self, request, *args, **kwargs):
        recipe = self.get_object()
        compositions = recipe.compositions.all()
        price = compositions.aggregate(
            price=Sum(
                F('material__price') * F('quantity')
            )
        )['price']

        purchase = models.Purchase.objects.create(
            recipe=recipe,
            quantity=1,
            price=price,
            is_opportunity=True,
            is_served=False
        )

        serializer = serializers.PurchaseSerializer(purchase)
        return Response(serializer.data)


class MaterialViewSet(FlexFieldsModelViewSet):
    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer
    filterset_fields = '__all__'


class CompositionViewSet(FlexFieldsModelViewSet):
    queryset = models.Composition.objects.all()
    serializer_class = serializers.CompositionSerializer
    filterset_fields = '__all__'


class TagViewSet(FlexFieldsModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    fielterset_fields = ('name',)


class CategoryViewSet(FlexFieldsModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filterset_fields = '__all__'

    @action(detail=False, methods=['get',])
    def recipes(self, request, *args, **kwargs):
        self.serializer_class = serializers.RecipeCategorySerializer
        return self.list(request)


class PlanViewSet(FlexFieldsModelViewSet):
    queryset = models.Plan.objects.all()
    serializer_class = serializers.PlanSerializer
    filterset_fields = '__all__'


class PurchaseViewSet(FlexFieldsModelViewSet):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    filterset_fields = '__all__'
    permit_list_expands = (
        'recipe',
        'recipe.compositions',
        'recipe.compositions.material'
    )


class SearchHistoryViewSet(FlexFieldsModelViewSet):
    queryset = models.SearchHistory.objects.all()
    serializer_class = serializers.SearchHistorySerializer
    filterset_fields = '__all__'

    @action(detail=False, methods=['get',])
    def popular(self, request, *args, **kwargs):
        self.serializer_class = serializers.PopularSearchSerializer
        self.queryset = models.SearchHistory.objects.values(
            'keyword'
        ).annotate(
            count=Count('pk')
        ).order_by('-count')

        return self.list(request)
