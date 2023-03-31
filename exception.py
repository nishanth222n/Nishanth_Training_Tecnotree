try:
    
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = num1 / num2
        print("Result: ", result)
        
except ZeroDivisionError:
        print("Please enter a non-zero value for the denominator.")
