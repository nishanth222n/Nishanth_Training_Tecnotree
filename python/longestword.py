# Write a program that takes a list of words and returns the longest word in the list.

string = input("Enter a list of words, separated by commas: ")
list = string.split(',')

longestword = ''
for word in list:
    if len(word) > len(longestword):
        longestword = word

print("The longest word in the list is:", longestword)
