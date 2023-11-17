"""
URL configuration for zonifero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
]

# swagger
SchemaView = get_schema_view(
    openapi.Info(
        title="Zonifero2 API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
swagger_url_pattern = [
    path("swagger/", SchemaView.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

# debug_toolbar
debug_toolbar_url_pattern = [
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns.extend(swagger_url_pattern)
urlpatterns.extend(debug_toolbar_url_pattern)