import RPi.GPIO as GPIO
import time

def angle_to_percent(angle):
    if angle >180 or angle<0:
        return False
    
    start = 4
    end = 12.5
    ratio = (end-start)/180
    
    angle_as_percent = angle*ratio
    
    return start + angle_as_percent

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pwm_gpio=12
frequence=50
GPIO.setup(pwm_gpio,GPIO.OUT)
pwm=GPIO.PWM(pwm_gpio, frequence)

pwm.start(angle_to_percent(0))
time.sleep(1)

pwm.ChangeDutyCycle(angle_to_percent(90))
time.sleep(1)

pwm.stop()
GPIO.cleanup()


