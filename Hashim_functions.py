# Name: Hashim Bukhtiar
# Date: June 12th, 2021
# File Name: Hashim_funcs.py
# Description: This is a module containing all of the functions required for 
# the main program.

from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def type_of_trash(trash):
    # Look for Peel's advice on how to dispose of the trash
    try:
        trash = trash.replace(" ", "+")

        link = f"https://www.peelregion.ca/scripts/waste/how-to-sort-your-waste.pl?action=search&query={trash}"
        r = requests.get(link)

        soup = BeautifulSoup(r.content, 'html.parser')

        garbage = soup.find('span', attrs={'style': 'font-size:1.1em'})

        return garbage.get_text()
    
    except:
        # If the item is CRC or garbage, it will not work with the previous
        # block of code, so this part accounts for that
        try:
            trash = trash.replace(" ", "+")

            link = f"https://www.peelregion.ca/scripts/waste/how-to-sort-your-waste.pl?action=search&query={trash}"
            r = requests.get(link)

            soup = BeautifulSoup(r.content, 'html.parser')

            garbage = soup.find('span', attrs={'style': 'font-size:1.2em'})
            Garbage = garbage.get_text()
            if "This item is garbage." in Garbage:
                Garbage += "Put this in your grey bin."

            elif "This item is reusable waste." in Garbage or "HHW" in Garbage:
                Garbage += "\nDispose of this at your local CRC."

            return Garbage
        
        except:
            # If all else fails, we give the user more information to check 
            # their piece of waste themselves.
            driver = webdriver.Chrome()
            link = f"https://www.peelregion.ca/scripts/waste/how-to-sort-your-waste.pl?action=search&query={trash}"
            driver.get(link)
            return 'More Information Given'

def environmental_impact(grn, blu, grbg, yrd, spec):
    print("\nCongratulations on contributing to a more sustainable world!\n")
    composting = round(0.65 * (2.26 * grn), 2) # Calculates compost in kg
    garbage_incinerated = round(0.7 * grbg, 2) # Calculates amount of garbage incinerated
    blu = round(0.6 * blu, 2) # Calculates amount of blue bin items were recycled

    # Tell the user how much green bin waste went towards composting 
    if grn > 0:
        print(f"You contributed about {composting} kilograms of waste to \
fertilization/ composting, and prevented it from ending up in landfills!")

    # Tell the user how many items they recycled
    if blu > 0:
        print(f"You recycled about {blu} items that will be reused instead of polluting \
the environment!")

    # Tell the user how many garbage items were incinerated
    if grbg > 0:
        print(f"You allowed about {garbage_incinerated} items to be incinerated instead of \
going to landfills!")

    # Tell the user how many yard waste items they disposed of
    if yrd > 0:
        print(f"You sent {yrd} yard waste items to be disposed of properly!")
    
    # Tell the user how many special items (CRC or other) they properly disposed of
    if spec > 0:
        print(f"You allowed {spec} items to be disposed of in the corrent \
manner, saving the environment a lot of potential harm!")