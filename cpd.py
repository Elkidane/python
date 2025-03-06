#comoundd interest calcuator

principle=0 #initial principal amount
rate=0  #interest rate
time=0 #number of time periods elapsed

while principle <=0:
   principle=float(input("Enter the principle amount : "))
if principle<=0:
    print("Principle cannot be less than or equal to zero!")

while rate <=0:
   rate=float(input("Enter the  Interest rate  : "))
if rate<=0:
    print("Interest rate  cannot be less than or equal to zero!")
while time <=0:
   time=float(input("Enter the time in years : "))
if time<=0:
    print("Time rate  cannot be less than or equal to zero!")

total=principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s: {total}")