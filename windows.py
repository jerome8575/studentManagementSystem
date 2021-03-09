import PySimpleGUI as sg
from layout import createStudentInfoLayout, createSubjectsLayout, createAddClassSubjectsLayout, createMainLayout


def createStudentInfoWin():
    return sg.Window("student", createStudentInfoLayout(), margins=(10, 10), size=(500, 300))
def createAddClassSubjectsWin():
    return sg.Window("classes", createAddClassSubjectsLayout(), margins=(30, 30), size=(500, 300))
def createSubjectsWin(subjectName):
    return sg.Window(subjectName, createSubjectsLayout(subjectName), margins=(30, 30), size=(500, 300))
def createMainWindow():
    return sg.Window("Student management system", createMainLayout(), margins=(30, 30), size=(500, 300))
