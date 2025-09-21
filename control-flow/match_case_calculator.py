# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))
# operator = input("Choose the operation (+, -, *, /):")
# match operator:
#     case "+":
#         result = num1 + num2
#         print(f'The result is {result}')
#     case "-":
#         result = num1 - num2
#         print(f'The result = {result}')
#     case "*":
#         result = num1 * num2
#         print(f'The result is {result}')
#     case "/":
#         if num2 != 0:
#             result = num1 / num2
#             print(f'The result is {result}')
#         else:
#             print("Error: Can't divede by zero.")
#     case _:
#         print("Invalid operator. Please choose from +, -, *, /.")
              
# match_case_calculator.py

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ").strip()

        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}.")
            case "-":
                result = num1 - num2
                print(f"The result is {result}.")
            case "*":
                result = num1 * num2
                print(f"The result is {result}.")
            case "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}.")
            case _:
                print("Invalid operation. Please choose from +, -, *, /.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()



