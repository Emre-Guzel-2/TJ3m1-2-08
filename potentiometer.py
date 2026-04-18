# Created by Emre Guzel
# Created on April 18, 2026
# Project: Potentiometer controlled Servo
import board
import pwmio
import analogio
import time

# setting the ports 
servo = pwmio.PWMOut(board.GP8, frequency=50)
pot = analogio.AnalogIn(board.GP26)

# dividing the pot reading by this gives us the angle in degrees
# biggest 16-bit number/max degrees in the servo
RATIO = 65535 // 180

try:
    while True:
        # Read the raw value from the pot (0 to 65535)
        raw_value = pot.value

        # divide raw value by RATIO to get angle in degrees
        angle = raw_value // RATIO 

        # Convert angle to duty cycle
        duty = int(1638 + (angle / 180) * (8192 - 1638))

        # set the servo
        servo.duty_cycle = duty

        # sleep/puse
        time.sleep(0.02)

except KeyboardInterrupt:
    servo.deinit()
    pot.deinit()
    print("Program stopped.")