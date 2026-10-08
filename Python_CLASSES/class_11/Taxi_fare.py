d = float(input())

if d==0:
    print("No trip.")

elif 0<d<=2.0:
    print("Fare: Rs.50.00")

elif d>2:
    f=50 + 15*(d-2)
    print(f"Fare:Rs.{f:.2f}")