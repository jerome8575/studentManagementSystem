import PySimpleGUI as sg

from Class import Class
from Student import Student, Students

from windows import windows


# creates a class object and adds it to a class list
def createClass(classEvent, studentClasses):
    cl = Class(classEvent)
    studentClasses.append(cl)

# checks if a window was closed or exited
def checkClosedWindow(event):
    if event == sg.WIN_CLOSED or event == "Done":
        return True

# reads the window for selected class subject
def readSubjectWindow(subjectEvent, studentClasses):
    while True:
        event, values = windows[subjectEvent].read()
        if event is None or event == "Done":
            windows[subjectEvent].close()
            break
        else:
            cl = Class(event)
            studentClasses.append(cl)

def readAddClassesWindow():
    while True:
        event2, values2 = windows["AddClassSubject"].read()
        print(event2)
        if event2 == sg.WIN_CLOSED or event2 == "Done":
            windows["AddClassSubject"].close()
            break
        elif event2 != None:
            readSubjectWindow(event2, studentClasses)


studentList = Students()   # Students object, list of all students
studentClasses = []  # list of student's classes

while True:
    event, values = windows["StudentInfo"].read()
    if event == "Add Classes":
        readAddClassesWindow()
    elif event == "OK":
        # create student object with input from user as fields
        student = Student(values["fn"], values["ln"], int(values["gr"]), studentClasses)
        studentList.addStudent(student)
    elif event == sg.WIN_CLOSED or event == "Quit":
        break

studentList.printList()
windows["StudentInfo"].close()
