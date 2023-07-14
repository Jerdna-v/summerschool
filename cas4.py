def number_five_print(*args):
    # args=args[0]
    # print(args)
    if len(args) == 1:
        args= tuple(args[0])
    # print(args)
    if args[0]>500: return
    if args[0]>150: number_five_print(args[1:])
    if args[0]%5==0:print(args[0])
    number_five_print(args[1:])
# number_five_print(12,75,150,100,145,525,60)

#1
def modul_calc(n,modul):
    return sum([x for x in range(n+1) if x%2==modul])
def even_odd_division(number):
    print(modul_calc(number,0)/modul_calc(number,1))
# even_odd_division(10)


def reverse_list(l):
    i = len(l)-1
    while(i>=0):
        print(l[i])
        i-=1
# reverse_list([1,2,3,4])


def n_m_sum(n,m):
    sum=0
    n_str=""
    for i in range(m):
        n_str+=str(n)
        sum+=int(n_str)
        print(n_str,sum)
    print(sum)
n_m_sum(2,5)

def n_m_rec(n,m):
    if m==0:return n
    return n_m_rec(n,m-1)+n

def fml_string(s1,s2):

    temp=s1[0]+s2[0]

    if(len(s1)%2==0):
        temp+=s1[int(len(s1)/2-1)]+s1[int(len(s1)/2)]
    else:
        temp += s1[int(len(s1) / 2)]
    if (len(s2) % 2 == 0):
        temp += s2[int(len(s2) / 2 - 1)]+s2[int(len(s2) / 2)]
    else:
        temp += s2[int(len(s2) / 2)]

    temp+=s1[-1]+s2[-1]
    print(temp)
fml_string("America","Semos")
fml_string("sega","arno")

plus = lambda x,y: x+y
minus = lambda x,y: x-y
times = lambda x,y: x*y
div = lambda x,y: x/x

students = [
    ("Tea", 100),
    ("Ana", 12),
    ("Marija", 56),
    ("Aleksandar", 92),
    ("Milan", 78),
    ("Ivan", 45)
]

# Да се извадат посебно положените а посебно неположените студенти. Услов за положување е над 50 поени.

passed=[s for s in students if s[1]>50]
failed=[s for s in students if s[1]<=50]

# Да се креира листа само со имињата од положените студенти и да се сортираат по азбучен редослед

passed_name=[p[0] for p in passed ]

# Да им се додадат плус 5 поени на неположените студенти поради грешка на професорите при преглед на задачите и

passed_new=passed.extend([s for s in failed if s[1]+5>50])

# повторно да се извршат пресметките

# Да се пресмета процентот на положеност пред и по додавање на дополнителните поени


employees = [
    ("Tea", 87000),
    ("Ana", 12300),
    ("Marija", 56000),
    ("Aleksandar", 92000),
    ("Milan", 7800),
    ("Ivan", 34000),
    ("Ivana", 13450)
]

# Фирмата одлучила да им се даде покачување на вработените за 6% од нивната моментална плата, изврши ја промената во
# листата
# employees=[emp for emp in employees emp[1]+emp[1]*6%]
# Владата одлучува да се зголеми минималната плата на 18000, имплементирај ја промената во листата
# employees=[emp for emp in employees if emp[1]<18000]
# Фирмата одлучува да ги награди Ивана и Милан со дополнително зголемување од 10000
# employees=[emp for emp in employees if not emp[0]=="Ivana" or emp[0]=="Milan"]
# Фирмата одлучува да ја отпушти Ана
# employees=[emp for emp in employees if not emp[0]=="Ana"]
# # Фирмата одлучува да им се намали платата за 10% на сите што земаат над 50000 поради економска криза
#
# for emp in employees:
#     emp[1]=emp[1]+emp[1]*0.06
#     if emp[1]<18000: emp[1]=18000
#     if emp[0]=="Ivana" or emp[0]=="Milan": emp[0]+=10000
#     if emp[1]==50000: emp[1]=emp[1]-emp[1]*0.1
#
# employees=[emp for emp in employees if emp[0]!="Ana"]
#
#
#




def sum(n):
    if n==0: return 0
    return n+sum(n-1)

print(sum(3))

def sum_div(n):
    if n==0: return 0
    return 1/n+sum_div(n-1)

def fib(n):
    if n==0 or n==1: return n
    return (fib(n-1)+fib(n-2))
print(sum_div(3))
print(fib(5))





