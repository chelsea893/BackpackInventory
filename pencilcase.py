'''
title: Pencil Case
author: Chelsea Chen
date-created: 2021-02-22
'''
from objects import Pencil, Pen, Eraser, Highlighter
class PencilCase():
    '''
    represents a pencil case where objects can be stored and taken out of
    '''
    def __init__(self,BRAND,POSITION):
        self.PENCILCASEITEMS = [Pencil("pencil case"), Pen("black","pencil case"), Pen("green","pencil case"), Pen("red","pencil case"), Pen("blue","pencil case"), Eraser("pencil case"), Highlighter("yellow","pencil case")]
        self.OBJECTLIST = []
        self.BRAND = BRAND
        self.POSITION = POSITION

    def getPosition(self):
        return self.POSITION

    def addItem(self,ITEM):
        return self.PENCILCASEITEMS.append(ITEM)

    def removeItem(self,ITEM):
        self.PENCILCASEITEMS.pop(ITEM)

    def getObjectsCase(self):
        return self.PENCILCASEITEMS

    def __repr__(self):
        return f"{self.BRAND} pencil case"

    def getCaseBrand(self):
        return self.BRAND

if __name__ == "__main__":
    PENCILCASE = PencilCase("yes")
    print(PENCILCASE.getObjectsCase())
