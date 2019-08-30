from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from tokosehat.core import models


class MaterialSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'

    expandable_fields = {
        'tags': (
            'tokosehat.core.serializers.TagSerializer',
            {'source': 'tags', 'many': True}
        )
    }

class CompositionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Composition
        fields = '__all__'

    expandable_fields = {
        'material': (
            'tokosehat.core.serializers.MaterialSerializer',
            {'source': 'material'}
        )
    }


class TagSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class PlanSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class PurchaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Purchase
        fields = '__all__'

    expandable_fields = {
        'recipe': (
            'tokosehat.core.serializers.RecipeSerializer',
            {'source': 'recipe'}
        )
    }


class TagImageSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('image',)


class RecipeSerializer(FlexFieldsModelSerializer):
    tags = TagSerializer(read_only=True, many=True, source='get_tags')

    class Meta:
        model = models.Recipe
        fields = '__all__'

    expandable_fields = {
        'compositions': (
            'tokosehat.core.serializers.CompositionSerializer',
            {'source': 'compositions', 'many': True}
        )
    }


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        extra_kwargs = {
            'prohibitions': {'required': False},
            'requirements': {'required': False},
        }


class RecipeCategorySerializer(FlexFieldsModelSerializer):
    recipes = RecipeSerializer(read_only=True, many=True, source='get_recipes')
    class Meta:
        model = models.Category
        fields = '__all__'


class SearchHistorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.SearchHistory
        fields = '__all__'


class PopularSearchSerializer(serializers.Serializer):
    keyword = serializers.CharField()
    count = serializers.IntegerField()
