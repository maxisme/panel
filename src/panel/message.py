from luma.core.interface.serial import spi, noop
from luma.core import legacy
from luma.core.legacy.font import proportional, CP437_FONT
from luma.led_matrix.device import max7219

CASCADED = 4
BLOCK_ORIENTATION = -90
SCROLL_DELAY = 0.03


def show_message(text: str):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(
        serial,
        cascaded=CASCADED,
        block_orientation=BLOCK_ORIENTATION
    )

    legacy.show_message(
        device,
        text,
        fill="white",
        font=proportional(CP437_FONT),
        scroll_delay=SCROLL_DELAY
    )
