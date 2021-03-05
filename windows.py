import PySimpleGUI as sg
from layout import layouts

# create the windows
windowStudentInfo = sg.Window("student", layouts["StudentInfo"], margins=(50, 50))
windowAddClassSubject = sg.Window("classes", layouts["addClassSubjects"], margins=(30, 30))
windowMath = sg.Window("math", layouts["layMath"])
windowEnglish = sg.Window("english", layouts["layEng"])
windowScience = sg.Window("science", layouts["laySci"])
windowLanguage = sg.Window("language", layouts["layLang"])
windowHistory = sg.Window("history", layouts["layHist"])
windowElective = sg.Window("elective", layouts["layElec"])

# dictionary of windows

windows = {"StudentInfo": windowStudentInfo,
           "AddClassSubject": windowAddClassSubject,
           "Math": windowMath,
           "English": windowEnglish,
           "Science": windowScience,
           "Language": windowLanguage,
           "History": windowHistory,
           "Elective": windowElective}
