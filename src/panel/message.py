import time

from luma.core.interface.serial import spi, noop
from luma.core import legacy
from luma.core.legacy import textsize
from luma.core.legacy.font import proportional,  LCD_FONT, TINY_FONT, SEG7_FONT
from luma.core.render import canvas
from luma.led_matrix.device import max7219

CASCADED = 4
BLOCK_ORIENTATION = 90
SCROLL_DELAY = 0.05
MAX_WIDTH = 32
SMALL_FONT = proportional(SEG7_FONT)
DEFAULT_FONT = proportional(LCD_FONT)


def show_message(text: str, should_slide: bool, timeout: int, font):

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(
        serial,
        cascaded=CASCADED,
        block_orientation=BLOCK_ORIENTATION,
        blocks_arranged_in_reverse_order=True
    )

    if should_slide:
        legacy.show_message(
            device,
            text,
            fill="white",
            font=font,
            scroll_delay=SCROLL_DELAY
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

        if timeout != 0:
            time.sleep(timeout)
            with canvas(device) as draw:
                legacy.text(
                    draw=draw,
                    xy=(0, 0),
                    txt="",
                )
