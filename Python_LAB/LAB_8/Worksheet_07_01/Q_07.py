# b1 , b2 , b3 = map(int,input().split())

# a1=(b1+b2-b3)//2
# a2=(b1+b3-b2)//2
# a3=(b2+b3-b1)//2

# print(a1,a2,a3)

#CODEFORCE

x1,x2,x3,x4=map(int,input().split())
x=max(x1,x2,x3,x4)

if x==x1:
    a=x4-x3   
    b=x4-x2
    c=x4-x1

print(a,b,c)