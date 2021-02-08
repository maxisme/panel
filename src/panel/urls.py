from django.urls import path

from panel.views import health, message_handler

urlpatterns = [
    path("health", health),
    path("", message_handler),
]
