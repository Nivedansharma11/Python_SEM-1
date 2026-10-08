unit=int(input())

if 1<unit<=100:
    amount=unit*3.0
    print(f"Bill: Rs.{amount:.2f}")
elif 101<=unit<=200:
    unit=unit-100
    amount=unit*5.0 +300
    print(f"Bill: Rs.{amount:.2f}")
elif 201<=unit<=300:
    unit=unit-200
    amount=unit*7.0 +800
    print(f"Bill: Rs.{amount:.2f}")
elif unit>=301:
    unit=unit-300
    amount=unit*10.0+1500
    print(f"Bill: Rs.{amount:.2f}")