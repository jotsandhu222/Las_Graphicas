from watchFunctions import ring, check_button_press, blink_led_and_vibration, send_sms, screen_message, sms_sent_if_button_not_pressed
from time import sleep
from gpiozero import LED, Button
import time
import threading

#              watch start confirmation
sleep(2)
blink_led_and_vibration(3)
ring(2)
sleep(2)
screen_message("watch is", "top")
screen_message("ON", "center")
#              confirmation end


#              demo mode
def demo_mode():
    screen_message("Demo Mode", "center")        
    button = Button(2)                      #gpio 2
    led = LED(17)                           #gpio 17
    
    while True:
        screen_message("WARNING!!", "top")
        screen_message("are you ok?", "center")
        
        start_time = time.time()
        while not button.is_pressed and (time.time() - start_time) < 5:
            sleep(0.1)
            blink_led_and_vibration()
            led.off()



#             main mode            
def main():
    screen_message("Production mode", "center")
    button = Button(2)
    led = LED(17)
    heartbeat = 100           #remove this when the module will get connected !!!!!!!!!!
    gps_location = "gmaps location"
    
    
    condition_met = threading.Event()
    
    while True:
        if heartbeat < 60 | heartbeat > 120:
            screen_message("abnormal activity", "top")
            screen_message("press button for false alarm", "center")
        
            alert_cancelled = sms_sent_if_button_not_pressed(button, heartbeat, gps_location)
            
            if alert_cancelled:
                sleep(60)
            else:
                sleep(300)
                
        else:
            sleep(0.5)
            
            
            
      
            #create threads
t1 = threading.Thread(target=check_button_press)
t2 = threading.Thread(target=led.on)
            #start threads
t1.start()
t2.start()
            
            #wait threads to end then finish
t1.join()
t2.join()