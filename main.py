#THEJAS SHREE K 
#PYTHON PROJECT 
#CREATING A CALCULATOR

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a,b):
    return a%b


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Moudulus")


    
choice = input("Enter choice(1/2/3/4/5): ")
if choice in ('1', '2', '3', '4','5'):
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))

        if choice == '1':
            print(a, "+", b, "=", add(a, b))

        elif choice == '2':
            print(a,"+",b,"=",subtract(a,b))

        elif choice == '3':
            print(a, "*", b, "=", multiply(a,b))

        elif choice == '4':
            print(a, "/", b, "=", divide(a,b))
        
        elif choice =='5':
            print(a,"%",b,"=",modulus(a,b))
            
else:
        print("Invalid Input")
