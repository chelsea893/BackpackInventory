'''
title: Locker
author: Chelsea Chen
date-created: 2021-02-22
'''

class Locker():
    '''
    Represents a Locker where objects can be stored and taken out of
    '''
    def __init__(self):
        self.LOCKERITEMS = []

    def addItem(self,ITEM):
        return self.LOCKERITEMS.append(ITEM)

    def removeItem(self,ITEM):
        return self.LOCKERITEMS.append(ITEM)

    def getLockObjects(self):
        return self.LOCKERITEMS