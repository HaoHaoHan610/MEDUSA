class Myclass:
    x = 5

p1 = Myclass()

print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("john",24)

print(p1.age)
print(p1.name)

print(p1)