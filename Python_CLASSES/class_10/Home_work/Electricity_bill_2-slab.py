unit=int(input())

if unit<=100:
    amount=unit*1.50
    print(f"Bill: Rs.{amount:.2f}")
elif unit>100:
    amount=unit*2.50
    print(f"Bill: Rs.{amount:.2f}")