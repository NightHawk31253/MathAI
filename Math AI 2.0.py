# This is area function

def area():
    def area_circle():
        r = (float(input("Enter the radius (in cm) = ")))
        return (22 / 7) * (r ** 2)

    def area_square():
        a = (float(input("Enter the side(in cm) = ")))
        return a ** 2

    def area_rectangle():
        l = (float(input("Enter the length (in cm) = ")))
        b = (float(input("Enter the bredth (in cm) = ")))
        return l * b

    def area_triangle():
        b = (float(input("Enter the bredth (in cm) = ")))
        h = (float(input("Enter the height (in cm) = ")))
        return (1 / 2) * b * h

    shape = (input("Which area do you wanna calculate? (circle/square/rectangle/triangle) = "))
    if shape == "circle":
        print("The area of circle is:")
        print(area_circle())
    elif shape == "square":
        print("The area of square is:")
        print(area_square())
    elif shape == "rectangle":
        print("The area of rectangle is:")
        print(area_rectangle())
    elif shape == "triangle":
        print("The area of triangle is:")
        print(area_triangle())
    else:
        print("Please enter the shape!")

# These are normal calculator functions

def add():
    a = float(input("Enter 1st value: "))
    b = float(input("Enter 2nd value: "))
    return (a+b)
def subtract():
    a = float(input("Enter 1st value: "))
    b = float(input("Enter 2nd value: "))
    return (a-b)
def multiply():
    a = float(input("Enter 1st value: "))
    b = float(input("Enter 2nd value: "))
    return (a*b)
def divide():
    a = float(input("Enter 1st value: "))
    b = float(input("Enter 2nd value: "))
    return (a/b)

# This is LCm and HCF function

def lcm_hcf():
    ques = input("What do you wanna calculate? = ")
    a = float(input("Enter no 1 = "))
    b = float(input("Enter no 2 = "))
    def lcm():
        HCF = float(input("Ener the HCF = "))
        LCM = (a*b)/HCF
        print("The LCM is:")
        return LCM
    def hcf():
        LCM = float(input("Ener the LCM = "))
        HCF = (a*b)/LCM
        print("The HCF is:")
        return HCF

    if (ques == "lcm"):
        print(lcm())
    elif (ques == "hcf"):
        print(hcf())
    else:
        print("Please tell me what you tryna calculate")

#this is bmi calculator function

def bmi():
    name = input("Enter name: ")
    height_m = float(input("enter height in meters: "))
    weight_kg = float(input("Enter weight in kilograms: "))

    bmi= weight_kg/(height_m**2)
    print ("bmi:")
    print(bmi)
    if bmi >=18 and bmi<=25:
        print(bmi)
        print(name + "is healthy")
    elif bmi < 18.1:
        print(bmi)
        print(name + " is underweight")
    else:
        print(bmi)
        print(name + " is overweight")
def fact():
    num = int(input("enter a number: "))
    fac = 1
    for i in range(1, num + 1):
        fac = fac * i
    print("factorial of ", num, " is ", fac)

def power():
    a = float(input("Enter the number: "))
    b = float(input("Enter it's power: "))
    return a**b

#This is percentage calculator

def percentage():
    a = float(input("enter total: "))
    b = float(input("enter the part: "))
    c = (b/a)*100
    return str(c) + "%"

#This is main function (maths AI)

def math_ai():
    cmd = input("What do you want to do?: ")
    if cmd == ("add"):
        print(add())
    elif cmd == ("sub"):
        print(subtract())
    elif cmd == ("multiply"):
        print(multiply())
    elif cmd == ("divide"):
        print(divide())
    elif cmd == ("lcm/hcf"):
        print(lcm_hcf())
    elif cmd == ("bmi"):
        print(bmi())
    elif cmd == ("area"):
        print(area())
    elif cmd == ("power"):
        print(power())
    elif cmd == ("factorial"):
        print(fact())
    elif cmd == ("percentage"):
        print(percentage())

math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()
math_ai()