def add_one(a, b):
    x = a + 1
    y = b + 1
    def mult(a, b):
        return "Nested function", a * b
    return "First function", mult(x, y)

a = 1
b = 2
x = 5
y = 6

print("Print function", add_one(x, y))
print("Print function", add_one(a, b))
print("Print function", add_one(x, a))
print("Print function", add_one(y, b))
