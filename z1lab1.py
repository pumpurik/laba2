def z1(): 
 num = int(input('Введите целое число : '))
 n=num
 rev = 0
 while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
 if num == rev:
    print ('True')
    return True
 else:
     print ('False')
     return False
z1()