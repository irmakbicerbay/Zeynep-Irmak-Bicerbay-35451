print("irmak")
x = 5
y = "irmak"
z = 0.01
x = 10

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

if x > 5:
    print("x is greater than 5!")
  
carbrands = ["audi" , "bmw" , "mercedes"]
x, y, z, = carbrands
print(x)
print(type(x))
print(type(carbrands))
for x in carbrands:
  print(x)
student1 = {
  "name": "irmak",
  "surname": "bicerbay",
  "index_number": 35451,
  }
print(student1)

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def show(self):
        print(self.name, self.grades)

student1 = Student("Irmak", {"oop": 5, "math": 100})
student1.show()
  
