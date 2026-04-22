#eg:
from abc import ABC,abstractclassmethod
class car(ABC):
    @abstractclassmethod
    def mileage(self):
        pass
class defender(car):
    def mileage(self):
        print('the mileage is 7kmpl')

class diago(car):
    def mileage(self):
        print("the mileage is 13kmpl")

class BMW(car):
    def mileage(self):
        print("the mileage is 13kmpl")
    
d=defender()
d.mileage()
i=diago()
i.mileage()
p=BMW()
p.mileage()
        