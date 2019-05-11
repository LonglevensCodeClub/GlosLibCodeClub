import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!^&*()_+:@~}{;'

lngth = input('password length')
length = int(lngth)


for p in range(3):  
  password = ''

  
  for c in range (length):
    password += random.choice(chars)
  print(password)





