def z3(): 
 n = int(input('Введите целое число : '))
 rev = 0
 if n >0:
  while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
 else:
  n=n*-1
  while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
  rev=rev*-1
 print (rev)
z3()