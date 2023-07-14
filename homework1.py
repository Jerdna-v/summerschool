# zadaca 3
points=int(input("Points: "))
if not (points<0 or points>100):
    if 0<=points<=60: print("1")
    elif 61<=points<=70: print("2")
    elif 71 <= points <= 80:print("3")
    elif 81 <= points <= 90: print("4")
    elif 91 <= points <= 100:print("5")
#zadaca 9
year=int(input("Year: "))
if year%4==0 or (year%400==0 and year%100==0):print("leap year")
#zadaca 10
if int(input("Years: "))-18>=0: print("Can vote")
#zadaca 13
x, y, z = str(input("Angles: ")).split(" ")
if int(x)+int(y)+int(z)==180: print("Triangle")