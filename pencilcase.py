'''
title: Pencil Case
author: Chelsea Chen
date-created: 2021-02-22
'''
from objects import Pencil, Pen, Eraser, Highlighter

def getRawData(fileName):
	import csv
	tempLi = []
	fil = open(fileName)
	text = csv.reader(fil)
	for line in text:
		tempLi.append(line)
	return tempLi

class PencilCase():
    '''
    represents a pencil case where objects can be stored and taken out of
    '''
    def __init__(self,BRAND,POSITION):
        self.rawArr = getRawData('backpack - Sheet1.csv')
        self.PENCILCASEITEMS = [Pencil(self.rawArr[2][0]), Pen(self.rawArr[2][2],self.rawArr[2][0]), Pen(self.rawArr[2][3],self.rawArr[2][0]), Pen(self.rawArr[2][4],self.rawArr[2][0]), Pen(self.rawArr[2][5],self.rawArr[2][0]), Eraser(self.rawArr[2][0]), Highlighter(self.rawArr[2][7],self.rawArr[2][0])]
        # self.PENCILCASEITEMS = [Pencil("pencil case"), Pen("black","pencil case"), Pen("green","pencil case"), Pen("red","pencil case"), Pen("blue","pencil case"), Eraser("pencil case"), Highlighter("yellow","pencil case")]
        self.BRAND = BRAND
        self.POSITION = POSITION
        self.small = False

    def getPosition(self):
        return self.POSITION

    def setPosition(self, NEWPOSITION):
        self.POSITION = NEWPOSITION
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

    def getSize(self):
        return self.small

if __name__ == "__main__":
    PENCILCASE = PencilCase("yes","here")
    print(PENCILCASE.getObjectsCase())
