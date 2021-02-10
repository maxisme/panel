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
        should_slide = message.validated_data['slide']
        timeout = message.validated_data['timeout']

        django_rq.get_queue(priority).enqueue(
            show_message,
            text=text,
            should_slide=should_slide,
            timeout=timeout,
        )
        return HttpResponse(f"Sent '{text}' with priority {priority}")

    return HttpResponseNotFound()
