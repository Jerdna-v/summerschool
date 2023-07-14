# import numpy as np
# import random as r
# # Задача 2.0:
# names = ["James", "John", "Mark", "Rick", "Taylor", "Ted", "Robin", "Barney", "Joey", "Jessica"]
# # Имаме дадена листа од имиња. Од дадената листа да се креира numpy низа. Од низата со помош на random модулот да се
# # одбере име по случаен избор. Ова име да му биде прикажано на корисникот којшто ќе може да одбере дали името да се
# # зачува во листата или не. Постапката да се повтори k (број внесен на почеток од програмата) пати (или додека не
# # снема имиња).
# np_l = np.array(names)
# protected= int(input("protect"))
# while 0>=protected>len(np_l)/2: protected= int(input("protect"))
# counter=0
# # np_l_protected=np.empty([1,protected])
# try:
#     # np_l_protected=np.array([x for x in np_l if input(str(x)+"Da se zastiti? (y/n)")=='y'] and )
# except:
#     pass
# times=int(input())
# while times > 0 or len(np_l) <= 0:
#     rand=r.randint(0, len(np_l)-1)
#     if input(str(np_l.item(rand))+" - Da se izbrise? (y/n)") == 'y' and np_l.item(rand) not in np_l_protected: np_l = np.delete(np_l, rand)
#     times -= 1
# print(np_l)
#
# # Задача 2.1: Да му се дозволи на корисникот да „заштити“ одредени имиња од отстранување од листата. Односно да се
# # елиминира ситуацијата кадешто за „заштитено“ име ќе биде прашан корисникот дали ќе биде отстрането ова име. На
# # почеток корисникот внесува број m којшто означува колку имиња сака да заштити. Овој број не може да биде поголем од
# # големината на листата / 2. Доколку се внесе невалиден број да се побара од корисникот повторно да внесе валиден
# # број. Откако ќе внесе валиден број, ги внесува m-те заштитени имиња.
#
