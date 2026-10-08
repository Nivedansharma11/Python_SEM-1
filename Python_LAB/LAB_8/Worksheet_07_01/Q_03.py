n , a , b = map(int,input().split())

if b>2*a:
        x=n*a
        print(x)
else:        
        x1 = (n//2)*b
        x2 = (n%2)*a

        print(x1+x2)