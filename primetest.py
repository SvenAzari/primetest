#In order to run this script, you need to have Python 3 installed.
#Made by Sven Azari
#http://www.github.com/svenazari

#import
import math
from os import system, name

#clear
def clear ():
  if name == 'nt':
      _ = system('cls')
  else:
      _ = system('clear')

#main part
def primetest ():
    print ("# PRIME TEST #")
    print (" ")
    prime = float(input ("X = "))
    print (" ")
    prime1 = math.ceil(prime / 2) + 1
    if prime == 1:
      print ("NOR PRIME NOR COMPOSIT")
      fuex ()
    elif prime == 2:
      print ("PRIME")
      fuex ()
    elif prime < 1:
      print ("ENTER ONLY NATURAL NUMBERS")
      primetest ()
    for PT in range (2, prime1, 1):
        a = prime % PT
        if a == 0:
            break
    if a != 0:
        print ("PRIME")
        fuex ()
    else:
        print ("COMPOSITE")
        fuex ()

#exit function
def fuex ():
  ex = float(input ("[1 (new), 2 (exit)]: "))
  if ex == 1:
    clear ()
    primetest ()
  elif ex == 2:
    clear ()
    exit ()
  else:
    print ("Wrong input!")
    fuex ()

clear ()
primetest () #call main part function
