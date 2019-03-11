# Make a function to determine if a number is odd or even

def odd_even(number):
    if number % 2 == 0:
        return "Even"
    if number % 2 != 0:
        return "Odd"

# Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    even_numbers = []    
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

# Given a list return the unique names in the list

def unique_names(list_of_names):
    unique_names = set(list_of_names)
    return unique_names

# Make a function that determines if a word is a palindrome

def palindrome_detector(string):
    """
    Input: string
    returns : True/False"""
    reverse = string[::-1]
    if reverse == string:
        return True
    else:
        return False

print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7]))
print(unique_names(['john', 'john', 'john']))
print(palindrome_detector('racecar'))
print(palindrome_detector('not'))
