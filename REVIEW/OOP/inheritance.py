class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)


class Grade:
    def __init__(self,grade = 0,practice = 0):
        self.grade = grade
        self.practice = practice

class Student(Person,Grade):
    def __init__(self, fname, lname,grade = 0,practice = 0):
        Person.__init__(self,fname, lname)
        Grade.__init__(self,grade,practice)

s1 = Student("Hao","Le",5,8)

print(s1.grade)