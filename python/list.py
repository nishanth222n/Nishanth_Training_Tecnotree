# Write a program that takes two lists of numbers and returns a new list with the elements that appear in both lists.

list1_str = input("Enter the first list of numbers, separated by commas: ")
list1 = list(map(int, list1_str.split(',')))

list2_str = input("Enter the second list of numbers, separated by commas: ")
list2 = list(map(int, list2_str.split(',')))

CommonElements = []
for element in list1:
    if element in list2:
        CommonElements.append(element)
print("The common elements in both lists are:", CommonElements)
