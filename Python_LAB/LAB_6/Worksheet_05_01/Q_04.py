print({1, 2, 2, 3, 3, 3})
print([1, 2, 2, 3, 3, 3])

s = {1, 2, 3}
s.add(42)
s.add("hello")
s.add((10, 20))
s.add([1, 2])

print(hash((1, 2, 3))) # ________ (works)
print(hash((1, [2, 3]))) # ________ (what happens?)