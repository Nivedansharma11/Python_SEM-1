# # Write your reference solution here
# ib=int(input())
# b=ib
# d=0

# while b>=0:
#     if d==3:
#         print(f"Final balance: {b}")
#         print(f"Declined withdrawals: {d}")
#         print("Card blocked")
#         break
#     elif d<3:
#         t=int(input())
#         if t==0:
#            break
#         else :
#                 if t>=b:
#                     b=b+t
#                 else:
#                     d=d+1

                    
# print(f"Final balance: {b}")
# print(f"Declined withdrawals: {d}")
# print("Session closed")


# # n=int(input())
# # k=int(input())

# # x=n+k

# # print(x)


# print(2 + 3)
# print("2" + "3")

# print("Hello" + ", " + "World!")
# print("ha" * 3)
# print("-" * 30)
# print(type("ha" * 3))

# print("hello" - "ello")
# print("hello" / 2)

# print("123" + 4)
# print("123" == 4)

# print(bin(13))
# print(bin(255))

# print(bin(42)) # base 2
# # print(oct(42)) # base 8
# # print(hex(42)) # base 16
# # print(int("101010", 2)) # binary string -> decimal
# # print(int("52", 8)) # octal string -> decimal
# # print(int("2a", 16)) # hex string -> decimal

# print(0b101010) # binary literal
# print(0o52) # octal literal
# print(0x2a) # hex literal

# print(13 & 10)

# print(bin(13))
# print(bin(10))
# print(bin(13 & 10))


# print(12 & 10)
# print(6 & 3)

# print(12 | 10)
# print(6 | 3)

# print(12 ^ 10)
# print(6 ^ 3)
# print(9 ^ 9)
# print(9 ^ 0)

# print(f"{1/3:.3f}")

# print(f"{0.1:.55f}")

# import sys
# print(sys.float_info.dig) # significant decimal digits of precision
# print(sys.float_info.max) # largest representable float


# print(f"{0.1:.20f}")
# print(f"{0.2:.20f}")
# print(f"{0.3:.20f}")
# print(f"{0.1 + 0.2:.20f}")


# n=list(map(int,input().split()))

# age = n[1:]

# t=0

# while t<6:
#     x=age[t]
#     t=t+1
#     print(x)


# n=int(input())
# s=0
# digit=list(map(int,str(n)))
# k=0

# while len(digit)>1 :
#     kn=sum(digit)
#     digit=list(map(int,str(k)))

#     s=s+1

# Write your reference solution here
# g=int(input())

# d=0
# m=0
# nm=0
# steps=[]
# while True:
#         ds=int(input())
#         if ds==-1:
#                 best=steps.sort()
#                 print(f"Days goal met: {m} out of {d}")
#                 print(f"Best day: Day {steps.index(max(steps))} with {max(steps)} steps")
#                 break

#         else:
#                 steps.append(ds)
#                 if ds<g:
#                         d=d+1
#                         print(f"Day {d}: {ds} steps - Goal missed")
#                 elif ds>=g:
#                         m=m+1
#                         d=d+1
#                         print(f"Day {d}: {ds} steps - Goal met")

