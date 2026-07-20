# ==========================================================
#               PYTHON ASSIGNMENT 3 
#               Question 8
# Create a function named 'introduce' that takes two
# arguments:
# 1. name - positional argument
# 2. age - default argument (None)
# ==========================================================

def introduce(name, age=None):

    if age is not None:
        print(f"My name is {name}. I am {age} years old.")
    else:
        print(f"My name is {name}. My age is secret.")


introduce("John", 20)
introduce("John")



#               Question 9
# Create a function drop_minimum() that takes variable
# length arguments (*args) and returns a list after
# removing the minimum value.

def drop_minimum(*args):

    numbers = list(args)

    minimum = min(numbers)

    numbers.remove(minimum)

    return numbers


result = drop_minimum(5, -2, 8, 4, -5, 7, 10)

print("List after removing minimum value:", result)



#               Question 10
# Create a function find_max(a, b, c) that returns the
# largest of three numbers using the built-in max() function.
# Create another function main() to read three integers
# from the user and print the maximum value.

def find_max(a, b, c):
    return max(a, b, c)


def main():

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))

    maximum = find_max(x, y, z)

    print("Maximum Value:", maximum)


main()


#               Question 11
# Write a lambda function to add two numbers.
# 

add = lambda a, b: a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum:", result)



#               Question 12
# Write a lambda function that accepts a temperature in
# Celsius and converts it to Fahrenheit.
# Formula:
# Fahrenheit = Celsius * 9 / 5 + 32

convert = lambda celsius: (celsius * 9 / 5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = convert(celsius)

print("Temperature in Fahrenheit:", fahrenheit)



#               Question 13
# Write a lambda function that checks whether a number
# is even or odd.

check = lambda num: "Even" if num % 2 == 0 else "Odd"

number = int(input("Enter a number: "))

result = check(number)

print("The number is:", result)



#               Question 14
# Write a lambda function that returns the square of
# a given number.


square = lambda num: num ** 2

number = int(input("Enter a number: "))

result = square(number)

print("Square:", result)

#               Question 15
# Write a lambda function that returns True if a number
# is positive, otherwise returns False.

is_positive = lambda num: True if num > 0 else False

number = int(input("Enter a number: "))

result = is_positive(number)

print("Result:", result)



#               Question 16
# Write a lambda function that returns the length of
# a given string.


string_length = lambda text: len(text)

text = input("Enter a string: ")

result = string_length(text)

print("Length of the string:", result)



#               Question 17
# Write a lambda function that returns the largest
# number from a list.

largest = lambda numbers: max(numbers)

numbers = [12, 45, 7, 89, 23, 56]

result = largest(numbers)

print("List:", numbers)
print("Largest Number:", result)


