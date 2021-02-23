'''
title: Backpack
author: Chelsea Chen
date-created: 2021-02-22
'''
from objects import Binder, Notebook, Laptop, Tablet
from pencilcase import PencilCase

def getRawData(fileName):
	import csv
	tempLi = []
	fil = open(fileName)
	text = csv.reader(fil)
	for line in text:
		tempLi.append(line)
	return tempLi

class Backpack():
    '''
    Represents a Backpack for items to be stored
    '''
    def __init__(self,BRAND):
        self.rawArr = getRawData('backpack - Sheet1.csv')
        self.OBJECTSCARRIED = [Laptop(self.rawArr[1][0]),Tablet(self.rawArr[1][0]), Binder(self.rawArr[1][3], self.rawArr[1][0]), PencilCase(self.rawArr[1][4],self.rawArr[1][0])]
        #self.OBJECTSCARRIED = [Laptop("Backpack"),Tablet("Backpack"), Binder("Math/Science", "Backpack"), PencilCase("Bagsmart","Backpack")]
        self.BRAND = BRAND

    def addItem(self,ITEM):
        return self.OBJECTSCARRIED.append(ITEM)

    def removeItem(self,ITEM):
        return self.OBJECTSCARRIED.pop(ITEM)

    def getBackpackObjects(self):
        return self.OBJECTSCARRIED

    def getBackpackBrand(self):
        return self.BRAND

    def __repr__(self):
        return f"{self.BRAND} backpack"


if __name__ == "__main__":
    BACKPACK = Backpack("yes")
    print(BACKPACK.getBackpackObjects())



