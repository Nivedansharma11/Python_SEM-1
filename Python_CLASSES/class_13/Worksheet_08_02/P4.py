# n=int(input())

# i=1
# c=0
# while i<=n:
#     if n%i==0:
#         c=c+1
#     i=i+1
# if c==2:
#     print("Prime")
# else:
#     print("Mot Prime")


n= int(input())

i=2
c=0

while i<(n**0.5):
    if n%i==0:
        c=c+1
        break
    i=i+1

if c>0:
    print("Not Prime")
else:
    print("Prime")