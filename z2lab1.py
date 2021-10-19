def z2():
    spisok = [int(i) for i in input('Введите список через пробел из положительных целых чисел ').split()]
    spisok1 = []
    for i in spisok:
        if i%2==0 :
            spisok1.append(i)
    print (spisok1)
    spisok2=[]
    for i in spisok:
        if i%3==0 :
            spisok2.append(i)
    print (spisok2)
    spisok3=[]
    for i in spisok:
        if i%5==0 :
            spisok3.append(i)
    print (spisok3)
z2()

