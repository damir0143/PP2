# 1. Iterators: iter() and next()
nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

print("-----")

# 2. Loop through an Iterator
nums2 = [10, 20, 30]
it2 = iter(nums2)
for n in it2:
    print(n)

print("-----")

# 3. Create an Iterator
class Count:
    def __init__(self, max):
        self.max = max
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

for n in Count(5):
    print(n)

print("-----")

# 4. Generators: yield keyword
def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

print("-----")

# 5. Creating Generator Functions
def squares(n):
    for i in range(n):
        yield i * i

for s in squares(5):
    print(s)

print("-----")

# 6. Generator Expressions
gen_expr = (x * x for x in range(5))
for value in gen_expr:
    print(value)