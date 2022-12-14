try: 
    x = int(input("Enter Value of x: "))
    y = int(input("Enter Value of y: "))
except: 
    print("Invalid input")
else: 
    print("Valid Input")
finally: 
    print("Try Except Executed!")

while True:     
    op = input("Enter the operation: ")
    if op == "+": 
        print(x+y)
    elif op == "-": 
        print(x-y)
    elif op == "*":
        print(x*y)
    elif op == "/":
        print(x/y)
    elif op == "**":
        print(x**y)
    elif op == "%":
        print(x%y)
    else :
        print("Invalid operation! Breaking Off!!")
        break
