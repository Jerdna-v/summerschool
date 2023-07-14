# x, y = str(input("Input two numbers")).split(" ")
# x=int(x)
# y=int(y)
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x**y)
# print(x//y)

# name, year = str(input("Ime i godina: ")).split(" ")
# print(f"Zdravo {name}, ti vo 2023 kje imash {2023-int(year)}")

# print(True if int(input("Number "))%2==0 else False)

# x, y, sign = str(input("Input two numbers and a sign ")).split(" ")
# x=int(x)
# y=int(y)
# if sign=="+":
#     print(x+y)
# elif sign=="-":
#     print(x-y)
# elif sign == "*":
#     print(x*y)
# elif sign=="/":
#     print(x/y)
# elif sign=="**":
#     print(x**y)
# elif sign=="//":
#     print(x//y)

# x = int(input("number "))
# if x>= 1000:
#     print("preterano poz")
# elif x<999 and x>100:
#     print("mnogu poz")
# elif x<=100 and x>0:
#     print("poz")
# elif x==0:
#     print("nula")
# elif x<0 and x>-100:
#     print("neg")
# elif x<=-100 and x>-999:
#     print("mnogu neg")
# elif x<=-1000:
#     print("preterano neg")
#

# name = str(input("Vnesi ime"))
# ocenki = str(input("Vnesi 5 ocenki")).split()
# ocenki = [int(i) for i in ocenki]
# zbir=ocenki[0]+ocenki[1]+ocenki[2]+ocenki[3]+ocenki[4]
# for i in range(len(ocenki)): print(f"predmet {i+1} = {ocenki[i]}")
# print(f"Zbir = {zbir}")
# print(f"Prosecna = {zbir/5}")



# loop version
# for l in letter:
#     if l == '1': temp+= "eden"
#     if l == '2': temp += "dva"
#     if l == '3': temp += "tri"
#     if l == '4': temp += "cetiri"
#     if l == '5': temp += "pet"
#     if l == '6': temp += "sest"
#     if l == '7': temp += "sedum"
#     if l == '8': temp += "osum"
#     if l == '9': temp += "devet"
#     temp+=" "
# letter = str(input("number "))
# temp = ""
# # first digit
# if letter[0] == '1': temp+= "eden"
# if letter[0] == '2': temp += "dva"
# if letter[0] == '3': temp += "tri"
# if letter[0] == '4': temp += "cetiri"
# if letter[0] == '5': temp += "pet"
# if letter[0] == '6': temp += "sest"
# if letter[0] == '7': temp += "sedum"
# if letter[0] == '8': temp += "osum"
# if letter[0] == '9': temp += "devet"
# temp+=" "
# # second digit
# if letter[1] == '1': temp+= "eden"
# if letter[1] == '2': temp += "dva"
# if letter[1] == '3': temp += "tri"
# if letter[1] == '4': temp += "cetiri"
# if letter[1] == '5': temp += "pet"
# if letter[1] == '6': temp += "sest"
# if letter[1] == '7': temp += "sedum"
# if letter[1] == '8': temp += "osum"
# if letter[1] == '9': temp += "devet"
#
# print(temp)

# chasovi = ['pon', 'petok', 'sreda']
# vikend= ['sab','ned']
# if str(input("den ")) in chasovi: print("chas")
# else: print("sloboden")

palind = str(input("number "))
if palind[::-1] == palind: print("true")
else: print("false")

