class student:
def init(self,name,age):
self.name=name
self.age=age

student1=student("ashwini",20)
student2=student("Sushant",34)
print(student1.name,student1.age)
print(student2.name,student2.age)
class student:
def init(self,name,age):
self.name=name
self.age=age
student1=student("ashwini",20)
student2=student("Sushant",34)
print(student1.name,student1.age)
print(student2.name,student2.age)
Output-
ashwini 20
Sushant 34
class student:
def__init__(self,name,age)
self.name=name
self.age=age
class student_marks:
def__init__(self,name,english,maths,science,sst):
self.name=name
self.english=english
self.maths=maths
self.science=science
self.sst=sst
def calculate_avg_marks(self):
total_marks=self.english+self.maths+self.science+self.sst
avg_marks=total_marks/4
student1=student_marks("Ashwini",20,12,14,15)
student2=student_marks("Ashu",10,18,16,9)
student3=student_marks("Sonu",16,14,20,11)
student4=student_marks("Sushant",20,20,20,20)

print(student1.calculate_avg_marks())
print(student2.calculate_avg_marks())
print(student3.calculate_avg_marks())
print(student4.calculate_avg_marks())
Output-
15.25
13.25
15.25
20.0
class Person():
def init(self,name):
print("Person Init called.")
self.name = name

class Student(Person):
def init(self, name):
Person.init(self, name)
print("Student Init called.")
self.name = name
def display(self):
print("Student",self.name)

class Employee(Person):
def init(self, name):
Person.init(self, name)
print("Employee Init called.")
self.name = name
def display(self):
print("Employee",self.name)

student = Student('Vicky')
student.display()
employee= Employee('Vikas')
employee.display()
class Person():
def init(self,name):
print("Person Init called.")
self.name = name

class Student(Person):
def init(self, name):
print("Student Init called.")
self.name = name
Person.init(self, name)

def display(self):
    print("Student",self.name)
student = Student('Vicky')
student.display()
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
class Cuboid:
def init(self, length, width,height):
self.length = length
self.width = width
self.height=height

def total_surface_area(self):
    return 2*(self.length * self.width +self.width*self.height+self.length*self.height)
class Cube:
def init(self, length):
self.length = length

def total_surface_area(self):
    return 6*self.length * self.length
cuboid=Cuboid(5,4,3)
print(cuboid.total_surface_area())
cube=Cube(5)
print(cube.total_surface_area())
Output-
94
150
