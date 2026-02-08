# basic_functions.py
#1
def add(a, b):
    """Return the sum of two numbers"""
    return a + b

#2
def subtract(a, b):
    """Return the difference of two numbers"""
    return a - b

#3
def multiply(a, b):
    """Return the product of two numbers"""
    return a * b

#4
def divide(a, b):
    """Return the division of two numbers (if possible)"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

#5
def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0


# Example usage
if __name__ == "__main__":
    print(add(3, 5))        
    print(subtract(10, 4)) 
    print(multiply(2, 6))  
    print(divide(8, 2))    
    print(is_even(7))      
