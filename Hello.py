def sum():
    print("Hello, World!") #this is a python class
    x,y,z="Orange", "Banana", "Cherry"
    print(z,y)
    a=2
    b=2.1
    print(type(a),type(b))
    print(len(x),len(z))
    x=input("Enter Your Name= ")
    print("Hello",x)
    x=int(input("Enter x= "))
    y=int(input("Enter y= "))
    print("Sum is", x+y)
    print("the sum of a+b =", a+b)
    print(ord('A'),ord('a'))
    name="Mikiyas"
    age=22
    GPA=1.133546
    print("my name is {:s} and I am {:d} Years old and my gpa is {:.2f}".format(name, age, GPA))
sum()
