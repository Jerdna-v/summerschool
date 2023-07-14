# flight_prices = {"Dortmund": 4480,
#  "Frankfurt": 7128,
#  "Budapest": 2595,
#  "Berlin": 8910,
#  "Paris": 3537,
#  "Venice": 2668,
#  "London": 2595,
#  "Milan": 2595,
#  "Rome": 5658,
#  "Malta": 5578}
# inp = str(input())
# if inp not in flight_prices.keys():
#     flight_prices[inp]=None
# print(flight_prices[inp])

# list1 = [11,22,3,10]
# list2 = [6,7,8,9,10,11,11,23,34,67]
#
# # list1 = [10]
# # list2 = [76,71]
#
# list1.extend(list2)
#
# if 4<=len(list1)<=10:
#     list1 = list(set(list1))
#
# else:
#     while(len(list1)<4): list1.append(0)
#     list1 = list1[:10]
# list1.sort()
# print(list1)

# inp = int(input())
# counter=1
# while(inp>0):
#     counter*=inp
#     inp-=1
# print(counter)

# inp = int(input())
# for num in range(1,inp+1):
#     if num % 3 == 0 and num % 5 == 0:
#         print("#tripet")
#         continue
#     if num % 3 == 0: print("#tri")
#     elif num % 5 == 0: print("#pet")
#     else: print(num)

lines = ["aBcccbB", "Ova e linija 2.", "Ova e TreTa linija."]

for word in lines:
    print(word.lower())

inp = int(input())

for num in range(11):
    print(inp," * ",num," = "+str(inp*num))