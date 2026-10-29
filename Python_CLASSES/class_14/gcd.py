# Optimal approach 
a =int(input())
b=int(input())

m=min(a,b)
if a==0 or b==0:
    print(max(a,b))
else:
    while m>0:
        x=a%m
        y=b%m

        if x==0 and y==0:
            print(m)
            break
        else:
            m=m-1


# Brute Force Approch