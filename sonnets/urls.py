from django.urls import include, path
from rest_framework.routers import DefaultRouter

from sonnets import views

router = DefaultRouter()
router.register(r'sonnets', views.SonnetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]