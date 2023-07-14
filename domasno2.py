# ЗАДАЧА 1
# Да се напише програма којашто за датум прочитан од стандарден влез во форматот (DD MM YYYY)
# ќе испечати порака ДА доколку датумот е валиден или порака НЕ доколку датумот не е валиден.
# За оваа проверка да се креира функција којашто ќе ја проверува валидноста на датумот.
# Печатењето на пораката да се направи надвор од функцијата.
#
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
#
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

# Задача 4
# Да се внесе еден стринг од страна на корисникот и за дадениот стринг да се извршат следните модификации:
# Да се прочисти стрингот од знаците ! и . и да се сменат сите букви во мали

# Задача 5
# Dа се напише програма во која од стандарден влез прво се внесува еден
# позитивен цел број z, а потоа последователно се внесуваат парови цели
# броеви (a, b). Внесувањето на парови цели броеви треба да заврши кога
# корисникот ќе го внесе парот (0, 0). Треба да се пресмета колку пати z е
# еднаков на збирот на секој внесен пар броеви a и b, како и колкав процент
# од вкупниот број внесени парови (a, b) даваат збир z (ЗАБЕЛЕШКА: парот (0,
# 0) не се зема во предвид при извршувањето на пресметките!).

# Задача 6
# Да се внесе еден стринг од страна на корисникот и за дадениот стринг да се извршат следните модификации:
# Да се отстранат празните места на почеток и крај од стрингот
# Да се изброи колку пати се појавува буквата „а“
# а колку буквата „м“ во стрингот
# (да се земат во предвид и големите и малите букви при ова броење)
# Да се замени буквата „т“ во стрингот со карактерот „$“
# а буквата „б“ со карактерот „*“
# (да се земат во предвид и големи и малите букви при оваа модификација)