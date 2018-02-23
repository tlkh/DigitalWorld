import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)
# Use GPIO12, 16, 20 and 21 for the buttons.
# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
lst = [12,16,20,21]
for n in lst:
    GPIO.setup(n,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
movement_list = []
done = False
buttons = {'left':GPIO.input(12),'up':GPIO.input(16),'right':GPIO.input(20)}

while True:
    print(21,GPIO.input(21))
    print(12,buttons['left'])
    '''
    We loop through the key (button name), value (gpio number) pair of the buttons
    dictionary and check whether the button at the corresponding GPIO is being
    pressed. When the OK button is pressed, we will exit the while loop and 
    write the list of movements (movement_list) to the database. Any other button
    press would be stored in the movement_list.

    Since there may be debouncing issue due to the mechanical nature of the buttons,
    we can address it by putting a short delay between each iteration after a key
    press has been detected.
    '''
    # Write to database once the OK button is pressed
