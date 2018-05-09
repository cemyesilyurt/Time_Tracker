"""
File listsCanvas.
Defines class ListsCanvas.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

from tkinter import Canvas, Scrollbar, TOP, BOTTOM, BOTH, X, Y, HORIZONTAL
from listsFrame import ListsFrame

class ListsCanvas(Canvas):
    
    def __init__(self, parent, controller):
        
        # create canvas
        Canvas.__init__(self,master=parent,scrollregion=(0,0,3000,200))
        self.controller = controller        

        # create subframe
        self.lFrame = ListsFrame(parent=self,controller=self.controller)        
                                
        # create scrollbar        
        self.hBar=Scrollbar(master=parent,orient=HORIZONTAL)    

        # place subframe        
        self.lFrame.pack(fill=BOTH)
        
        # place scrollbar
        self.hBar.pack(side=BOTTOM,fill=X)
        
        # configure scrollbar
        self.hBar.config(command=self.xview)  
                        
        # configure canvas        
        self.config(xscrollcommand=self.hBar.set)                