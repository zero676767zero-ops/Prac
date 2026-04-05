# Matrix - vcc -> Pin 1 (3.3V), gnd -> Pin 6, DIN -> Pin 19(MOSI (GPIO 10)), CS/LOAD -> Pin 24(GPIO 8), Clk -> Pin 23(GPIO 11)

# sudo apt update
# sudo apt install -y python3-pip
# pip3 install luma.led_matrix


from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from luma.core.legacy import show_message, text
from luma.core.legacy.font import proportional, CP437_FONT
import time

# Uses /dev/spidev0.0 (SPI0 CE0)
serial = spi(port=0, device=0, gpio=noop())

# For a single 8x8 matrix
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)
device.contrast(50)   # 0-255 (increase if needed)

print("MAX7219 8x8 Matrix Ready...")

def blink_dot():
    with canvas(device) as draw:
        draw.point((3,3), fill="white")
        draw.point((4,3), fill="white")
        draw.point((4,4), fill="white")
        draw.point((3,4), fill="white")

def diagonal_line():
    with canvas(device) as draw:
        for i in range(8):
            draw.point((i, i), fill="white")

def border_box():
    with canvas(device) as draw:
        for x in range(8):
            draw.point((x, 0), fill="white")
            draw.point((x, 7), fill="white")
        for y in range(8):
            draw.point((0, y), fill="white")
            draw.point((7, y), fill="white")

def show_letter_A():
    with canvas(device) as draw:
        # Draw a simple 'A'
        points = [(1,7),(1,6),(1,5),(1,4),(1,3),(1,2),(1,1),(2,0),(3,0),(4,0),(5,0),
                  (6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),
                  (2,7),(2,6),(2,5),(2,4),(2,3),(2,2),(2,1),(3,1),(4,1),(5,1),
                  (5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(3,4),(4,4)]
        for p in points:
            draw.point(p, fill="white")

try:
    while True:
        device.clear()
        blink_dot()
        time.sleep(1)

        device.clear()
        diagonal_line()
        time.sleep(1)

        device.clear()
        border_box()
        time.sleep(1)

        device.clear()
        show_letter_A()
        time.sleep(2)

        device.clear()
        show_message(device, "RUIA CS-IT", fill="white",
                     font=proportional(CP437_FONT),
                     scroll_delay=0.1)

        time.sleep(1)

except KeyboardInterrupt:
    device.clear()
    print("\nStopped. Display cleared.")