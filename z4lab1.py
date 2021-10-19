def z4():
    n = int(input('Введите число : '))
    a = n/2
    b = (a + n/a)/2
    while b != a:
        a = b
        b = (a+ n/a)/2
    print(a)
    return a
z4()