import time

from luma.core.interface.serial import spi, noop
from luma.core import legacy
from luma.core.legacy.font import proportional, CP437_FONT
from luma.core.render import canvas
from luma.led_matrix.device import max7219

CASCADED = 4
BLOCK_ORIENTATION = -90
SCROLL_DELAY = 0.1


def show_message(text: str, should_slide: bool, timeout: int):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(
        serial,
        cascaded=CASCADED,
        block_orientation=BLOCK_ORIENTATION
    )

    if should_slide:
        legacy.show_message(
            device,
            text,
            fill="white",
            font=proportional(CP437_FONT),
            scroll_delay=SCROLL_DELAY
        )
    else:
        with canvas(device) as draw:
            legacy.text(
                draw=draw,
                xy=(0, 0),
                txt=text,
                fill="white",
                font=proportional(CP437_FONT),
            )

            time.sleep(timeout)

            legacy.text(
                draw=draw,
                xy=(0, 0),
                txt="",
            )
