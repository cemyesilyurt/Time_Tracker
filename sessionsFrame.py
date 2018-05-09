"""
File sessionsFrame.
Defines class SessionsFrame.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

from tkinter import Frame, Button, Label, GROOVE

class SessionsFrame(Frame):
    
    def __init__(self, parent, controller):
        
        # construct frame, set controller
        Frame.__init__(self,master=parent,borderwidth=3,
                       relief=GROOVE,padx=10,pady=10)
        self.controller = controller
        
        # create labels
        
        self.listLabel = Label(master=self)
        self.listLabel["text"] = "Active Sessions:"
        self.listLabel["width"] = 17
        self.listLabel["anchor"] = "w"
                
        self.numberLabel = Label(master=self)
        self.numberLabel["text"] = "#"
        self.numberLabel["width"] = 17
        self.numberLabel["anchor"] = "w"
        
        self.projectLabel = Label(master=self)
        self.projectLabel["text"] = "Project:"        
        self.projectLabel["width"] = 17
        self.projectLabel["anchor"] = "w"

        self.durationLabel = Label(master=self)
        self.durationLabel["text"] = "Duration (min):"        
        self.durationLabel["width"] = 17
        self.durationLabel["anchor"] = "w"

        self.startLabel = Label(master=self)
        self.startLabel["text"] = "Start:"        
        self.startLabel["width"] = 17
        self.startLabel["anchor"] = "w"

        self.endLabel = Label(master=self)
        self.endLabel["text"] = "End:"        
        self.endLabel["width"] = 17
        self.endLabel["anchor"] = "w"
                
        self.statusLabel = Label(master=self)
        self.statusLabel["text"] = "Status:"            
        self.statusLabel["width"] = 17
        self.statusLabel["anchor"] = "w"
        
        # place labels

        self.listLabel.grid(row=0, column=0, sticky="w")
        self.numberLabel.grid(row=1, column=0, sticky="w")
        self.projectLabel.grid(row=2, column=0, sticky="w")
        self.durationLabel.grid(row=3, column=0, sticky="w")
        self.startLabel.grid(row=4, column=0, sticky="w")
        self.endLabel.grid(row=5, column=0, sticky="w")
        self.statusLabel.grid(row=6, column=0, sticky="w")