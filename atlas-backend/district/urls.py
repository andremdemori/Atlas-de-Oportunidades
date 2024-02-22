from django.urls import path, include
from rest_framework_nested import routers

from .views import DistrictViewSet

from . import views as v

router = routers.DefaultRouter()

#router.register("geojson", DistrictViewSet, basename='District')

urlpatterns = [
    path("", include(router.urls)),
    path('geojson/', v.DistrictGeoJson.as_view(),name='district_geojson'),
]