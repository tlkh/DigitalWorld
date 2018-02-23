import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase
url = 'https://fir-robot-dw.firebaseio.com' # URL to Firebase database
token = 'ZdgZXosuV87HKcUWLKhnVN6YQNabxYLwpKWNnsSb' # unique token used for authentication
# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)
# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)
# Use GPIO12, 16, 20 and 21 for the buttons.
# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
lst = [12,16,20,21]
for n in lst:
    GPIO.setup(n,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []
done = False
buttons = {'left':12,'up':16,'right':20}

while not done:
    for key in buttons:
        if GPIO.input(buttons[key]) == GPIO.HIGH:
            print("button pressed", key)
            movement_list.append(key)
            sleep(0.4)
    if GPIO.input(21) == GPIO.HIGH:
        print(GPIO.input(21))
        done = True
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
firebase.put('/','movement_list',movement_list)
print('exiting')
