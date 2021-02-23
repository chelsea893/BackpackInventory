'''
title: Locker
author: Chelsea Chen
date-created: 2021-02-22
'''
from objects import Binder, Notebook
class Locker():
    '''
    Represents a Locker where objects can be stored and taken out of
    '''
    def __init__(self):
        self.LOCKERITEMS = [Binder("English/Social Studies", "Locker"), Notebook("Art/AGA", "Locker")]

    def addItem(self,ITEM):
        return self.LOCKERITEMS.append(ITEM)

    def removeItem(self,ITEM):
        return self.LOCKERITEMS.append(ITEM)

    def getLockObjects(self):
        return self.LOCKERITEMS

if __name__ == "__main__":
    LOCKER = Locker()
    print(LOCKER.getLockObjects())
