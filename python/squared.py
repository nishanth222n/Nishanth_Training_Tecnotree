# Write a program that takes a list of numbers and returns a new list with the elements squared.

string = input("Enter a list of numbers, separated by commas: ")
List = [int(num) for num in string.split(',')]
SquaredNum = [num**2 for num in list]
print("The list with squared elements is:", SquaredNum )
