"""
File myDB.
Defines class MyDB.
"""

# Originally by: 
# Cem H. Yesilyurt
# 5/9/18
# Python 3.6.2

import sqlite3
import datetime
import csv

class MyDB:
    
    def __init__(self):
                
        # connect and initialize cursor
        self.conn = sqlite3.connect('myWorkDB.sqlite')            
        self.cur = self.conn.cursor()
        
        # create Projects table
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS Projects (
                id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name   TEXT,
                status TEXT                     
                );
            ''')                
        
        # create Sessions table
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS Sessions (
                id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                projectid   INTEGER NOT NULL,
                duration    INTEGER,
                start       TEXT NOT NULL,
                end         TEXT,
                status      TEXT NOT NULL
                );
            ''')
        
        # save changes
        self.conn.commit()
        
        
    def createProject(self, projectDict):
        """
        Creates a project entry in the Projects table.
        """
        self.cur.execute('''INSERT INTO Projects (name, status) 
                            VALUES (?, ?);''',
                         (projectDict['name'], projectDict['status']))        
        # save changes
        self.conn.commit()        
    
    def updateProjectStatus(self, projectDict):
        """
        Updates a project's status in the Projects table.
        """
        self.cur.execute('''UPDATE Projects SET status = ? WHERE id = ?;''',
                         (projectDict['status'],projectDict['id']))        
        # save changes
        self.conn.commit()        
        
        
    def startSession(self, sessionDict):
        """
        Creates a session entry in the Session table.
        """
        # get start time as datetime
        start = datetime.datetime.now()              
        
        # ex: 2018-05-06 16:45:16.845938
        
        # insert new session into datble, using start datetime
        self.cur.execute('''INSERT INTO Sessions (projectid, start, status)
                            VALUES (?, ?, ?);''',
                             (sessionDict['projectid'], str(start), 'Active'))        
        # save changes
        self.conn.commit()
        
        
    def endSession(self, sessionId):
        """
        Completes a session entry in the Sessions table.
        """        
        # retrieve start time
        self.cur.execute('''SELECT start FROM Sessions WHERE id = ?;''',
                         (sessionId,))
        start = self.cur.fetchone()[0]
        # format of start is: YYYY-MM-DD HH:MM:SS.microseconds
        # ex: 2018-05-06 16:45:16.845938                                      
        # but since this came from dbase TEXT column, this is a string, so       
        # convert it to datetime        
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')        
        
        # get end time as datetime
        end = datetime.datetime.now()            
        # ex: 2018-05-06 16:46:58.462379
        
        # compute difference between the two datetimes
        # get time-delta object
        # format: '# days, #:#:#.#'  (days, hrs, min, sec, decimal sec)
        delta = end - start
        
        # compute duration in minutes
        durationInMins = 0
        
        # if delta is more than one day
        if 'day' in str(delta):         
            pieces = str(delta).split(' ')
            days = int(pieces[0])
            hrsmins = pieces[2]
            timepieces = hrsmins.split(':')
            hrs = int(timepieces[0])
            mins = int(timepieces[1])
            secs = float(timepieces[2])
            if secs >= 30: mins+=1
            durationInMins = days*24*60 + hrs*60 + mins
        else:
            days = 0
            timepieces = str(delta).split(':')
            hrs = int(timepieces[0])
            mins = int(timepieces[1])
            secs = float(timepieces[2])
            if secs >= 30: mins+=1    
            durationInMins = hrs*60 + mins                        
                
        self.cur.execute('''UPDATE Sessions SET end = ?, duration = ?, 
                            status = ? WHERE id = ?;''',
                             (str(end), durationInMins, 'Complete', sessionId))        
        # save changes
        self.conn.commit()
        
        
    def export(self, option):
        
        # select records from database
        # use join statement        
        
        if option == 'ByDate':
            self.cur.execute('''SELECT s.id AS 'Session ID', 
                                       s.start AS 'Start',
                                       s.end AS 'End', 
                                       s.duration AS 'Duration (min)',
                                       s.status AS 'Session Status', 
                                       p.name AS 'Project Name', 
                                       p.status AS 'Project Status'
                                FROM Projects p, Sessions s 
                                WHERE s.projectid = p.id 
                                ORDER BY s.start ASC;''') 
            
        elif option == 'ByProject':
            self.cur.execute('''SELECT p.id AS 'Project ID', 
                                       p.name AS 'Project Name',
                                       p.status AS 'Project Status', 
                                       s.start AS 'Start', 
                                       s.end AS 'End', 
                                       s.duration AS 'Duration (min)', 
                                       s.status AS 'Session Status'
                                FROM Projects p, Sessions s 
                                WHERE s.projectid = p.id 
                                ORDER BY p.id, s.start ASC;''')    
            
        elif option == 'AllData':
            self.cur.execute('''SELECT s.id AS 'Session ID',
                                       s.start AS 'Start',
                                       s.end AS 'End',
                                       s.duration AS 'Duration (min)', 
                                       s.status AS 'Session Status',
                                       p.id AS 'Project ID',
                                       p.name AS 'Project Name',
                                       p.status AS 'Projects Status' 
                                FROM Projects p, Sessions s 
                                WHERE s.projectid = p.id 
                                ORDER BY p.id, s.start ASC;''')
            
                    
        colNames = list(map(lambda x: x[0], self.cur.description))
        #print(colNames)
        
        data = self.cur.fetchall()
        #print(data)
        data.insert(0,colNames)
        #print(data)
        
        filename = datetime.datetime.strftime(
                datetime.datetime.now(), 'MyWorkData_'+option+'_%Y_%b_%d.csv')
        
        try:
            f = open(file=filename,mode='w',newline='')
            writer = csv.writer(f)
            writer.writerows(data)
            #print('writing complete')            
            f.close()
            
        except:
            
            if option == 'ByDate': 
                print('Problem exporting data by date')
            elif option == 'ByProject': 
                print('Problem exporting data by project')
            elif option == 'AllData':
                print('Problem exporting all data')
                
        return filename
    
    
    def deleteAllData(self):
        
        self.cur.execute('''DELETE FROM Projects;''')
        self.cur.execute('''DELETE FROM Sessions;''')
        self.conn.commit()