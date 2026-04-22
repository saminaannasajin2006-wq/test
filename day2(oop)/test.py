import math
class area():
    def calc(self):
        pass
class rectangle(area):
    def calc(self,length,breadth):
        return length*breadth
class circle(area):
    def calc(self,radius):
        return math.pi*(radius**2)
class square(area):
    def calc(self,length):
        return length**2
    
r=rectangle()
print(r.calc(4,6))

c=circle()
print(c.calc(3))

s=square()
print(s.calc(4))
    