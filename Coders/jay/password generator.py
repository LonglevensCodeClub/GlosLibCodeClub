import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!^&*()_+:@~}{;'

password = ''


for c in range (10):
    password += random.choice(chars)
print(password)





