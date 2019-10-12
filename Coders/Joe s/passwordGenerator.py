#!/bin/python3
import random
passlength = 30
chars = 'abcdefghijklmnopqrstuvwxyz1234567890};@~#!£$*SDFGH'
password =''
for c in range (passlength):
  password += random.choice(chars)
  
  
print(password)