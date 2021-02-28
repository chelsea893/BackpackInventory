# CSE3120-Project

## Backpack Inventory
This program allows for the user to alter the inventory of a locker, backpack, and a pencil case by being able to add objects
and move them to each of the different locations.

## External files
- Requires Python 3.8 to function 

## How to run Program
- Retrieve all files from git (CSE3120-Project) and upload onto Pycharm
- Run the main.py file 
- Follow instructions given on the menu upon running the program

## Use of Abstraction, Aggregation, and Encapsulation in Program

### Abstraction
In this program, I used abstraction to set the level of detail needed for each of the objects in the program, such as objects such as the locker, backpack, pencil case, tablet, laptop, binder, etc. For example, there are a lot more attributes that the backpack could have, such as the colour, but I specified the details to those that were relevant to the program, such as being able to add or remove an object form the backpack.

### Aggregation 
Using aggregation, I grouped objects together based on their location in arrays so that their location could be accessed and changed.

### Encapsulation
For each of the objects, I used setter and getter methods to encapsulate what was necessary for the program to function. For example, for the backpack, locker, and pencil case I created getter methods to return a list of the objects that were in their inventory and for the other objects in objects.py I created getter and setter methods to retrieve and set their location.