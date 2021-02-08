from django.urls import path

from panel.views import message_view

urlpatterns = [
    path('message', message_view),
]
