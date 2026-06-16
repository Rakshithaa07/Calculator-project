import os

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations_dict={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    number1=float(input("enter the first number:"))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        operator=input("pick an operator:")
        number2=float(input("enter the second number:"))
        calculation_function=operations_dict[operator]
        output=calculation_function(number1,number2)
        print(f" {number1} {operator} {number2} = {output}")
        should_continue=input(f"type 'yes' to continue with {output} or 'no' to start new calculation or 'x' to exit calculation:")
        if should_continue=='yes':
            number1=output
        elif should_continue=='no':
            continue_flag=False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print("exiting..thank you for using calculator...")

calculator()

    