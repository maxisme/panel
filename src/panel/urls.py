from django.urls import path

from panel.views import message_view, health_view

urlpatterns = [
    path('', health_view),
    path('message', message_view),
]
