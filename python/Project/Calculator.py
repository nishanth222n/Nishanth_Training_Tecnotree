# Calculator

while True:
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))
 operation = input("Enter operation :\n+\n-\n*\n/\n%\n\n")

 if operation == "+":
    result = num1 + num2
    print(result)

 elif operation == "-":
    result = num1 - num2
    print(result)

 elif operation == "*":
    result = num1 * num2
    print(result)

 elif operation == "/":
    if num2 == 0:
        print("Error: division by zero")
    else:
        result = num1 / num2
        print(result)

 elif operation == "%":
    result = num1 % num2
    print(result)     

 else:
    print("Invalid operation entered")
    break
