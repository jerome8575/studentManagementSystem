import PySimpleGUI as sg

# basic layout of the first window
layoutStudentInfo = [[sg.Text("Add a student")],
                     [sg.Text("First Name  "), sg.InputText('', size=(10, 1), key="fn")],
                     [sg.Text("Last Name   "), sg.InputText('', size=(10, 1), key="ln")],
                     [sg.Text("Grade       "), sg.InputText('', size=(10, 1), key="gr")],
                     [sg.Button("Add Classes")],
                     [sg.Button("OK"), sg.Button("Quit")]]
# this layout asks user to click on the class subject they want to add
layoutAddClassSubject = [[sg.Text("Select subject")],
                         [sg.Button("Math"), sg.Button("English"), sg.Button("Science")],
                         [sg.Button("Language"), sg.Button("History"), sg.Button("Electives")],
                         [sg.Button("Done")]]
# layouts for each class subject
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

# dictionary of active layouts
layouts = {"StudentInfo": layoutStudentInfo,
           "addClassSubjects": layoutAddClassSubject,
           "layMath": layoutMath,
           "layEng": layoutEnglish,
           "laySci": layoutScience,
           "layLang": layoutLanguage,
           "layHist": layoutHistory,
           "layElec": layoutElective}
