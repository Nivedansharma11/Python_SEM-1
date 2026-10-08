#Method 1
n = int(input())


if n%3==0 and n%5!=0:
    print("Fizz")

if n%5==0 and n%5!=0:
    print("Buzz")

if n%15==0:
    print("FizzBuzz")

#Method 2

n = int(input())

if n%3==0:
    print("Fizz", end="")

if n%5==0 :
    print("Buzz")