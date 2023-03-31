
#giving input 
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

#filtering the even number and doubling the odd number
FilteredNumbers = [num*2 for num in numbers if num % 2 != 0]
print("Filtered and doubled numbers: ", FilteredNumbers)
