n=int(input())
a=int(input())
b=int(input())

i=1
while i<=n:
    if i%a==0 or i%b==0:
        print(i)
        i=i+1
    else:
        i=i+1
    