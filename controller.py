"""
File controller.
Defines class Controller.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

import tkinter
from myDB import MyDB   # MODEL
from topFrame import TopFrame  # VIEW
from projectsFrame import ProjectsFrame
from sessionsFrame import SessionsFrame
import datetime

class Controller:        
      
      
    def __init__(self):
        """
        Creates model and view to be used with this controller.
        """        
        root = tkinter.Tk()          
        root.title('Time Tracker by Cem H. Yesilyurt')        
        self.model = MyDB()
        self.view = TopFrame(parent=root,controller=self)
        self.displayProjectsAndSessions()
        self.view.mainloop()
        root.destroy()
    
    
    def createProject(self):
        """
        Callback function for create project button.
        """        
        # pop up toplevel window with entry and ok, cancel buttons
        # enter project name in entry
        # when click ok, get entry text and create project with name as entry text
        # display project info in projects pane
        
        messageBox = tkinter.Toplevel()
        mInfo = tkinter.Label(master=messageBox, 
                              text = "Please enter the project's name:",
                              width=30, height=2)
        mEntry = tkinter.Entry(master=messageBox, width = 30)        
        mEmptyLabel1 = tkinter.Label(master=messageBox)
        mOkButton = tkinter.Button(master=messageBox,text = 'Ok', width=15)
        mCancelButton = tkinter.Button(master=messageBox,
                                       text = 'Cancel', width=15)
        mOkButton['command'] = lambda: \
            self.createProjectCommand(messageBox, mEntry)
        mCancelButton['command'] = messageBox.destroy
        mEmptyLabel2 = tkinter.Label(master=messageBox)
        mInfo.pack()
        mEntry.pack()
        mEmptyLabel1.pack()
        mOkButton.pack()
        mCancelButton.pack()
        mEmptyLabel2.pack()
        # to make the toplevel the active window and place the cursor in 
        # the Entry when the toplevel comes up
        mEntry.focus_set()
        # so that pressing enter hits ok:
        mEntry.bind('<Return>', lambda event: \
                    self.createProjectCommand(messageBox, mEntry))
        
        
    
    def createProjectCommand(self, messageBox, mEntry):
        """
        Callback function for create project toplevel's ok button.
        """    
        projectName = mEntry.get()
        self.model.createProject({'name': projectName, 'status': 'Ongoing'})
        messageBox.destroy()
        self.displayProjectsAndSessions()
    
    
    def displayProjectsAndSessions(self):
        """
        Displays ongoing projects and active sessions in the view's right hand
        frame for projects and sessions.
        """        
        # refresh session and project frames:
        
        # destroy existing sessions and projects frames
        lf = self.view.lsFrame.lCanvas.lFrame        
        lf.pFrame.destroy()        
        lf.sFrame.destroy()
    
        # create new session and project frames        
        lf.pFrame = ProjectsFrame(parent=lf,controller=self)
        lf.sFrame = SessionsFrame(parent=lf,controller=self)
        lf.pFrame.pack(fill=tkinter.BOTH,expand=True)                        
        lf.sFrame.pack(fill=tkinter.BOTH,expand=True)        
        
        # display ongoing projects in view:
        
        # select ongoing projects from database
        self.model.cur.execute('''SELECT * FROM Projects WHERE status = ?;''',
                               ('Ongoing',))
        projects = self.model.cur.fetchall() # tuple of id, name, status
                
        # create and place new project labels:        
        parent = self.view.lsFrame.lCanvas.lFrame.pFrame
        col = 1

        for project in projects:
            idLabel = tkinter.Label(master=parent,
                                    text=project[0],anchor ="w")
            nameLabel = tkinter.Label(master=parent,
                                      text=project[1],anchor ="w")
            statusLabel = tkinter.Label(master=parent,
                                        text=project[2],anchor ="w")
            idLabel.grid(row=1,column=col)
            nameLabel.grid(row=2,column=col)
            statusLabel.grid(row=3,column=col)
            col += 1
        
        # display active sessions in view:
        
        # select active sessions from database
        self.model.cur.execute('''SELECT * FROM Sessions WHERE status = ?;''', 
                               ('Active',))
        sessions = self.model.cur.fetchall() 
        # tuple of id, projectid, duration, start, end, status                        
        
        # create and place new session labels:  
        
        parent = self.view.lsFrame.lCanvas.lFrame.sFrame
        col = 1
    
        for session in sessions:
            idLabel = tkinter.Label(master=parent,
                                    text=session[0],anchor ="w")
            projectidLabel = tkinter.Label(master=parent,
                                           text=session[1],anchor ="w")
            durationLabel = tkinter.Label(master=parent,
                                          text=session[2],anchor ="w")                      
                        
            # convert start and end from strings to datetimes.
            # ex: 2018-05-06 16:46:58.462379
            start = datetime.datetime.strptime(session[3], 
                                               '%Y-%m-%d %H:%M:%S.%f')
            if session[4] != None: 
                end = datetime.datetime.strptime(session[4], 
                                                 '%Y-%m-%d %H:%M:%S.%f')
            else:
                end = ''
            
            # convert start and end from datetimes to formatted strings:
            # ex: May 02, 2018\n11:43 AM              
            startLabel = tkinter.Label(master=parent,anchor ="w")
            startLabel["text"] = datetime.datetime.strftime(
                start, '%b %d, %Y\n%I:%M %p')              
            endLabel = tkinter.Label(master=parent,anchor ="w")
            if end != '':
                endLabel["text"] = datetime.datetime.strftime(
                    end, '%b %d, %Y\n%I:%M %p')
            else:
                endLabel["text"] = end
            
            # place labels
            statusLabel = tkinter.Label(master=parent,
                                        text=session[5],anchor ="w")            
            idLabel.grid(row=1,column=col)
            projectidLabel.grid(row=2,column=col)
            durationLabel.grid(row=3,column=col)
            startLabel.grid(row=4,column=col)
            endLabel.grid(row=5,column=col)
            statusLabel.grid(row=6,column=col)
            col += 1        
                

    def updateProjectStatus(self):               
        """
        Callback function for update project status button.
        """        
        # retrieve projects from database
        self.model.cur.execute('''SELECT * FROM Projects WHERE status = ?;''', 
                               ('Ongoing',))
        projects = self.model.cur.fetchall()
        
        # if no ongoing projects exist
        if len(projects) == 0:
            self.displayMessageBox(msg="No ongoing projects to select from." +
            "\nPlease create a project.")
            
        # if projects exist
        else:                
            rbDict = {'option': 'project',
                      'msg': 'Please select an ongoing project:',
                      'objects': projects,
                      'okCallback': self.updateProjectStatusOkCallback}
            # choose ongoing project from radio buttons
            self.radioButtonsWindow(rbDict)             
    
    
    def radioButtonsWindow(self, rbDict):
        """
        Creates a toplevel with radio buttons for selection among a list of
        ongoing projects or active sessions.
        """        
        # RADIOBUTTONS WITH ID OPTIONS
        
        # rbDict = {'option': 'session' or 'project', 'msg': string, 
        #           'objects': list of objects,
        #           'okCallback': callback function for ok button}
        
        messageBox = tkinter.Toplevel()
        # make the toplevel the active window
        messageBox.focus_set()
        mInfo = tkinter.Label(master=messageBox, text = rbDict['msg'], 
                              width=35, height=1)
        mEmptyLabel1 = tkinter.Label(master=messageBox)
    
        v = tkinter.IntVar()
        radioButtons = []
        for obj in rbDict['objects']:            
            rButton = tkinter.Radiobutton(master=messageBox)
            rButton['variable'] = v
            rButton['value'] = int(obj[0])
            if rbDict['option'] == 'session':
                rButton['text'] = str(obj[0])
            elif rbDict['option'] == 'project':
                rButton['text'] = str(obj[1])
            radioButtons.append(rButton)
        
        # set default choice
        v.set(rbDict['objects'][0][0])
        
        mOkButton = tkinter.Button(master=messageBox,text = 'Ok', width=15)
        mCancelButton = tkinter.Button(master=messageBox,
                                               text = 'Cancel', width=15)
        mOkButton['command'] = lambda: rbDict['okCallback'](messageBox, v)
        # so that pressing enter hits ok:
        messageBox.bind('<Return>', lambda event: \
                            rbDict['okCallback'](messageBox, v))        
        mCancelButton['command'] = messageBox.destroy
        mEmptyLabel2 = tkinter.Label(master=messageBox)
    
        mInfo.pack()
        mEmptyLabel1.pack()
        for rb in radioButtons: rb.pack()
        mOkButton.pack()
        mCancelButton.pack()
        mEmptyLabel2.pack() 
        
                        
    def updateProjectStatusOkCallback(self,messageBox,v):
        """
        Callback function for update project status toplevel's first ok button.
        """    
        projectid = v.get()
        messageBox.destroy()
        
        # new message box:
        # RADIOBUTTONS WITH STATUS OPTIONS
        messageBox = tkinter.Toplevel()
        mInfo = tkinter.Label(master=messageBox, 
                              text = 'Please select status for project ' + 
                              str(projectid) + '.\n\n' +
                              'IF MARKED AS FINISHED,\n' +
                              'PROJECT WILL DISAPPEAR\n'
                              'FROM VIEW, BUT WILL\n' + 
                              'APPEAR IN EXPORT.',
                              justify=tkinter.CENTER,width=35, height=6)
        mEmptyLabel1 = tkinter.Label(master=messageBox)
        
        # new radio buttons:
        v = tkinter.StringVar()
        v.set('Ongoing')
        rb1 = tkinter.Radiobutton(master=messageBox,variable=v,
                                  value='Ongoing',text='Ongoing')
        rb2 = tkinter.Radiobutton(master=messageBox,variable=v,
                                  value='Finished',text='Finished')
        
        # new ok and cancel buttons:
        mOkButton = tkinter.Button(master=messageBox,text = 'Ok', width=15)
        mCancelButton = tkinter.Button(master=messageBox,
                                       text = 'Cancel', width=15)
        mOkButton['command'] = lambda: \
            self.updateProjectStatusCommand(messageBox, v, projectid)
        # so that pressing enter hits ok:
        messageBox.bind('<Return>', lambda event: \
                        self.updateProjectStatusCommand(
                            messageBox, v, projectid))
        mCancelButton['command'] = messageBox.destroy
        mEmptyLabel2 = tkinter.Label(master=messageBox)
        
        # place widgets:
        mInfo.pack()
        mEmptyLabel1.pack()
        rb1.pack()
        rb2.pack()
        mOkButton.pack()
        mCancelButton.pack()
        mEmptyLabel2.pack()    
        
    
    def updateProjectStatusCommand(self,messageBox,v,projectid):
        """
        Callback function for update project status toplevel's second ok button.
        """    
        chosenStatus = v.get()
        self.model.updateProjectStatus({'id':projectid,'status':chosenStatus})
        messageBox.destroy()
        self.displayProjectsAndSessions()              
    
    
    def startSession(self):
        """
        Callback function for start session button.
        """        
        # retrieve projects from database
        self.model.cur.execute('''SELECT * FROM Projects WHERE status = ?;''', 
                               ('Ongoing',))
        projects = self.model.cur.fetchall()
        
        # if no ongoing projects exist
        if len(projects) == 0:
            self.displayMessageBox(msg='Sessions are associated with ongoing' +
                                   'projects.\nNo ongoing projects to select' +
                                   ' from.\nPlease create a project.')
        
        # if ongoing projects exist
        else:            
            rbDict = {'option': 'project',
                      'msg': 'Please select an ongoing project:',
                      'objects': projects,
                      'okCallback':self.startSessionOkCallback}
            # choose ongoing project from radio buttons
            self.radioButtonsWindow(rbDict)            
        
        
    def startSessionOkCallback(self,messageBox,v):
        """
        Callback function for start session toplevel's ok button.
        """    
        projectid = v.get()
        messageBox.destroy()
        
        # create new session
        self.model.startSession({'projectid':projectid})
        self.displayProjectsAndSessions()    
    
    
    def endSession(self):
        """
        Callback function for end session button.
        """        
        # retrive sessions from database
        self.model.cur.execute('''SELECT * FROM Sessions WHERE status = ?;''', 
                               ('Active',))
        sessions = self.model.cur.fetchall()
        
        # if no active sessions
        if len(sessions)==0:
            self.displayMessageBox(msg="No active sessions to select from." + 
            "\nPlease start a session.")
        
        # if active sessions exist:
        else:
            rbDict = {'option': 'session',
                      'msg': 'Please select an active session:',
                      'objects': sessions,
                      'okCallback':self.endSessionOkCallback}
            # choose active session from radio buttons
            self.radioButtonsWindow(rbDict)            
      
      
    def endSessionOkCallback(self, messageBox, v):
        """
        Callback function for end session toplevel's ok button.
        """        
        sessionId = v.get()
        messageBox.destroy()
        
        # end selected session
        self.model.endSession(sessionId)
        self.model.cur.execute('''SELECT duration FROM Sessions
                                  WHERE id = ?;''', (sessionId,))
        durationInMin = self.model.cur.fetchone()[0]
        self.displayMessageBox(msg='Your session lasted ' + 
                               str(durationInMin) + ' minutes.\nIt has been' +
                               ' recorded in the database.')                               
        self.displayProjectsAndSessions()
        
    
    def exportByDate(self):
        """
        Callback function for export work log by date button.
        """
        filename = self.model.export(option='ByDate')                            
        self.displayMessageBox('Export by Date complete!\n' +
                               'Please check the "Time_Tracker"\n' +
                               'folder for the MS Excel file:\n' +
                               filename)
        
        
    def exportByProject(self):
        """
        Callback function for export work log by project button.
        """        
        filename = self.model.export(option='ByProject')      
        self.displayMessageBox('Export by Project complete!\n' +
                               'Please check the "Time_Tracker"\n' +
                               'folder for the MS Excel file:\n' +
                               filename)        
        
    
    def exportAllData(self):
        """
        Callback function for export all data button.
        """        
        filename = self.model.export(option='AllData')       
        self.displayMessageBox('Export All Data complete!\n' +
                               'Please check the "Time_Tracker"\n' +
                               'folder for the MS Excel file:\n' +
                               filename)                
        
    
    def deleteAllData(self):
        """
        Callback function for delete all data button.
        """        
        messageBox = tkinter.Toplevel()
        
        mInfo = tkinter.Label(master=messageBox, text = 'Are you sure?',
                              justify=tkinter.CENTER,width=35, height=4)
        mEmptyLabel1 = tkinter.Label(master=messageBox)        
        mOkButton = tkinter.Button(master=messageBox,text = 'Ok', width=15)
        mCancelButton = tkinter.Button(master=messageBox,
                                           text = 'Cancel', width=15)
        mOkButton['command'] = lambda: self.deleteAllDataOkCallback(messageBox)
        # do not let pressing enter hit ok - user must click 'ok' or 'cancel'
        # (to prevent accidental deletions)
        mCancelButton['command'] = messageBox.destroy
        mEmptyLabel2 = tkinter.Label(master=messageBox)
        
        # place widgets:
        mInfo.pack()        
        mOkButton.pack()
        # place empty label betwen ok and cancel to prevent accidental clicks
        # on ok
        mEmptyLabel1.pack()       
        mCancelButton.pack()
        mEmptyLabel2.pack()           
        
    
    def deleteAllDataOkCallback(self,messageBox):                
        """
        Callback function for delete all data toplevel's ok button.
        """
        messageBox.destroy()
        
        # delete all data
        self.model.deleteAllData()        
        self.displayMessageBox(msg='All projects and sessions deleted.')                               
        self.displayProjectsAndSessions()        
            
        
    def displayMessageBox(self, msg):
        """
        Displays message in top level box.
        """
        messageBox = tkinter.Toplevel()
        # make the toplevel the active window
        messageBox.focus_set()        
        mlabel = tkinter.Label(master = messageBox, text = msg, 
                               width=35,height=5)
        mlabel.pack()
        mEmptyLabel1 = tkinter.Label(master=messageBox,width=35)
        mEmptyLabel1.pack()        
        button = tkinter.Button(master = messageBox, text = 'Ok',width =15)        
        button.pack()
        button['command'] = messageBox.destroy   
        mEmptyLabel2 = tkinter.Label(master=messageBox,width=35)
        mEmptyLabel2.pack()        
        # so that pressing enter hits ok:
        messageBox.bind('<Return>', lambda event: messageBox.destroy())        
        
        
if __name__ == "__main__":        
    c = Controller()