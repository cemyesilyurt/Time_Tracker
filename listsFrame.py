"""
File listsFrame.
Defines class ListsFrame.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

from tkinter import Frame, TOP, BOTTOM, BOTH
from projectsFrame import ProjectsFrame
from sessionsFrame import SessionsFrame

class ListsFrame(Frame):
    
    def __init__(self, parent, controller):
        
        # create frame
        Frame.__init__(self,master=parent)
        self.controller = controller        
        
        # create subframes        
        self.pFrame = ProjectsFrame(parent=self,controller=self.controller)        
        self.sFrame = SessionsFrame(parent=self,controller=self.controller)
                
        # place subframes        
        self.pFrame.pack(fill=BOTH,expand=True)
        self.sFrame.pack(fill=BOTH,expand=True)