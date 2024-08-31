#simple python calculator

#for addition
def add(x,y):
    return x+y

#for substraction
def subtract(x,y):
    return x-y

#for multiplication
def multiply(x,y):
    return x*y

#for division
def divide(x,y):
    return x/y
def calculator():
        print("Simple Calculator")
        print("=================")
        print("Select operation:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.multiplication")
        print("4.Division")

# taking input from the user
while True:
    calculator()
    choice=input("Enter the choice(1,2,3,4):")

#check if the choice is one the four options
    if choice in['1','2','3','4']:
        num1=float(input("Enter the first number"))
        num2=float(input("Enter the second number:"))

            #printing 
    if choice=='1':
        print(f"Result:{num1}+{num2}={add(num1,num2)}")

    elif choice=='2':
        print(f"Result:{num1}-{num2}={subtract(num1,num2)}")

    elif choice=='3':
        print(f"Result:{num1}*{num2}={multiply(num1,num2)}")

    elif choice=='4':
        result=divide(num1,num2)

        print(f"Result:{num1}/{num2}={result}")




                       


























