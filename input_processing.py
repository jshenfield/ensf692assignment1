# input_processing.py
# Jack Shenfield, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self, light, pedestrian, vehicle):
        self.light = light
        self.pedestrian = pedestrian
        self.vehicle = vehicle
        pass

    # Asks user to input an update to the status by choosing which object changed, and what it changed to
    def update_status(self): 
        print('\nAre changes detected in the vision input?')

        # saving initial values of each sensory input
        original_light = self.light
        original_pedestrian = self.pedestrian
        original_vehicle = self.vehicle

        # Ask for menu input from user
        value1 = input('Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program:')

        # If user wants to end the program, end the program
        if(value1 == '0'):
            quit()

        # Ask for status input from user
        value2 = input('What change has been identified?:')

        # If user is referring to light, update light
        # If user gives an invalid value, print that and reset light to original value
        if(value1 == '1'):
            if(value2 != 'red' and value2 != 'yellow' and value2 != 'green'):
                print('YOUR STATUS INPUT IS INVALID. PLEASE TRY AGAIN!')
                self.light = original_light
            else:
                self.light = value2


        # If user is referring to pedestrian, update pedestrian
        # If user gives an invalid value, print that and reset pedestrian to original value
        elif(value1 == '2'):
            if(value2 != 'yes' and value2 != 'no'):
                print('YOUR STATUS INPUT IS INVALID. PLEASE TRY AGAIN!')
                self.pedestrian = original_pedestrian
            else:
                self.pedestrian = value2


        # If user is referring to vehicle, update vehicle
        # If user gives an invalid value, print that and reset vehicle to original value
        elif(value1 == '3'):
            if(value2 != 'yes' and value2 != 'no'):
                print('YOUR STATUS INPUT IS INVALID. PLEASE TRY AGAIN!')
                self.vehicle = original_vehicle           
            else:
                self.vehicle = value2


        # If user did not give 1, 2, 3, or 0 for menu input, it is invalid.
        else:
            print('YOUR MENU INPUT IS INVALID. PLEASE TRY AGAIN!')
    
        pass



# The sensor object should be passed to this function to print the action message and current status
# Proceed, Caution, and STOP conditions detected and printed.
# STOP also is triggered for any invalid values
def print_message(sensor):
    if(sensor.light == 'green' and sensor.pedestrian == 'no' and sensor.vehicle == 'no'):
        print('\nProceed')
    elif(sensor.light == 'yellow' and sensor.pedestrian == 'no' and sensor.vehicle == 'no'):
        print('\nCaution')
    else:
        print('\nSTOP')
    print('\nLight =', sensor.light, ', Pedestrian =', sensor.pedestrian, ", Vehicle =", sensor.vehicle, '.')
    pass



# Main function
# Runs continuously until user gives 0 for menu input, or manually stops running the program
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    # initialize variables as per assignment
    light = 'green'
    pedestrian = 'no'
    vehicle = 'no'
    x = True

    # create my sensor
    sensor1 = Sensor(light, pedestrian, vehicle)

    # run through the program
    while(x == True):
     
        sensor1.update_status()
        print_message(sensor1)

    

    





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

