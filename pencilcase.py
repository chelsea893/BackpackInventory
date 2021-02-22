'''
title: Pencil Case
author: Chelsea Chen
date-created: 2021-02-22
'''

class PencilCase():
    '''
    represents a pencil case where objects can be stored and taken out of
    '''
    def __init__(self,BRAND):
        self.PENCILCASEITEMS = []
        self.OBJECTLIST = []
        self.BRAND = BRAND

    def addItem(self,ITEM):
        for object in self.OBJECTLIST:
            if object == ITEM:
                return self.PENCILCASEITEMS.append(ITEM)
            else:
                print("Object can not fit in pencil case!")

    def removeItem(self:
        self.PENCILCASEITEMS.pop()

    def getObjectsCase(self):
        return self.PENCILCASEITEMS
