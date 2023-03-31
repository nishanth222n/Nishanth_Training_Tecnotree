# Write a program that takes a string and returns the number of times each letter appears in the string.

string = input("Enter a string: ")
LetterCount = {}

for char in string:
    if char.isalpha():
        char = char.lower()
        if char in LetterCount:
            LetterCount[char] += 1
        else:
            LetterCount[char] = 1

print("Letter counts in the string:")
for letter, count in LetterCount.items():
    print(f"{letter}: {count}")
