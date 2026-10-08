a = int(input())

if a>1000:
    a=a-(0.1*a)
    print(f"Discounted price: RS.{a:.2f}")