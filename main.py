###Import all libraries here
import subprocess 
import PiMotor
import time
import sys
from test_sensor import *
from gpiozero import LED, DistanceSensor, Button
from signal import pause

#Define custom pins for UT, led, button
sensor = DistanceSensor(6, 5, max_distance=1, threshold_distance=0.2)
led = LED(20)
button = Button(21)

#Assign motors
m1 = PiMotor.Motor("MOTOR1",1) #front left
m2 = PiMotor.Motor("MOTOR2",1) #font right
m3 = PiMotor.Motor("MOTOR3",1) #rear right
m4 = PiMotor.Motor("MOTOR4",1)  #rear left 


#driving function 
def forward(speed):
    m1.forward(speed)
    m2.reverse(speed)
    m3.forward(speed)
    m4.reverse(speed)
    print("Forward")
    
def reverse(speed):
    m1.reverse(speed) 
    m2.forward(speed)
    m3.reverse(speed)
    m4.forward(speed)
    print("Reverse")
    
def stop():
    m1.stop()
    m2.stop()
    m3.stop()
    m4.stop()
    
    print("Stop")
    
def turn_left(speed):
    m1.stop()
    m2.reverse(speed)
    m3.forward(speed)
    m4.stop()
    print("Turn Left")
    
def turn_right(speed):
    m1.forward(speed)
    m2.stop()
    m3.stop()
    m4.reverse(speed)
    
    print("Turn Right")


if __name__ == '__main__':
    try:
        while True:
            led.off()
            forward(40)
            current_distance = distance()
            if(current_distance < 20):
                led.blink()
                reverse(20)
                time.sleep(1)
                turn_right(40)
                time.sleep(1)
            elif(button.is_pressed):
                stop()
    except KeyboardInterrupt:
            GPIO.cleanup()
                
                
                
            
                
        
      
        
   
        

    
