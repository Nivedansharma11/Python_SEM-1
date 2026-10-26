# n=int(input())
# i=0
# fn=0
# while i<=n:
#     fn=fn + (-(-1)**(i+1))*i


#     i=i+1

# print(fn)


n=int(input())

if n%2==0:
    x1=n//2
    print(*-1)
else:
    x2=n//2
    y=(x2*-1)+n
    print(y)

