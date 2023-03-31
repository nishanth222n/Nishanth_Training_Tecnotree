# Write a program that takes a list of numbers and returns a new list with only the prime numbers.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

string = input("Enter a list of numbers, separated by commas: ")
list = [int(num) for num in string.split(',')]
PrimeNum = [num for num in list if is_prime(num)]

# print the result
print("The prime numbers in the list are:", PrimeNum)
