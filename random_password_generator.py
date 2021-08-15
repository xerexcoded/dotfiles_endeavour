import random
import os
os.system('cls')


upperCase ="ABCDEFGHIJKLMNOPQRSTVWXYZ"
lowerCase =upperCase.lower()
digits= '1234567890'
symbols = '!@#$%^&*();:?~'

upper,lower,nums,syms=True ,True,True ,True
all=''
print("Y for yessir N for NOPLEASE!!")
u=input("want some uppercase action too? :")
if u == 'n' or u == 'N':
    upper=False
else:
    all+=upperCase
u=input("do you want lowercaseyyyyyyy missy? :")
if u =='n' or u =='N':
    lower=False
else:
    all+=lowerCase
u=input("want ramanujan's friend to come to your passywardy? :")
if u =="n" or u =="N":
    digits=False
else:
    all+=digits
u=input("want some symbols , if yes you are a simp? :")
if u=='n' or u=='N':
    syms=False
else:
    all+=symbols
length =int(input("how long is it gonna be :"))

passwardy="".join(random.sample(all,length))
print(passwardy)
#max limit for number of characters is 74
