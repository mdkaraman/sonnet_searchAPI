from django.urls import include, path
from rest_framework.routers import DefaultRouter

from sonnets import views

router = DefaultRouter()
router.register(r'sonnets', views.SonnetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
