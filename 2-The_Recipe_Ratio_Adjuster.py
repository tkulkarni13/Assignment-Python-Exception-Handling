# Task 1: Start

while True: # loop to get answer for servings of recipe
    try:
        servings_recipe = int(input("How many servings is the recipe for: ")) # user input
        break
    except ValueError: # make sure user entered a valid number
        print("Please enter a valid number: ")
while True: # loop to get answer for servings needed by user
    try:
        servings_actual = int(input("How many servings would you wish to prepare: ")) # user input
        break
    except ValueError: # make sure user entered a valid number
        print("Please enter a valid number.")

# Task 2: Quantity Calculation
try:
    adjustment_factor = servings_actual / servings_recipe
except ZeroDivisionError: # if the user tries to enter a recipe with zero servings, the error message below will be shown to them
    print("You can't have a recipe with no servings.")
else:
    print("You should multiply all the recipe quantities by a factor of: ", adjustment_factor) # print out the adjustment factor so the recipe can be adjusted

# Task 3: Serving Success

finally: # prints a nice message for the user
    print("Enjoy coooking!")