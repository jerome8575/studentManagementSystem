import PySimpleGUI as sg
from layout import createStudentInfoLayout, createSubjectsLayout, createAddClassSubjectsLayout


def createStudentInfoWin():
    return sg.Window("student", createStudentInfoLayout(), margins=(10, 10))
def createAddClassSubjectsWin():
    return sg.Window("classes", createAddClassSubjectsLayout(), margins=(30, 30))
def createSubjectsWin(subjectName):
    return sg.Window(subjectName, createSubjectsLayout(subjectName), margins=(30, 30))
