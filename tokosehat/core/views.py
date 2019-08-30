from rest_flex_fields import FlexFieldsModelViewSet
from tokosehat.core import models, serializers

# Create your views here.



class RecipeViewSet(FlexFieldsModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    filterset_fields = ('title',)
    search_fields = ('title', 'description', 'instruction', 'tools')


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
    fielterset_fields = '__all__'


class PlanViewSet(FlexFieldsModelViewSet):
    queryset = models.Plan.objects.all()
    serializer_class = serializers.PlanSerializer
    fielterset_fields = '__all__'


class PurchaseViewSet(FlexFieldsModelViewSet):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    fielterset_fields = '__all__'
