import logging

import django_rq
import luma.core.legacy.font as luma_font
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from luma.core.legacy import textsize
from rest_framework.decorators import api_view

from panel.message_panel import display_message
from panel.serializers import MessageSerializer


def health(request: HttpRequest) -> HttpResponse:
    return HttpResponse()


@api_view(["POST"])
def message_handler(request: HttpRequest) -> HttpResponse:
    message = MessageSerializer(data=request.data)
    message.is_valid(raise_exception=True)

    priority = message.validated_data["priority"]
    text = message.validated_data["text"]
    font_arg = message.validated_data["font"]

    # check font exists
    try:
        font = getattr(luma_font, font_arg)
        font = luma_font.proportional(font)
    except AttributeError:
        font = settings.DEFAULT_FONT

    text_width = textsize(text, font)[0]

    # slide if text too long to fit on one screen
    should_slide = text_width > settings.MAX_WIDTH
    if should_slide:
        logging.warning(
            f"Text is too large({text_width}/{settings.MAX_WIDTH}) sliding..."
        )

    # send message to panel queue
    django_rq.get_queue(priority).enqueue(
        display_message,
        text=text,
        should_slide=should_slide,
        font=font,
    )

    return HttpResponse(f"Sent '{text}' with priority {priority}")
