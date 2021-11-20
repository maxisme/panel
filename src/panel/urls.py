from django.urls import path

from panel.views import handler, health

urlpatterns = [
    path("health", health),
    path("", handler),
]
