# ЗАДАЧА 1
# Да се напише програма којашто за датум прочитан од стандарден влез во форматот (DD MM YYYY)
# ќе испечати порака ДА доколку датумот е валиден или порака НЕ доколку датумот не е валиден.
# За оваа проверка да се креира функција којашто ќе ја проверува валидноста на датумот.
# Печатењето на пораката да се направи надвор од функцијата.
def date_check(date):
    if date[3:5] == "02" and (date[:2] <= "28" or "29"):
        if int(date[6:])%400==0 or (int(date[6:])%4==0 and int(date[6:])%100!=0): print("leap year")
        return "valid"
    if date[3:5] == "01" or "03" or "05" or "07" or "08" or "10" or "12" and date[:2] <= "31": return "valid"
    if date[3:5] == "04" or "06" or "09" or "11" and date[:2] <= "30": return "valid"
    return "not valid"

print(date_check(str(input("Input date: "))))

# 1,3,5,7,8,10,12 - 31
# 2
# 4, 6, 9, 11 - 30
#
# Проверка за валидност на датумот:
# Дали месецот е помеѓу Јануари и Декември (1-12)
# Дали бројот на денови е соодветен според месецот
# Доколку месецот е Февруари дали годината е престапна?
# Престапни години се годините коишто се деливи со 400 или се деливи со 4 ама не со 100.

# ЗАДАЧА 2
# Да се напише програма којашто од стандарден влез ќе вчитува 3 карактери и
# истите ќе ги шифрира во две секвенци со должина 3.
# На крај да се спојат овие 2 секвенци во еден број.
def combine(first, second):
    first.extend(second)
    return int("".join(first))
def first(l):
    for i in range(len(l)):
        if l[i].isalpha():l[i]="6"
        elif l[i].isnumeric(): l[i] = "8"
        else: l[i] = "1"
    return l
def second(l):
    for i in range(len(l)):
        if l[i].isalpha():l[i]="1"
        else: l[i] = "0"
    return l
l= str(input("input: ")).split(" ")
print(combine(first(l.copy()), second(l)))

# Правила за првата секвенца:
# Доколку карактерот е број да се замени со 8
# Доколку карактерот е буква да се замени со 6
# Доколку карактерот е специјален знак да се замени со 1
#
#
# 	Правила за втората секвенца:
# 	     - Доколку каратерот е буква да се замени со 1, во спортивно   со 0
#
# За решавање на задачата да се креираат три функции:
# Функција за првото шифрирање
# Функција за второто шифрирање
# Функција за спојување на двете шифри
#
#
#
# Примери:
#
#
# / * 1
# Прва секвенца - 118
# Втора секвенца - 000
# Краен резултат - 118000
#
# a # 2
# Прва секвенца - 618
# Bтора секвенца - 100
# Краен резултат - 618100

# Задача 3
# За дадена листа да се изброи за секој елемент колку пати се појавува и да се креира речник со резултатот
# primer = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

l = str(input("input a list")).split(",")
d ={}
for e in l:
    if e in d.keys(): d[e]+=1
    if e not in d.keys(): d[e]=1
# Задача 4
# Да се внесе еден стринг од страна на корисникот и за дадениот стринг да се извршат следните модификации:
# Да се прочисти стрингот од знаците ! и . и да се сменат сите букви во мали

print(str(input("input ")).replace(".","").replace("!","").lower())

# Задача 5
# Dа се напише програма во која од стандарден влез прво се внесува еден
# позитивен цел број z, а потоа последователно се внесуваат парови цели
# броеви (a, b). Внесувањето на парови цели броеви треба да заврши кога
# корисникот ќе го внесе парот (0, 0). Треба да се пресмета колку пати z е
# еднаков на збирот на секој внесен пар броеви a и b, како и колкав процент
# од вкупниот број внесени парови (a, b) даваат збир z (ЗАБЕЛЕШКА: парот (0,
# 0) не се зема во предвид при извршувањето на пресметките!).
z = int(input("z = "))
counter=0
times=0
while True:
    x, y = str(input()).split(" ")
    x=int(x)
    y=int(y)
    if x==0 and y==0:break
    if x+y==z: counter+=1
    times+=1
print(counter, counter/times*100, "%")
# Задача 6
# Да се внесе еден стринг од страна на корисникот и за дадениот стринг да се извршат следните модификации:
# Да се отстранат празните места на почеток и крај од стрингот
# Да се изброи колку пати се појавува буквата „а“
# а колку буквата „м“ во стрингот
# (да се земат во предвид и големите и малите букви при ова броење)
# Да се замени буквата „т“ во стрингот со карактерот „$“
# а буквата „б“ со карактерот „*“
# (да се земат во предвид и големи и малите букви при оваа модификација)
inp_str=str(input("input ")).strip().lower().replace("t","$").replace("b","*")
print(inp_str)
print(inp_str.count("a"), inp_str.count("m"))