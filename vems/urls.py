from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.views import P2PTransactionViewSet
from prosumer.views import (
    GenerationViewSet,
    LoadViewSet,
    ProsumerViewSet,
    StorageViewSet,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Vaidyuti API",
      default_version='v1',
      description="API for Vaidyuti Energy Management System",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mail@vaidyuti-placeholder.dummy"),
      license=openapi.License(name="GNU GPL v3 License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r"prosumer/generations", GenerationViewSet)
router.register(r"prosumer/loads", LoadViewSet)
router.register(r"prosumer/prosumers", ProsumerViewSet)
router.register(r"prosumer/storages", StorageViewSet)
router.register(r"core/p2-p-transactions", P2PTransactionViewSet)

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("api/docs/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/", include("openapi.urls")),
    path("api/v1/", include(router.urls)),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
