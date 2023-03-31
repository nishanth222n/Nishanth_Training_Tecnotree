# Write a program that takes a string and returns a new string with all the vowels removed.

string = input("Enter a string: ")
newstring = ""
for char in string:
    if char not in "aeiouAEIOU":
        newstring += char

print("The new string with all the vowels removed is:", newstring)
