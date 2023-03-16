
from django.contrib import admin
from django.urls import path, include

from hello_world.core import views as core_views



urlpatterns = [

    path("admin/", admin.site.urls),
    path("", include("uniapp.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
