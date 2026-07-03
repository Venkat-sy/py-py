"""
Project 3: Basic Calculator
External Requirements: None
"""
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

while True:
    print("A. Addition  B. Subtraction  C. Multiplication  D. Division  E. Exit")
    choice = input("Enter your choice: ").upper()
    if choice == 'E': break
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if choice == 'A': print("Result:", add(a, b))
    elif choice == 'B': print("Result:", sub(a, b))
    elif choice == 'C': print("Result:", mul(a, b))
    elif choice == 'D': print("Result:", div(a, b))
