'''
title: Objects for Backpack Inventory
author: Chelsea Chen
date-created: 2021-02-22
'''
class Binder():
    def __init__(self, SUBJECT, POSITION):
        self.SUBJECT = SUBJECT
        self.POSITION = POSITION
        self.small = False

    def __repr__(self):
        return f"{self.SUBJECT} binder"

    def getPosition(self):
        return self.POSITION

    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION

    def getSize(self):
        return self.small

class Notebook():
    def __init__(self, SUBJECT, POSITION):
        self.SUBJECT = SUBJECT
        self.POSITION = POSITION
        self.small = False
    def __repr__(self):
        return f"{self.SUBJECT} notebook"
    def getPosition(self):
        return self.POSITION
    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION

    def getSize(self):
        return self.small

class Pen():
    def __init__(self, COLOUR,POSITION):
        self.COLOUR = COLOUR
        self.POSITION = POSITION
        self.small = True
    def __repr__(self):
        return f"{self.COLOUR} pen"
    def getPosition(self):
        return self.POSITION
    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION
    def getSize(self):
        return self.small

class Laptop():
    def __init__(self,POSITION):
        self.POSITION = POSITION
        self.small = False
    def __repr__(self):
        return "Laptop"
    def getPosition(self):
        return self.POSITION
    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION
    def getSize(self):
        return self.small


class Tablet():
    def __init__(self,POSITION):
        self.POSITION = POSITION
        self.small = False
    def __repr__(self):
        return "Tablet"
    def getPosition(self):
        return self.POSITION
    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION
    def getSize(self):
        return self.small


class Highlighter():
    def __init__(self,COLOUR,POSITION):
        self.COLOUR = COLOUR
        self.POSITION = POSITION
        self.small = True

    def __repr__(self):
        return f"{self.COLOUR} Highlighter"
    def getPosition(self):
        return self.POSITION
    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION
    def getSize(self):
        return self.small


class Eraser():
    def __init__(self,POSITION):
        self.POSITION = POSITION
        self.small = True
    def __repr__(self):
        return "Eraser"
    def getPosition(self):
        return self.POSITION
    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION
    def getSize(self):
        return self.small

class Pencil():
    def __init__(self,POSITION):
        self.POSITION = POSITION
        self.small = True
    def __repr__(self):
        return "Pencil"
    def getPosition(self):
        return self.POSITION
    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION
    def getSize(self):
        return self.small

class WritingUtensil():
    def __init__(self,OBJECT,POSITION):
        self.small = True
        self.POSITION = POSITION
        self.OBJECT = OBJECT
    def __repr__(self):
        return f"{self.OBJECT}"

    def getPosition(self):
        return self.POSITION

    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
        return self.POSITION

    def getSize(self):
        return self.small

