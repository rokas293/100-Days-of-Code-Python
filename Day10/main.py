from art import logo
import os

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Muliply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  run = True
 
  while run:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' to start a new calculation")
    continue_calc = input("Type y/n/new: ")
    if continue_calc == "y":
      run = True
      num1 = answer
    elif continue_calc == "n":
      run = False
      print("\nGoodbye.")
    elif continue_calc == "new":
       calculator()
       os.system('cls||clear')
    else:
      print("Invalid response.")
      run = False
      print("\nGoodbye.")

calculator()
