class person:
    def __init__(self,name,age):
        self.name = name
        self.__age= age

p1=person("Akshay",20)
print(p1.name,"\n",p1._person__age)
      

        