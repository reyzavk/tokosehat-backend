from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    instruction = models.TextField()
    tools = models.TextField(blank=True, default='')
    price = models.PositiveIntegerField()


class Material(models.Model):
    name = models.CharField(max_length=255)
    calorie = models.FloatField()
    price = models.PositiveIntegerField()


class Composition(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='compositions', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, related_name='compositions', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()


class Category(models.Model):
    name = models.CharField(max_length=255)
    prohibitions = models.ManyToManyField(Tag, related_name='blockers')
    requirements = models.ManyToManyField(Tag, related_name='categories')


class Plan(models.Model):
    date = models.DateField()
    recipes = models.ManyToManyField(Recipe, related_name='plans')


class Purchase(models.Model):
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    is_opportunity = models.BooleanField()

