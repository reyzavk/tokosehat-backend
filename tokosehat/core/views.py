from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from django.db.models import (
    Subquery,
    OuterRef,
    Prefetch,
)
from rest_framework.decorators import action
from tokosehat.core import models, serializers
# Create your views here.



class RecipeViewSet(FlexFieldsModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    filterset_fields = ('title',)
    search_fields = ('title', 'description', 'instruction', 'tools')

    @action(detail=False, methods=['get',])
    def recent(self, request, *args, **kwargs):
        self.queryset = models.Recipe.objects.exclude(
            purchases=None
        ).order_by('-datetime')

        return self.list(request)


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
