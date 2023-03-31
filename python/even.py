#  Write a program that takes a list of numbers and returns the sum of all even numbers in the list.

numbertostring = input("Enter a list of numbers, separated by commas: ")
numbertolist = [int(num) for num in numbertostring.split(',')]

even = 0
for num in numbertolist:
    if num % 2 == 0:
        even += num

print("The sum of all even numbers in the list is:", even)
