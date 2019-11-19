#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:20:10 2019

Author: David Baraona
Course Number: DSCI 15310
Section Number: 002
Due Date: November 6, 2019
"""
print(__doc__)

import pandas as pd

#reads in the csv file
foodData = pd.read_csv("/Users/davidbaraona/Desktop/Assignment 4 CSV File.csv")

#converts the csv file into a list
mylist = foodData['food'].tolist()

def cheapMeal():
    """
    The function cheapMeal() accepts no arguments and performs the tasks
    needed to help the user find a cheap meal including displaying different
    entrees, sides, and drinks for the user to choose from
    """
    print(cheapMeal.__doc__)
    
    print("\nMain entree:\n")
    print(mylist[0:10])
    cheapEntree = input("What is your choice?\n")
    print("\nPick first side:\n")
    print(mylist[10:21])
    cheapSide1 = input("What is your first side?\n")
    print("\nPick second side:\n")
    print(mylist[10:21])
    cheapSide2 = input("What is your second side?\n")
    print("\nPick your drink:\n")
    print(mylist[21:22])
    cheapDrink = input("\nWhat is your drink?\n")
    print("\nYour meal is: ")
    print(cheapEntree + ",",cheapSide1 + ",",cheapSide2 + ",", cheapDrink)
    print("\nGood choice!")
    
def healthyMeal():
    """
    The function healthyMeal() accepts no arguments and performs the tasks
    needed to help the user find a healthy meal including displaying different
    entrees, sides, and drinks for the user to choose from
    """
    print(healthyMeal.__doc__)

    print("\nMain entree:\n")
    print(mylist[22:32])
    healthyEntree = input("What is your choice?\n")
    print("\nPick first side:\n")
    print(mylist[32:41])
    healthySide1 = input("What is your first side?\n")
    print("\nPick second side:\n")
    print(mylist[32:41])
    healthySide2 = input("what is your second side?\n")
    print("\nPick your drink:\n")
    print(mylist[41:48])
    healthyDrink = input("\nWhat is your drink?\n")
    print("\nYour meal is: ")
    print(healthyEntree + ",",healthySide1 + ",",healthySide2 + ",",healthyDrink)
    print("\nGood choice!")

def quickMeal():
    """
    The function quickMeal() accepts no arguments and performs the tasks
    needed to help the user find a quick meal including displaying different
    entrees, sides, and drinks for the user to choose from
    """
    print(quickMeal.__doc__)
    
    print("\nMain entree:\n")
    print(mylist[48:59])
    quickEntree = input("What is your choice?\n")
    print("\nPick first side:\n")
    print(mylist[59:65])
    quickSide1 = input("What is your first side?\n")
    print("\nPick second side:\n")
    print(mylist[59:65])
    quickSide2 = input("what is your second side?\n")
    print("\nPick your drink:\n")
    print(mylist[65:69])
    quickDrink = input("\nWhat is your drink?\n")
    print("\nYour meal is: ")
    print(quickEntree + ",",quickSide1 + ",",quickSide2 + ",",quickDrink)
    print("\nGood choice!")

def fastFood():
    """
    The function fastFood() accepts no arguments and performs the tasks
    needed to help the user find a fast food restaurant to eat at
    """
    print(fastFood.__doc__)
    
    print("\nFast food:\n")
    print(mylist[69:81])
    fastFoodChoice = input("What is your choice?\n")
    print("\nYour meal is: ")
    print(fastFoodChoice)
    print("\nGood choice!")
    
def restaurant():
    """
    The function restaurant() accepts no arguments and performs the tasks
    needed to help the user find a restaurant to eat at
    """
    print(restaurant.__doc__)
    
    print("\nRestaurants:\n")
    print(mylist[81:98])
    restaurantChoice = input("What is your choice?\n")
    print("\nYour meal is: ")
    print(restaurantChoice)
    print("\nGood choice!")


option = 'yes'

#loop used to restart after an error and to let the user go through until they  choose no
while option != 'no':
    meal = input("What type of meal do you choose? cheap meal at home, healthy meal at home, quick meal at home, fast food, restaurant\n")
    
    if meal != "cheap meal at home" and meal != "healthy meal at home" and meal != "quick meal at home" and meal!= "fast food" and meal != "restaurant":
        print("\nError. Please choose a correct option\n")
        continue
    elif meal == "cheap meal at home":
        cheapMeal()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "healthy meal at home":
        healthyMeal()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "quick meal at home":
        quickMeal()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "fast food":
        fastFood()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break
    elif meal == "restaurant":
        restaurant()
        option = input("Do you want to choose another meal? yes or no\n")
        if option == 'no':
            print("\nHave a nice meal")
            break

























    
