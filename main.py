import PySimpleGUI as sg
from Student import Student
from Student import Students

# Students object contains list of students
studentList = Students()

# basic layout of the window
layout = [[sg.Text("Add a student")],
          [sg.Text("First Name"), sg.InputText('', size=(10, 1), key="fn")],
          [sg.Text("Last Name"), sg.InputText('', size=(10, 1), key="ln")],
          [sg.Text("ID number"),sg.InputText('', size=(10, 1), key="id")],
          [sg.Text("GPA"),sg.InputText('', size=(10, 1), key="gpa")],
          [sg.Button("OK")]]
# display window
window = sg.Window("student", layout, margins=(100, 100))

while True:
    event, values = window.read()
    keys = ["fn", "ln", "id", "gpa"]
    if event == "OK":
        # create student object with input from user as fields
        student = Student(values["fn"], values["ln"], int(values["id"]), float(values["gpa"]))
        # add student to student list
        studentList.addStudent(student)
        # reset inputs window
        for i in range(len(keys)):
            window[keys[i]]("")
    elif event == sg.WIN_CLOSED:
        break

studentList.printList()
window.close()



