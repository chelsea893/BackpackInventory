'''
title: Main Code for Backpack Inventory
author: Chelsea Chen
date-created: 2021-02-22
'''

class Binder():
    def __init__(self, SUBJECT):
        self.SUBJECT = SUBJECT
    def __str__(self):
        return f"{self.SUBJECt} binder"

class Notebook():
    def __init__(self, SUBJECT):
        self.SUBJECT = SUBJECT

class Pen():
    def __init__(self, COLOUR):
        self.COLOUR = COLOUR

class Laptop():
    def __init__(self, BRAND):
        self.BRAND = BRAND

class Tablet():
    def __init__(self,BRAND):
        self.BRAND = BRAND

class Highlighter():
    def __init__(self,COLOUR):
        self.COLOUR = COLOUR

class Eraser():
    def __init__(self):
        self.ITEM = ERASER

class Pencil():
    def __init__(self):
        self.ITEM = PENCIL

class Main():
    '''
    Main code for the program
    '''
    def __init__(self):
        self.BACKPACK = Backpack()
        self.LOCKER = Locker()
        self.PENCILCASE = PencilCase()


