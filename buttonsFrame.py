"""
File buttonsFrame.
Defines class ButtonsFrame.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

from tkinter import Frame, Button, Label, GROOVE, CENTER

class ButtonsFrame(Frame):
    
    def __init__(self, parent, controller):
        
        # construct frame, set controller
        Frame.__init__(self,master=parent,borderwidth=3,
                       relief=GROOVE,padx=10,pady=10)                                              
        self.controller = controller
        
        # create buttons and labels
        
        self.manageProjectsLabel = Label(master=self)
        self.manageProjectsLabel["text"] = 'Manage Projects:'
        
        self.createProjectButton = Button(master=self)
        self.createProjectButton["text"] = 'Create Project'
        self.createProjectButton["width"] = 17
        self.createProjectButton["justify"] = CENTER
        self.createProjectButton["command"] = self.controller.createProject
                
        self.updateProjectStatusButton = Button(master=self)
        self.updateProjectStatusButton["text"] = 'Update Project Status'
        self.updateProjectStatusButton["width"] = 17
        self.updateProjectStatusButton["justify"] = CENTER
        self.updateProjectStatusButton["command"] = \
            self.controller.updateProjectStatus
        
        self.emptyLabel1 = Label(master=self,text='',bg='cyan')

        self.manageSessionsLabel = Label(master=self)
        self.manageSessionsLabel["text"] = 'Manage Sessions:'
                
        self.startSessionButton = Button(master=self)
        self.startSessionButton["text"] = 'Start Session'
        self.startSessionButton["width"] = 17
        self.startSessionButton["justify"] = CENTER
        self.startSessionButton["command"] = self.controller.startSession
        
        self.endSessionButton = Button(master=self)
        self.endSessionButton["text"] = 'End Session'
        self.endSessionButton["justify"] = CENTER
        self.endSessionButton["width"] = 17
        self.endSessionButton["command"] = self.controller.endSession
        
        self.emptyLabel2 = Label(master=self,text='',bg='cyan')
        
        self.exportLabel = Label(master=self)
        self.exportLabel["text"] = 'Export Work Log:'
        
        self.exportByDateButton = Button(master=self)
        self.exportByDateButton["text"] = 'By Date'        
        self.exportByDateButton["width"] = 17
        self.exportByDateButton["justify"] = CENTER
        self.exportByDateButton["command"] = self.controller.exportByDate
        
        self.exportByProjectButton = Button(master=self)
        self.exportByProjectButton["text"] = 'By Project'        
        self.exportByProjectButton["width"] = 17
        self.exportByProjectButton["justify"] = CENTER
        self.exportByProjectButton["command"] = self.controller.exportByProject
        
        self.exportAllDataButton = Button(master=self)
        self.exportAllDataButton["text"] = 'All Data'        
        self.exportAllDataButton["width"] = 17
        self.exportAllDataButton["justify"] = CENTER
        self.exportAllDataButton["command"] = self.controller.exportAllData     
                
        self.emptyLabel3 = Label(master=self,text='',bg='cyan')                                
        
        self.refreshLabel = Label(master=self)
        self.refreshLabel["text"] = 'Refresh Database:'
        
        self.deleteAllDataButton = Button(master=self)
        self.deleteAllDataButton["text"] = "Delete All Data"
        self.deleteAllDataButton["width"] = 17
        self.deleteAllDataButton["justify"] = CENTER
        self.deleteAllDataButton["command"] = self.controller.deleteAllData
        
        self.emptyLabel4 = Label(master=self,bg='cyan')
        
        self.quitButton = Button(master=self)
        self.quitButton["text"] = "Quit"
        self.quitButton["width"] = 17
        self.quitButton["justify"] = CENTER
        self.quitButton["command"] = self.quit        
        
        self.emptyLabel5 = Label(master=self,bg='cyan')                                                                            
                                      
        # place buttons and labels using pack    
                
        self.manageProjectsLabel.pack()
        self.createProjectButton.pack()
        self.updateProjectStatusButton.pack()
        
        self.emptyLabel1.pack()
        
        self.manageSessionsLabel.pack()
        self.startSessionButton.pack()
        self.endSessionButton.pack()
        
        self.emptyLabel2.pack()
        
        self.exportLabel.pack()
        self.exportByDateButton.pack()
        self.exportByProjectButton.pack()
        self.exportAllDataButton.pack()
        
        self.emptyLabel3.pack()
        self.refreshLabel.pack()
        self.deleteAllDataButton.pack()
        
        self.emptyLabel4.pack()
        
        self.quitButton.pack()
        self.emptyLabel5.pack()              