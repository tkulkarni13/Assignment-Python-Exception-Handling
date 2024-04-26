# Task 1: Start

while True: # infinite loop until user enters a valid number.
    try:
        tempF = int(input("Please enter the temperature in Fahrenheit: ")) # get user input
        break
    except ValueError: # make sure user input is a number so it can be converted to temperature
        print("That's not a number. Please enter a valid number.")

# Task 2: Temperature Conversion

def fahrenheitToCelsius (temp): # function to convert temperature from fahrenheit to celsius
    try:
        newTemp = round(((temp - 32) * 5 / 9), 2) # conversion and rounding
    except OverflowError: # if an error is detected, the below message is displayed
        print ("There was an overflow error.")
    else: # if there are no errors in the conversion, the temperature is shown to the user in celsius
        print("The temperature is {} degrees Celsius.".format(newTemp))
    finally: # display friendy text to the user no matter what
        print("Thanks for using this weather forcast application!")

fahrenheitToCelsius(tempF) # call function with user inputted temperature

# Task 3: User Experience
# added at line 19