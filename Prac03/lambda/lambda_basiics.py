# lambda_basics.py

# 1. Add two numbers
add = lambda a, b: a + b
print(add(3, 4)) 


# 2. Square a number
square = lambda x: x * x
print(square(5))  


# 3. Check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(6))  


# 4. Get length of a string
string_length = lambda s: len(s)
print(string_length("hello"))  


# 5. Multiply all numbers in a list by 2 using map
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  
