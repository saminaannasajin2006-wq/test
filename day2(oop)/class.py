num=20
print(type(num))

def my_function():
    print("Hello from a function")
    my_function()

class Myclass:
    x = 5
p1 =Myclass()
print(p1.x)

#base class

class vehicle:
    def vehicle_info(self):
        print("inside vehicle class")

#child class
class car(vehicle):
    def car_info(self):
        print('inside car class')
# create object of car

c1=car()
    # access vehicles info using car object
c1.vehicle_info()
c1.car_info()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        return f"hi i am {self.name} and i am {self.age} year old"
p1 = Person("Diuthendrh",19)
p2 = Person("Samina Anna",20)

print(p1)
print(p1.greet())
print(p2.name,p2.age) 