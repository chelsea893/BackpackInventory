'''
title: Main Code for Backpack Inventory
author: Chelsea Chen
date-created: 2021-02-22
'''
from backpack import Backpack
from locker import Locker
from pencilcase import PencilCase
from objects import Binder, Notebook, Pen, Highlighter, WritingUtensil
import sys

def inventory(TOTALINVENTORY, LIST):
    for items in LIST:
        TOTALINVENTORY.append(items)

class Main():
    '''
    Main code for the program
    '''
    def __init__(self):
        self.BACKPACK = Backpack("Eagle Creek")
        self.LOCKER = Locker()
        self.PENCILCASE = PencilCase("Bagsmart","Backpack")
        self.TOTALINVENTORY = []
        self.LOCATIONS = ["Locker","Backpack","pencil case"]
        self.OBJECTS = ["Binder", "Notebook", "Pen", "Highlighter", "Other Writing Utensil"]
        self.INVENTORY = True

    def inventory(self, TOTALINVENTORY, LIST):
        for items in LIST:
            TOTALINVENTORY.append(items)

    def startup(self):
        while self.INVENTORY == True:
            self.TOTALINVENTORY = []
            ''' Menu for Backpack inventory'''
            print("Welcome to Inventory!")
            print(self.LOCKER)
            print("----")
            ITEMSLOCKER = self.LOCKER.getLockObjects()
            for items in ITEMSLOCKER:
                print(items)

            print("")
            BACKPACKBRAND = self.BACKPACK.getBackpackBrand()
            print(f"{BACKPACKBRAND} backpack")
            print("----")
            ITEMSBACKPACK = self.BACKPACK.getBackpackObjects()
            for items in ITEMSBACKPACK:
                print(items)

            print("")
            PENCILCASEBRAND = self.PENCILCASE.getCaseBrand()
            print(f"{PENCILCASEBRAND} pencil case")
            print("----")
            ITEMSPENCILCASE = self.PENCILCASE.getObjectsCase()
            for items in ITEMSPENCILCASE:
                print(items)

            print(
"""
1) Move Item
2) Add new Item
3) QUIT
"""
            )
            CHOICE = int(input("> "))

            # ----- MOVE ITEM ----- #
            if CHOICE == 1:
                # create a list of all items in inventory
                inventory(self.TOTALINVENTORY, ITEMSPENCILCASE)
                inventory(self.TOTALINVENTORY,ITEMSBACKPACK)
                inventory(self.TOTALINVENTORY, ITEMSLOCKER)

                # Print out inventory
                for i in range(len(self.TOTALINVENTORY)):
                    print(f"{i + 1}) {self.TOTALINVENTORY[i]}")

                # Choose item to move and where to move it to
                MOVE = int(input("> "))
                ITEM = self.TOTALINVENTORY[MOVE-1]
                print(f"{ITEM} is in {ITEM.getPosition()}")
                print("Move to:")

                for i in range(len(self.LOCATIONS)):
                    if self.LOCATIONS[i] != ITEM.getPosition():
                        print(f"{i+1}) {self.LOCATIONS[i]}")
                NEWLOCATION = int(input("> "))
                NEWPOSITION = self.LOCATIONS[NEWLOCATION - 1]

                # Move item from backpack to locker
                if NEWPOSITION == "Locker" and ITEM.getPosition() == "Backpack":
                    self.LOCKER.addItem(ITEM)
                    self.BACKPACK.removeItem(self.BACKPACK.getBackpackObjects().index(ITEM))
                    ITEM.setPosition("Locker")

                # Move item from pencil case to locker
                if NEWPOSITION == "Locker" and ITEM.getPosition() == "pencil case":
                    self.LOCKER.addItem(ITEM)
                    self.PENCILCASE.removeItem(self.PENCILCASE.getObjectsCase().index(ITEM))
                    ITEM.setPosition("Locker")

                # Move item from pencil case to backpack
                if NEWPOSITION == "Backpack" and ITEM.getPosition() == "pencil case":
                    self.BACKPACK.addItem(ITEM)
                    self.PENCILCASE.removeItem(self.PENCILCASE.getObjectsCase().index(ITEM))
                    ITEM.setPosition("Backpack")

                # Move item from locker to backpack
                if NEWPOSITION == "Backpack" and ITEM.getPosition() == "Locker":
                    self.BACKPACK.addItem(ITEM)
                    self.LOCKER.removeItem(self.LOCKER.getLockObjects().index(ITEM))
                    ITEM.setPosition("Backpack")

                # Move item from locker to pencil case
                if NEWPOSITION == "pencil case" and ITEM.getPosition() == "Locker":
                    if ITEM.getSize() == True:
                        self.PENCILCASE.addItem(ITEM)
                        self.LOCKER.removeItem(self.LOCKER.getLockObjects().index(ITEM))
                        ITEM.setPosition("pencil case")
                    else:
                        print("Object can not fit in pencil case")

                # Move item from backpack to pencil case
                if NEWPOSITION == "pencil case" and ITEM.getPosition() == "Backpack":
                    if ITEM.getSize() == True:
                        self.PENCILCASE.addItem(ITEM)
                        self.BACKPACK.removeItem(self.BACKPACK.getBackpackObjects().index(ITEM))
                        ITEM.setPosition("pencil case")
                    else:
                        print("Object can not fit in pencil case")

            # ----- CREATE ITEM ----- #
            if CHOICE == 2:
                for i in range(len(self.OBJECTS)):
                    print(f"{i + 1}) {self.OBJECTS[i]}")
                CREATE = int(input("> "))

                # Create binder
                if CREATE == 1:
                    SUBJECT = str(input("SUBJECT: "))
                    self.LOCKER.addItem(Binder(SUBJECT,"Locker"))
                    print(self.LOCKER.getLockObjects())

                # Create notebook
                if CREATE == 2:
                    SUBJECT = str(input("SUBJECT: "))
                    self.LOCKER.addItem(Notebook(SUBJECT, "Locker"))
                    print(self.LOCKER.getLockObjects())

                # Create pen
                if CREATE == 3:
                    COLOUR = str(input("COLOUR: "))
                    self.LOCKER.addItem(Pen(COLOUR, "Locker"))
                    print(self.LOCKER.getLockObjects())

                # Create highlighter
                if CREATE == 4:
                    COLOUR = str(input("COLOUR: "))
                    self.LOCKER.addItem(Highlighter(COLOUR, "Locker"))
                    print(self.LOCKER.getLockObjects())

                # Create other writing utensil
                if CREATE == 5:
                    OBJECT = str(input("Other Writing Utensil: "))
                    self.LOCKER.addItem(WritingUtensil(OBJECT, "Locker"))
                    print(self.LOCKER.getLockObjects())

            # ---- EXIT ---- #
            if CHOICE == 3:
                sys.exit()


if __name__ == "__main__":
    MAIN = Main()
    MAIN.startup()





