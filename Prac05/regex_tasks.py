import re

#1 Match 'a' followed by zero or more 'b'
print("#1")
pattern = r"ab*"
strings = ["a", "ab", "abb", "ac"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s, "-> match")


#2 Match 'a' followed by 2 to 3 'b'
print("\n#2")
pattern = r"ab{2,3}"
strings = ["ab", "abb", "abbb", "abbbb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s, "-> match")


#3 Find sequences of lowercase letters joined with underscore
print("\n#3")
text = "hello_world test_string Hello_World example_test"
pattern = r"[a-z]+_[a-z]+"

matches = re.findall(pattern, text)
print(matches)


#4 Find sequences of one uppercase letter followed by lowercase letters
print("\n#4")
text = "Hello world Python Programming"
pattern = r"[A-Z][a-z]+"

matches = re.findall(pattern, text)
print(matches)


#5 Match 'a' followed by anything ending in 'b'
print("\n#5")
pattern = r"a.*b"
strings = ["acb", "a123b", "ab", "aXYZb", "ac"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s, "-> match")


#6 Replace space, comma, or dot with colon
print("\n#6")
text = "Hello, world. Python is fun"
result = re.sub(r"[ ,.]", ":", text)

print(result)


#7 Convert snake_case to camelCase
print("\n#7")
text = "hello_world_example"

result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)
print(result)


#8 Split string at uppercase letters
print("\n#8")
text = "HelloWorldPython"

result = re.split(r"(?=[A-Z])", text)
print(result)


#9 Insert spaces between words starting with capital letters
print("\n#9")
text = "HelloWorldPython"

result = re.sub(r"([A-Z])", r" \1", text).strip()
print(result)


#10 Convert camelCase to snake_case
print("\n#10")
text = "helloWorldPython"

result = re.sub(r"([A-Z])", r"_\1", text).lower()
print(result)