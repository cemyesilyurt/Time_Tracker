"""
File listsScrollbarFrame.
Defines class ListsScrollbarFrame.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

from tkinter import Frame
from listsCanvas import ListsCanvas

class ListsScrollbarFrame(Frame):
    
    def __init__(self, parent, controller):
        
        # create frame
        Frame.__init__(self,master=parent,padx=10,pady=10)
        self.controller = controller
        
        # create canvas
        self.lCanvas = ListsCanvas(parent=self, controller=self.controller)        
        
        # place canvas
        self.lCanvas.pack()