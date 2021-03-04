import PySimpleGUI as sg
from Student import Student, Students
from Class import Class

# creates a list of all students
studentList = Students()

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
    if subjectEvent == "Math":
        event, values = windowMath.read()
        if checkClosedWindow(event):
            windowMath.close()
        elif event == "MAT101":
            createClass(event, studentClasses)
    elif subjectEvent == "English":
        event, values = windowEnglish.read()
        if checkClosedWindow(event):
            windowEnglish.close()
        elif event != None:
            createClass(event, studentClasses)
    elif subjectEvent == "Science":
        event, values = windowScience.read()
        if checkClosedWindow(event):
            windowScience.close()
        elif event != None:
            createClass(event, studentClasses)
    elif subjectEvent == "Language":
        event, values = windowLanguage.read()
        if checkClosedWindow(event):
            windowLanguage.close()
        elif event != None:
            createClass(event, studentClasses)
    elif subjectEvent == "History":
        event, values = windowHistory.read()
        if checkClosedWindow(event):
            windowHistory.close()
        elif event != None:
            createClass(event, studentClasses)
    elif subjectEvent == "Electives":
        event, values =windowElective.read()
        if checkClosedWindow(event):
            windowElective.close()
        elif event != None:
            createClass(event, studentClasses)


# basic layout of the first window
layoutStudentInfo = [[sg.Text("Add a student")],
          [sg.Text("First Name  "), sg.InputText('', size=(10, 1), key="fn")],
          [sg.Text("Last Name   "), sg.InputText('', size=(10, 1), key="ln")],
          [sg.Text("Grade       "), sg.InputText('', size=(10,1), key="gr")],
          [sg.Button("Add Classes")],
          [sg.Button("OK"), sg.Button("Quit")]]
# this window asks user to click on the class subject they want to add
layoutAddClassSubject = [[sg.Text("Select subject")],
                    [sg.Button("Math"), sg.Button("English"), sg.Button("Science")],
                    [sg.Button("Language"), sg.Button("History"), sg.Button("Electives")],
                    [sg.Button("Done")]]
# windows for each class subject
layoutMath = [[sg.Text("MATH")],
              [sg.Button("MAT101")],
              [sg.Button("Done")]]
layoutEnglish = [[sg.Text("ENGLISH")],
              [sg.Button("ENG101")],
              [sg.Button("Done")]]
layoutScience = [[sg.Text("SCIENCE")],
              [sg.Button("SCI101")],
              [sg.Button("Done")]]
layoutLanguage = [[sg.Text("LANGUAGE")],
              [sg.Button("LANG101")],
              [sg.Button("Done")]]
layoutHistory = [[sg.Text("HISTORY")],
              [sg.Button("HIS101")],
              [sg.Button("Done")]]
layoutElective = [[sg.Text("ELECTIVE")],
              [sg.Button("ELECT101")],
              [sg.Button("Done")]]

# create windows
windowStudentInfo = sg.Window("student", layoutStudentInfo, margins=(50, 50))
windowAddClassSubject = sg.Window("classes", layoutAddClassSubject, margins=(30,30))
windowMath = sg.Window("math", layoutMath)
windowEnglish = sg.Window("english", layoutEnglish)
windowScience = sg.Window("science", layoutScience)
windowLanguage = sg.Window("language", layoutLanguage)
windowHistory = sg.Window("history", layoutHistory)
windowElective = sg.Window("elective", layoutElective)

# Controls the window interactions
keys = ["fn", "ln", "gr"]
studentClasses = []
while True:

    event, values = windowStudentInfo.read()
    if event == "Add Classes":
        while True:
            event2, values2 = windowAddClassSubject.read()
            if event2 == sg.WIN_CLOSED or event2 == "Done":
                windowAddClassSubject.close()
                break
            elif event2 != None:
                readSubjectWindow(event2, studentClasses)

    elif event == "OK":
        # create student object with input from user as fields
        student = Student(values["fn"], values["ln"], int(values["gr"]), studentClasses)
        print(studentClasses)
        studentList.addStudent(student)

    elif event == sg.WIN_CLOSED or event == "Quit":
        break

studentList.printList()
windowStudentInfo.close()
