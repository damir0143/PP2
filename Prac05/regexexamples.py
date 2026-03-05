import re


# re.search() examples

print("SEARCH EXAMPLES")

#1 find first number
text = "My age is 20"
print(re.search(r"\d+", text).group())

#2 find word Python
text = "I learn Python programming"
print(re.search(r"Python", text).group())

#3 find first space
text = "Hello World"
print(re.search(r"\s", text))

#4 find uppercase letter
text = "hello World"
print(re.search(r"[A-Z]", text).group())

#5 find word starting with P
text = "Python is powerful"
print(re.search(r"P\w+", text).group())



# re.findall() examples

print("\nFINDALL EXAMPLES")

#1 find all numbers
text = "12 apples and 45 bananas"
print(re.findall(r"\d+", text))

#2 find all words
text = "Python is very fun"
print(re.findall(r"\w+", text))

#3 find all vowels
text = "hello world"
print(re.findall(r"[aeiou]", text))

#4 find all lowercase words
text = "Hello world python"
print(re.findall(r"[a-z]+", text))

#5 find words starting with capital letter
text = "Hello World Python"
print(re.findall(r"[A-Z][a-z]+", text))



# re.split() examples

print("\nSPLIT EXAMPLES")

#1 split by space
text = "Python is fun"
print(re.split(r"\s", text))

#2 split by comma
text = "apple,banana,orange"
print(re.split(r",", text))

#3 split by numbers
text = "apple1banana2orange3"
print(re.split(r"\d", text))

#4 split by dot
text = "www.google.com"
print(re.split(r"\.", text))

#5 split by multiple separators
text = "apple, banana orange"
print(re.split(r"[,\s]", text))


# re.sub() examples

print("\nSUB EXAMPLES")

#1 replace spaces with _
text = "hello world python"
print(re.sub(r"\s", "_", text))

#2 replace numbers with #
text = "My number is 12345"
print(re.sub(r"\d", "#", text))

#3 remove vowels
text = "hello world"
print(re.sub(r"[aeiou]", "", text))

#4 replace commas with :
text = "apple,banana,orange"
print(re.sub(r",", ":", text))

#5 replace multiple spaces
text = "hello    world"
print(re.sub(r"\s+", " ", text))