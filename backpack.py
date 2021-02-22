'''
title: Backpack
author: Chelsea Chen
date-created: 2021-02-22
'''
from main import Binder
class Backpack():
    '''
    Represents a Backpack for items to be stored
    '''
    def __init__(self,BRAND):
        self.OBJECTSCARRIED = [Binder("LA")]
        self.BRAND = BRAND

    def addItem(self,ITEM):
        return self.OBJECTSCARRIED.append(ITEM)

    def removeItem(self,ITEM):
        return self.OBJECTSCARRIED.pop(ITEM)

    def getBackpackObjects(self):
        return self.OBJECTSCARRIED

if __name__ == "__main__":
    BACKPACK = Backpack("yes")
    print(BACKPACK.getBackpackObjects())



