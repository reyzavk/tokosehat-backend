from rest_framework import routers
from tokosehat.core import views

router = routers.DefaultRouter()

router.register('recipes', views.RecipeViewSet)
router.register('materials', views.MaterialViewSet)
router.register('compositions', views.CompositionViewSet)
router.register('tags', views.TagViewSet)
router.register('categories', views.CategoryViewSet)
router.register('plans', views.PlanViewSet)
router.register('purchases', views.PurchaseViewSet)
