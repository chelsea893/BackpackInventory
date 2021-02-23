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

    def startUp(self):
        while self.INVENTORY == True:
            self.TOTALINVENTORY = []
            ''' Menu for Backpack inventory'''
            print("Welcome to Inventory!")
            print("""
Locker
----
            """)
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
            if CHOICE == 1:
                for items in ITEMSPENCILCASE:
                    self.TOTALINVENTORY.append(items)
                for items in ITEMSBACKPACK:
                    self.TOTALINVENTORY.append(items)
                for items in ITEMSLOCKER:
                    self.TOTALINVENTORY.append(items)
                for i in range(len(self.TOTALINVENTORY)):
                    print(f"{i + 1}) {self.TOTALINVENTORY[i]}")
                MOVE = int(input("> "))
                print(f"{self.TOTALINVENTORY[MOVE-1]} is in {self.TOTALINVENTORY[MOVE - 1].getPosition()}")
                print("Move to:")
                for i in range(len(self.LOCATIONS)):
                    if self.LOCATIONS[i] != self.TOTALINVENTORY[MOVE - 1].getPosition():
                        print(f"{i+1}) {self.LOCATIONS[i]}")
                NEWLOCATION = int(input("> "))
                if self.LOCATIONS[NEWLOCATION -1] == "Locker" and self.TOTALINVENTORY[MOVE - 1].getPosition() == "Backpack":
                    self.LOCKER.addItem(self.TOTALINVENTORY[MOVE - 1])
                    self.BACKPACK.removeItem(self.BACKPACK.getBackpackObjects().index(self.TOTALINVENTORY[MOVE - 1]))
                    self.TOTALINVENTORY[MOVE - 1].setPosition("Locker")
                    print(self.LOCKER.getLockObjects())
                    print(self.BACKPACK.getBackpackObjects())

                if self.LOCATIONS[NEWLOCATION -1] == "Locker" and self.TOTALINVENTORY[MOVE - 1].getPosition() == "pencil case":
                    self.LOCKER.addItem(self.TOTALINVENTORY[MOVE - 1])
                    self.PENCILCASE.removeItem(self.PENCILCASE.getObjectsCase().index(self.TOTALINVENTORY[MOVE - 1]))
                    self.TOTALINVENTORY[MOVE - 1].setPosition("Locker")
                    print(self.LOCKER.getLockObjects())
                    print(self.BACKPACK.getBackpackObjects())

                if self.LOCATIONS[NEWLOCATION -1] == "Backpack" and self.TOTALINVENTORY[MOVE - 1].getPosition() == "pencil case":
                    self.BACKPACK.addItem(self.TOTALINVENTORY[MOVE - 1])
                    self.PENCILCASE.removeItem(self.PENCILCASE.getObjectsCase().index(self.TOTALINVENTORY[MOVE - 1]))
                    self.TOTALINVENTORY[MOVE - 1].setPosition("Backpack")
                    print(self.BACKPACK.getBackpackObjects())
                    print(self.PENCILCASE.getObjectsCase())

                if self.LOCATIONS[NEWLOCATION -1] == "Backpack" and self.TOTALINVENTORY[MOVE - 1].getPosition() == "Locker":
                    self.BACKPACK.addItem(self.TOTALINVENTORY[MOVE - 1])
                    self.LOCKER.removeItem(self.LOCKER.getLockObjects().index(self.TOTALINVENTORY[MOVE - 1]))
                    self.TOTALINVENTORY[MOVE - 1].setPosition("Backpack")
                    print(self.BACKPACK.getBackpackObjects())
                    print(self.LOCKER.getLockObjects())

                if self.LOCATIONS[NEWLOCATION -1] == "pencil case" and self.TOTALINVENTORY[MOVE - 1].getPosition() == "Locker":
                    if self.TOTALINVENTORY[MOVE - 1].getSize() == True:
                        self.PENCILCASE.addItem(self.TOTALINVENTORY[MOVE - 1])
                        self.LOCKER.removeItem(self.LOCKER.getLockObjects().index(self.TOTALINVENTORY[MOVE - 1]))
                        self.TOTALINVENTORY[MOVE - 1].setPosition("pencil case")
                    else:
                        print("Object can not fit in pencil case")
                        print(self.PENCILCASE.getObjectsCase())
                        print(self.LOCKER.getLockObjects())
                if self.LOCATIONS[NEWLOCATION -1] == "pencil case" and self.TOTALINVENTORY[MOVE - 1].getPosition() == "Backpack":
                    if self.TOTALINVENTORY[MOVE - 1].getSize() == True:
                        self.PENCILCASE.addItem(self.TOTALINVENTORY[MOVE - 1])
                        self.BACKPACK.removeItem(self.BACKPACK.getBackpackObjects().index(self.TOTALINVENTORY[MOVE - 1]))
                        self.TOTALINVENTORY[MOVE - 1].setPosition("pencil case")
                    else:
                        print("Object can not fit in pencil case")
                        print(self.PENCILCASE.getObjectsCase())
                        print(self.BACKPACK.getBackpackObjects())
            if CHOICE == 2:
                for i in range(len(self.OBJECTS)):
                    print(f"{i + 1}) {self.OBJECTS[i]}")
                CREATE = int(input("> "))
                if CREATE == 1:
                    SUBJECT = str(input("SUBJECT: "))
                    self.LOCKER.addItem(Binder(SUBJECT,"Locker"))
                    print(self.LOCKER.getLockObjects())
                if CREATE == 2:
                    SUBJECT = str(input("SUBJECT: "))
                    self.LOCKER.addItem(Notebook(SUBJECT, "Locker"))
                    print(self.LOCKER.getLockObjects())
                if CREATE == 3:
                    COLOUR = str(input("COLOUR: "))
                    self.LOCKER.addItem(Pen(COLOUR, "Locker"))
                    print(self.LOCKER.getLockObjects())
                if CREATE == 4:
                    COLOUR = str(input("COLOUR: "))
                    self.LOCKER.addItem(Highlighter(COLOUR, "Locker"))
                    print(self.LOCKER.getLockObjects())
                if CREATE == 5:
                    OBJECT = str(input("Other Writing Utensil: "))
                    self.LOCKER.addItem(WritingUtensil(OBJECT, "Locker"))
                    print(self.LOCKER.getLockObjects())
            if CHOICE == 3:
                sys.exit()


if __name__ == "__main__":
    MAIN = Main()
    MAIN.startUp()




