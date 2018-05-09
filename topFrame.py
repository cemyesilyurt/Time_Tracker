"""
File topFrame.
Defines class TopFrame.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

from tkinter import Frame, LEFT, RIGHT, TOP, BOTTOM, BOTH, X, Y
from buttonsFrame import ButtonsFrame
from listsScrollbarFrame import ListsScrollbarFrame
from listsFrame import ListsFrame

class TopFrame(Frame):
    
    def __init__(self, parent, controller):
        
        # create frame
        Frame.__init__(self,master=parent,width=3000,height=200)
        self.controller = controller
        
        # create subframes                         
        self.bFrame = ButtonsFrame(
            parent=self,controller=self.controller)
        self.lsFrame = ListsScrollbarFrame(
            parent=self,controller=self.controller)        
        
        # place frame
        self.grid()
    
        # place subframes        
        self.bFrame.grid(row=0,column=0)
        self.lsFrame.grid(row=0,column=1)
        
        # color the subframes
        self.bFrame.config(bg = 'cyan')        
        self.lsFrame.config(bg = 'yellow')        
        
        # key points to ensure that frames are placed in the way we want: 
        # - carry masters through class definitions
        # - do not use pack / grid on self until you are sure
        #   how you want to place it; do placement of a child
        #   in its parent's class
