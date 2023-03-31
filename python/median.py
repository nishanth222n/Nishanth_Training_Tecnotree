# Write a program that takes a list of numbers and returns the median value.

def median(numbers_list):
    sorted_numbers = sorted(numbers_list)
    length = len(sorted_numbers)
    middle_index = length // 2
    
    if length % 2 == 0:
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        return sorted_numbers[middle_index]

numbers = input("Enter a list of numbers, separated by commas: ").split(',')
numbers = [int(num) for num in numbers]
print("The median value of the list is:", median(numbers))
