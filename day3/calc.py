print("1.add 2.subtract 3.divide 4.multiply")
choice = int(input("enter choice: "))

print("entere values")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if choice == 1:
    print("sum = ",a+b)
elif choice == 2:
    print("difference =", a - b)
elif choice == 3:
    print("quotient =", a / b)
elif choice == 4:
    print("product =", a * b)
else:
    print("enter a valid choice")