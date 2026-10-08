import weatherdesk
temp, rain = weatherdesk.weather_now("city")

city=input("Enter city")
price= float(input("Enter base price"))
orders = int(input("Enter orders last hour"))
riders = int(input("Enter no of riders online"))

print("Temperature:" ,temp ,"C")
print("Rain:", rain,"mm")

if temp-1.0 or rain==-1.0 :
    print("could not reach sky.... either service is down or city name is not supported")

pressure = orders / riders

print("Orders per rider:", pressure)
if rain > 0 and pressure > 3:
    surge=1.5
    print("Surge:",surge)
    print("Reason: raining AND every rider is buried in orders")
elif rain > 0:
    surge=1.3
    print("Surge:",surge)
    print("Reason: raining - fewer riders want to go out")
elif temp >= 33 and pressure > 3:
    surge=1.4
    print("Surge:",surge)
    print("Reason: heat wave AND riders are stretched thin")
elif temp >= 33:
    surge=1.2
    print("Surge:",surge)
    print("Reason: heat wave - nobody wants to step outside")
elif pressure > 4:
    surge=1.25
    print("Surge:",surge)
    print("Reason: dry and pleasant, but demand is running ahead of riders")
else:
    surge=1.0
    print("Surge:",surge)
    print("Reason: dry and pleasant, but demand is running ahead of riders")

Fprice = price * surge

print("Price:", Fprice) 