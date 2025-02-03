'''
Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.

The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.
'''

def calculate(num1, operator, num2):
    num1Int = int(num1)
    num2Int = int(num2)

    match operator:
        case "+":
            return num1Int + num2Int
        case "-":
            return num1Int - num2Int
        case "*":
            return num1Int * num2Int
        case "/":
            if num2Int == 0:
                return "Error: Division by zero."
            return num1Int / num2Int
        case _:
            return "Invalid Operator"

print(f'Solution: {calculate("6", "*", "4")}')