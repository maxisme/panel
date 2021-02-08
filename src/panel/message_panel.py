import time

from django.conf import settings
from luma.core import legacy
from luma.core.interface.serial import noop, spi
from luma.core.legacy.font import proportional
from luma.core.render import canvas
from luma.led_matrix.device import max7219


def display_message(text: str, should_slide: bool, font: proportional) -> None:
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(
        serial,
        cascaded=settings.CASCADED,
        block_orientation=settings.BLOCK_ORIENTATION,
        blocks_arranged_in_reverse_order=True,
    )

    if should_slide:
        legacy.show_message(
            device, text, fill="white", font=font, scroll_delay=settings.SCROLL_DELAY
        )
    else:
        with canvas(device) as draw:
            legacy.text(
                draw=draw,
                xy=(0, 0),
                txt=text,
                fill="white",
                font=font,
            )

        time.sleep(settings.MESSAGE_DISPLAY_TIME)
        device.clear()
