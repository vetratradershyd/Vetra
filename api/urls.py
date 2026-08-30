from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
# from rest_framework.routers import router
from django.urls import path,include

router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)

urlpatterns = router.urls
# urlpatterns = [
#     path("", include(router.urls)),
# ]

# urlpatterns = [
#     path('category/',CategoryViewSet.as_view()),
#     path('product/',ProductViewSet.as_view()),
# ]

# urlpatterns = [
    
# ]
