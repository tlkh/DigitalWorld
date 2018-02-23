from pythymiodw import *
from time import sleep
from firebase import firebase
url = 'https://fir-robot-dw.firebaseio.com' # URL to Firebase database
token = 'ZdgZXosuV87HKcUWLKhnVN6YQNabxYLwpKWNnsSb' # unique token used for authentication
# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)
robot = ThymioReal() # create an eBot object
no_movements = True

while no_movements:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.
    time.sleep(0.5)
    movement_list = firebase.get('/movement_list')
    if movement_list == "":
        print("no instructions")
        no_movements = True
    else:
        print("got new instructions!!")
        firebase.put('/','movement_list',"")
        no_movements = False

print("executing instructions")
for direction in movement_list:
    if direction == 'up':
        robot.wheels(100,100)
        time.sleep(1)
        robot.wheels(0,0)
    if direction == 'left':
        robot.wheels(-100,100)
        time.sleep(1)
        robot.wheels(0,0)
    if direction == 'right':
        robot.wheels(100,-100)
        time.sleep(1)
        robot.wheels(0,0)
