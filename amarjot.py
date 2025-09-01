#motor and led
from gpiozero import LED, Button
import time

#screen
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import ImageDraw, ImageFont, Image
from time import sleep

heartrate = 100
led = LED(17)
button = Button(2)
button2 = Button(22)

def screen_message(message):
     # I2C setup
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial)

    # Load font
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    
    # Create a new image and draw text
    image = Image.new("1", device.size)
    draw = ImageDraw.Draw(image)
    draw.text((10, 20), f"Index: {message}", font=font, fill=255)
    
    device.display(image)   # Turn ON (show text)
    sleep(0.8)

    device.clear()          # Turn OFF (clear screen)
    sleep(0.4)
    
    
def time_sleep(i):
	count = 10
	for i in range(count):
		if button.is_pressed:
			return True
		else:
			time.sleep(i/10)
	return False

def notify_user(message):
    screen_message(message, 18, 0.8, 0.4)
    while button.is_pressed:
        time.sleep(0.1)
        led.on()
        if time_sleep(0.8):
            led.off()
            heartrate = 100
            break
        led.off()
        if time_sleep(0.4):
            heartrate = 100
            break
        
def main():
    while True:
        print(heartrate)
        if heartrate < 70:
            notify_user("are you okay?")
        else:
            screen_message("heartrate normal")
            time.sleep(1)
        heartrate -= 5


if __name__ == "__main__":
    main()




# screen code

# Loop to flash text
for i in range(6):
    screen_message(i)