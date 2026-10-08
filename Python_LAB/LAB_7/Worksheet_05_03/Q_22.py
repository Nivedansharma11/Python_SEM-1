lst = [10, 20, 30]
lst.append(40)
lst.append(50)
print(lst)


lst = [10, 20, 30, 40, 50]
x = lst.pop()
print(x)
print(lst)
y = lst.pop(1)
print(y)
print(lst)


lst = [10, 20, 30, 20, 40]
lst.remove(20)
print(lst)
lst.remove(99)
