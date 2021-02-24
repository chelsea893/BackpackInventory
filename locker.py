'''
title: Locker
author: Chelsea Chen
date-created: 2021-02-22
'''
from objects import Binder, Notebook

def getRawData(fileName):
	import csv
	tempLi = []
	fil = open(fileName)
	text = csv.reader(fil)
	for line in text:
		tempLi.append(line)
	return tempLi

class Locker():
    '''
    Represents a Locker where objects can be stored and taken out of
    '''
    def __init__(self):
        self.rawArr = getRawData('backpack - Sheet1.csv')
        self.LOCKERITEMS = [Binder(self.rawArr[0][1], self.rawArr[0][0]), Notebook(self.rawArr[0][2], self.rawArr[0][0])]
        #self.LOCKERITEMS = [Binder("English/Social Studies", "Locker"), Notebook("Art/AGA", "Locker")]

    def addItem(self,ITEM):
        return self.LOCKERITEMS.append(ITEM)

    def removeItem(self,ITEM):
        return self.LOCKERITEMS.pop(ITEM)

    def getLockObjects(self):
        return self.LOCKERITEMS

    def __repr__(self):
        return f"Locker"

if __name__ == "__main__":
    rawArr = getRawData('backpack - Sheet1.csv')
    print(rawArr)

    LOCKER = Locker()
    print(LOCKER.getLockObjects())
