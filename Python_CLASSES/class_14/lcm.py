a=int(input())
b=int(input())

m=max(a,b)
if a==0 or b==0:
    print(0)
else:

    while True:
        x=m%a
        y=m%b

        if x==0 and y==0:
            print(m)
            break
        else:
            m=m+1
