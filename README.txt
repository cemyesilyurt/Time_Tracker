README.txt

Program name: Time Tracker
Author: Cem Hasan Yesilyurt
Date: 05/09/18
Development Environment: Python 3.6.2

Video demo: https://www.youtube.com/watch?v=viuPs4WgLG0

Description:  This program tracks the user's time spent on a multitude of projects.  This is useful for consultants who want to track how much time they are spending on each project, in order to ensure accurate billing of their clients.  Or, it can be used by anyone who just wants to track how much time they spend on things while they are on the computer.  

Program usage is as follows: The user can create a project and start a session for that project.  The program will continue to run in the background as the user performs their tasks.  When the user is done working for that session, he/she simply clicks the "end session" button.  This will record the end time and session duration in the database.  Multiple sessions can go on at the same time for different projects.  Multiple sessions can even go on for the same project.  This does not cause any problem with the program.  

When the user has completed a project, he/she may update the project's status from "ongoing" to "finished".  Marking a project as "finished" will take it off of the screen, but the program will keep that project and its records in the database. Similarly, only active sessions are displayed on the screen.  When a session is ended, its status is updated to "complete" and it is taken off of the screen, but the session details are recorded in the database.  

The contents of the database can be viewed at any time by exporting the data to a csv file.  The data can be sorted by date or by project.  For those who would like access to all the data, an "all data" export option has been included.  If at any time the user would like to wipe the database clean and start over from scratch, a "delete all data" option has also been included.  Measures have been taken to avoid accidental deletions: the program will ask users if they are sure before deleting any data.


The quit button will close the application, however it will not end the active sessions.  Active sessions must be ended one by one by the user.  The program has been written this way for the following reason.  If the user has to perform a task that will be taxing for the computer, he/she has the option of starting a session, closing the Time Tracker program, performing the task, then opening the Time Tracker program again to end the session.  The way the program is written, active sessions do not put any load on the system: an active session is merely marked as active in the database.  There is no background process running unless the Time Tracker program is open.

This program was written in Python using the sqlite3, tkinter, csv, and datetime modules.  It follows a model-view-controller architecture and is free for any to use.  If any choose to modify it, the author requests that the comment "Original Contributor: Cem H. Yesilyurt" be kept the same in all the scripts.  Thank you for your understanding in this matter - I hope the program will be beneficial.

Regards,
Cem H. Yesilyurt


Program Files:
- controller.py (main)
- myDB.py (model)
- topFrame.py (view) - contains buttonsFrame and listsScrollbarFrame
- buttonsFrame.py - contains buttons
- listsScrollbarFrame.py - contains scrollbar and listsCanvas
- listsCanvas.py - contains listsFrame
- listsFrame.py - containts projectsFrame and sessionsFrame
- projectsFrame.py
- sessionsFrame.py

Program Folders:
- TimeTracker_CHY is a directory that contains the executable file "TimeTracker_CHY".

Usage:
- download the zip file "TimeTracker_CHY" and run the application file (exe) "TimeTracker_CY".  You can place the folder anywhere on your computer and create a shortcut link to the application.