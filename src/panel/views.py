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

        queue = django_rq.get_queue(message.validated_data['priority'])
        queue.enqueue(show_message, text=message.validated_data['text'])
        return HttpResponse("Your response")

    return HttpResponseNotFound()
