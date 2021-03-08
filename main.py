import PySimpleGUI as sg

from Class import Class
from Student import Student, Students

from windows import createSubjectsWin, createStudentInfoWin, createAddClassSubjectsWin, createMainWindow

keys = ['fn', 'ln', 'gr']
studentList = Students()   # Students object, list of all students


# creates a class object and adds it to a class list
def createClass(classEvent, studentClasses):
    cl = Class(classEvent)
    studentClasses.append(cl)

# reads the window for selected class subject
def readSubjectWindow(subjectEvent, studentClasses):
    window = createSubjectsWin(subjectEvent)
    while True:
        event, values = window.read()
        if event is None or event == "Done":
            window.close()
            break
        else:
            cl = Class(event)
            studentClasses.append(cl)

def readAddClassesWindow(studentClasses):
    window = createAddClassSubjectsWin()
    while True:
        event2, values2 = window.read()
        if event2 == sg.WIN_CLOSED or event2 == "Done":
            window.close()
            break
        elif event2 != None:
            readSubjectWindow(event2, studentClasses)

def readStudentInfoWindow():
    studentClasses = []  # list of student's classes
    window = createStudentInfoWin()
    while True:
        event, values = window.Read()
        if event == "Add Classes":
            readAddClassesWindow(studentClasses)
        elif event == "OK":
            # create student object with input from user as fields
            student = Student(values["fn"], values["ln"], int(values["gr"]), studentClasses)
            studentList.addStudent(student)
            # reset student schedule
            studentClasses = []
            # clear fields
            for k in keys:
                window[k]("")
        elif event == sg.WIN_CLOSED or event == "Done":
            break
    window.close()

def main():
    mainWindow = createMainWindow()
    while True:
        event, values = mainWindow.read()
        if event == "as":
            readStudentInfoWindow()
        elif event is None or event == "Quit":
            mainWindow.close()
            break
    studentList.printList()

main()
