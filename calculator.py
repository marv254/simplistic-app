import sys
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponent(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y
  
def integer_divide(x, y):
  if y == 0:
      return "Error! Division by zero."
  return x // y  # Use integer division operator

if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("7. Integer Divide")  # New option for integer division
    
    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    
    elif choice == '5':
        print(f"{num1} ^ {num2} = {exponent(num1, num2)}")
    
    elif choice == '6':
        print(f"{num1} % {num2} = {modulus(num1, num2)}")
        
    elif choice == '7':
       print(f"{num1} // {num2} = {integer_divide(num1, num2)}")  # Updated for integer division
    
    else:
        print("Invalid input")
