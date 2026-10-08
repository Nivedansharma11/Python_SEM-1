s = "Hello World"
print(s.upper())
print(s.lower())
print(s)

raw = " hello world "
print(raw.strip())
print(raw.lstrip())
print(raw.rstrip())
print(len(raw), len(raw.strip()))

print(" hello world ".split())

print("alice,bob,charlie".split(","))

line = "A101,Laptop,5,29999.99"
parts = line.split(",")
print(parts[0])
print(parts[2])
print(type(parts[2]))

line = "A101,Laptop,5,29999.99"
parts = line.split(",")
print(parts[0])
print(parts[2])
print(type(parts[2]))

raw = " HELLO, world! "
print(raw.strip().lower())