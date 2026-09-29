from codrone_edu.drone import *

drone = Drone()
drone.connect()

# Welcome to Python for Robolink! Write your Python code below.

drone.disconnect()

from codrone_edu.drone import *    # load the drone library

drone = Drone()                    # create an object named drone
drone.pair()                       # connect through the controller

# your code goes here

drone.close()                      # disconnect

from codrone_edu.drone import *

drone = Drone()
drone.pair()

battery = drone.get_battery()      # ask the drone how much charge is left
print("Battery:", battery, "%")    # show it in the Console

drone.close()
from codrone_edu.drone import *

drone = Drone()
drone.pair()

print("Battery:", drone.get_battery(), "%")

drone.takeoff()      # lift to about 80 cm and hover
drone.hover(3)       # stay there for 3 seconds
drone.land()         # settle down

drone.close()
drone.set_drone_LED(0, 255, 0, 100)    # red, green, blue, brightness
drone.drone_buzzer(440, 500)    # 440 Hz for 500 milliseconds