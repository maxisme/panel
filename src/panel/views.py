from django.http import HttpResponse, HttpResponseNotFound
import django_rq
from luma.core.legacy import textsize
from rest_framework import serializers
from rest_framework.decorators import api_view

from panel.message import show_message, SMALL_FONT, MAX_WIDTH, DEFAULT_FONT
from panel.serializers import MessageSerializer, MAX_LEN_WITHOUT_SLIDE


def health_view(request):
    return HttpResponse()


@api_view(['POST'])
def message_view(request):
    if request.method == "POST":
        message = MessageSerializer(data=request.data)
        message.is_valid(raise_exception=True)

        priority = message.validated_data['priority']
        text = message.validated_data['text']
        timeout = message.validated_data['timeout']

        text_width = textsize(text, SMALL_FONT)[0]
        should_slide = text_width > MAX_WIDTH
        if not should_slide:
            font = SMALL_FONT
            print(f"Text is too large {text_width}/{MAX_WIDTH}")
        else:
            font = DEFAULT_FONT

        django_rq.get_queue(priority).enqueue(
            show_message,
            text=text,
            should_slide=should_slide,
            timeout=timeout,
            font=font
        )
        return HttpResponse(f"Sent '{text}' with priority {priority}")

    return HttpResponseNotFound()
