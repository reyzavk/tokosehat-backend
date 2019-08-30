from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    image = models.ImageField()
    instruction = models.TextField()
    tools = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title

    def get_tags(self):
        return Tag.objects.filter(
            materials__compositions__recipe=self
        ).distinct()


class Material(models.Model):
    name = models.CharField(max_length=255)
    calorie = models.FloatField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Composition(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='compositions', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, related_name='compositions', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.recipe.title + ': ' + self.material.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    materials = models.ManyToManyField(Material, related_name='tags')
    image = models.ImageField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    prohibitions = models.ManyToManyField(Tag, related_name='blockers')
    requirements = models.ManyToManyField(Tag, related_name='categories')

    def __str__(self):
        return self.name


class Plan(models.Model):
    date = models.DateField()
    recipes = models.ManyToManyField(Recipe, related_name='plans')


class Purchase(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='purchases', null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    is_opportunity = models.BooleanField()
    datetime = models.DateTimeField(auto_now_add=True)

