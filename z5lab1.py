def z5():
   n = int(input('Введите целое число : '))
   if n < 2:
       print('False')
       return False

   if n == 2:
       print('True')
       return True

   limit = n**(1/2)

   i = 2

   while i <= limit:

       if n % i == 0:
           print('False')
           return False

       i += 1
   print('True')
   return True
z5()