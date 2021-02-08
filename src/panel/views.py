from django.http import HttpResponse, HttpResponseNotFound
import django_rq
from rest_framework.decorators import api_view

from panel.message import show_message
from panel.serializers import MessageSerializer

@api_view(['POST'])
def message_view(request):
    if request.method == "POST":
        message = MessageSerializer(data=request.data)
        message.is_valid(raise_exception=True)

        priority = message.validated_data['priority']
        text = message.validated_data['text']

        django_rq.get_queue(priority).enqueue(show_message, text=text)
        return HttpResponse("Your response")

    return HttpResponseNotFound()
