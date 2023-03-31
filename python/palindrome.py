# Write a program that takes a list of strings and returns a new list with only the strings that are palindromes

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

strings = input("Enter a list of strings, separated by spaces: ")
list = strings.split()
palindromes = []

for string in list:
    if palindrome(string):
        palindromes.append(string)
print(palindromes)
