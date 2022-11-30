# Name: Hashim Bukhtiar
# Date: June 12th, 2021
# File Name: main.py
# Project Name: Sort-O-Matic
# Description: This program allows the user to sort their waste by checking 
# the type of item they have with the Peel website. If it cannnot find the item,
# the program takes the user to a site where they can find more information.
# At the end, it tells them how they contributed to the environment and made 
# the world more sustainable.
# Test Cases:

# INPUT 1:
# batteries
# 3
# brush
# 1
# Food and leftovers
# 4
# plastic
# 7
# Done
# OUTPUT 1:
# This item is household hazardous waste (HHW).
# Dispose of this at your local CRC.
#
# Put this item in a yard waste bag, container, or bushel basket.
#
# Put this item in your organics (green) cart.
#
# More Information Given
#
# Congratulations on contributing to a more sustainable world!
#
# You contributed about 5.88 kilograms of waste to fertilization/ composting, and prevented it from ending up in landfills!
# You sent 1 yard waste items to be disposed of properly!
# You allowed 10 items to be disposed of in the corrent manner, saving the environment a lot of potential harm!
# 
# Thank you for using this program! Have a nice day!

from sys import stdin
from time import sleep
import Hashim_functions

green = 0
blue = 0
garbage = 0
yard = 0
CRC = 0
special = 0

while True:
    # Get the type of trash from the user
    print("Please enter the kind of waste you wish to dispose of, or type 'Done' if you are done: ")
    trash = stdin.readline().strip('\n')
    
    if trash != "Done":
        try:
            # Get the number items the user is disposing of
            print(f"How many {trash} items are you disposing of?")
            num_of_items = int(stdin.readline().strip('\n'))

            # Pass info into the function
            result = Hashim_functions.type_of_trash(trash)
            print('\n'+result+'\n')

            # Add the appropriate number of items to the proper category
            if 'yard' in result:
                yard += num_of_items

            elif 'blue' in result:
                blue += num_of_items
            
            elif 'green' in result:
                green += num_of_items

            elif 'garbage' in result:
                garbage += num_of_items

            elif 'reusable waste' in result:
                CRC += num_of_items

            else:
                special += num_of_items

        # In case the user doesn't enter an integer, the program won't crash
        except:
            print("Error: Please enter an integer when asked about the number of items.")

    # If the user enters 'Done' loop is broken
    else:
        break

# Environmental Impact - Tell the user how they contributed to the environment
Hashim_functions.environmental_impact(green, blue, garbage, yard, special)

print("\nThank you for using this program! Have a nice day!")

sleep(10)