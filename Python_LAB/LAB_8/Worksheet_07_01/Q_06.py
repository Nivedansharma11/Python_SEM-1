n,m,a=map(int,input().split())

a1=n*m
a2=a*a

x=a1//a2

k=a1-x*a2
f=k//a2

print(x+f)
