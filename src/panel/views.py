import logging

from django.http import HttpResponse, HttpResponseNotFound
import django_rq
from luma.core.legacy import textsize

from rest_framework.decorators import api_view

from panel.message import show_message, MAX_WIDTH, DEFAULT_FONT
from panel.serializers import MessageSerializer

import luma.core.legacy.font as f


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
        font_arg = message.validated_data['font']

        # check font exists
        try:
            font = getattr(f, font_arg)
            font = f.proportional(font)
        except AttributeError:
            font = DEFAULT_FONT

        text_width = textsize(text, font)[0]
        should_slide = text_width > MAX_WIDTH
        if should_slide:
            logging.warning(f"Text is too large sliding... {text_width}/{MAX_WIDTH}")

        django_rq.get_queue(priority).enqueue(
            show_message,
            text=text,
            should_slide=should_slide,
            timeout=timeout,
            font=font
        )
        return HttpResponse(f"Sent '{text}' with priority {priority}")

    return HttpResponseNotFound()
