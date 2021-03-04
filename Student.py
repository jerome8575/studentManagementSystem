class Student:
    """Student class, initialize with first name, last name, id number, gpa
    function is print student whic prints all the fields"""

    firstName = ""
    lastName = ""
    grade = 0
    classSchedule = []

    def __init__(self, firstName, lastName, gr, cl):
        self.firstName = firstName
        self.lastName = lastName
        self.grade = gr
        self.classSchedule = cl

    def printStudent(self):
        print(self.firstName)
        print(self.lastName)
        print(self.grade)
        self.printClassSchedule()

    def printClassSchedule(self):
        for c in self.classSchedule:
            c.printClass()

    def addClass(self, c):
        self.classSchedule.append(c)


class Students:
    """keeps a list of students in alphabetical order by last name
    functions are printList(), addStudent(Student object)"""

    studentsList = []

    def __init__(self):
        self.studentsList = []

    def printList(self):
        for i in range(len(self.studentsList)):
            self.studentsList[i].printStudent()
            print("")
            print("----------------")

    def bisect(self, lastName):
        low = 0
        high = len(self.studentsList)
        while low < high:
            mid = (low + high) // 2
            if self.studentsList[mid].lastName < lastName:
                low = mid + 1
            else:
                high = mid
        return low

    def addStudent(self, s):
        self.studentsList.insert(self.bisect(s.lastName), s)
