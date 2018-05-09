"""
File projectsFrame.
Defines class ProjectsFrame.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

from tkinter import Frame, Button, Label, GROOVE

class ProjectsFrame(Frame):
    
    def __init__(self, parent, controller):
        
        # construct frame, set controller
        Frame.__init__(self,master=parent,borderwidth=3,
                       relief=GROOVE,padx=10,pady=10)
        self.controller = controller
        
        # create labels
        
        self.listLabel = Label(master=self)
        self.listLabel["text"] = "Ongoing Projects:"
        self.listLabel["width"] = 17
        self.listLabel["anchor"] = "w"
                
        self.numberLabel = Label(master=self)
        self.numberLabel["text"] = "#"
        self.numberLabel["width"] = 17
        self.numberLabel["anchor"] = "w"
        
        self.nameLabel = Label(master=self)
        self.nameLabel["text"] = "Name:"        
        self.nameLabel["width"] = 17
        self.nameLabel["anchor"] = "w"
        
        self.statusLabel = Label(master=self)
        self.statusLabel["text"] = "Status:"            
        self.statusLabel["width"] = 17
        self.statusLabel["anchor"] = "w"                
        
        # place labels
        
        self.listLabel.grid(row=0, column=0, sticky="w")
        self.numberLabel.grid(row=1, column=0, sticky="w")
        self.nameLabel.grid(row=2, column=0, sticky="w")
        self.statusLabel.grid(row=3, column=0, sticky="w")
    