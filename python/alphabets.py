# Write a program that takes a list of strings and returns a new list with all the strings sorted in alphabetical order.

string = input("Enter a list of strings, separated by commas: ")
list = string.split(',')
sortedstring = sorted(list)
print("The sorted list of strings is:", sortedstring)
