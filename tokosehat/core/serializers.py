from rest_flex_fields import FlexFieldsModelSerializer
from tokosehat.core import models


class RecipeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Recipe
        fields = '__all__'


class MaterialSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'


class CompositionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Composition
        fields = '__all__'


class TagSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class PlanSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PurchaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Purchase
        fields = '__all__'
