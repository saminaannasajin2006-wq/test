#polymorphism defines the ability to take different forms 
#eg- len()

x='hello world'
y=[12,'hi',-1,9.999]
z=('99.99','hell')
print (len(x))
print (len(y))
print (len(z))
G={'yak':3,'sparrow':4}
print (len(G))

class Animal:
    def speak(self):
        print("Animal speaks")
class  Dog(Animal):
    def speak(self):
       print("Dog barks") 
class cat(Animal):
    def speak(self):
        print("cat meows")

a=Animal()
a.speak() #output: Animal speaks

d =Dog()
d.speak()  #output: Dog barks
c=cat()
c.speak()    #output: Cat meows
