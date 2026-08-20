units = float(input("Enter your electricity units: "))

if units <= 0:
    print("Invalid units")

elif units <= 100:
    bill = units * 5
    print("Final bill:", bill)

elif units <= 200:
    bill = units * 7
    print("Final bill:", bill)

elif units <= 300:
    bill = units * 10
    print("Final bill:", bill)

else:
    bill = units * 12
    print("Final bill:", bill)
