import PySimpleGUI as sg


classes = {"Math" : "MAT101",
           "English" : "ENG101",
           "Science" : "SCI101",
           "Language": "LANG101",
           "History" : "HIST101",
           "Electives": "ELEC101"}

def createStudentInfoLayout():
    studentInfo = [[sg.Text("Add a student")],
                         [sg.Text("First Name  "), sg.InputText('', size=(10, 1), key="fn")],
                         [sg.Text("Last Name   "), sg.InputText('', size=(10, 1), key="ln")],
                         [sg.Text("Grade       "), sg.InputText('', size=(10, 1), key="gr")],
                         [sg.Button("Add Classes")],
                         [sg.Button("OK"), sg.Button("Quit")]]
    return studentInfo

def createAddClassSubjectsLayout():
    addClassSubjects = [[sg.Text("Select subject")],
                             [sg.Button("Math"), sg.Button("English"), sg.Button("Science")],
                             [sg.Button("Language"), sg.Button("History"), sg.Button("Electives")],
                             [sg.Button("Done")]]
    return addClassSubjects

def createSubjectsLayout(subjectName):
    layout = [[sg.Text(subjectName)],
                      [sg.Button(classes[subjectName])],
                      [sg.Button("Done")]]
    return layout