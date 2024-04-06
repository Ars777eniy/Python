import random
from random import randint

def vivod(a):
  if(a == 51):
    print("---------------------------")
    print("     |*|    |2|    |3|     ")
    print("---------------------------")
  elif(a == 2):
    print("---------------------------")
    print("     |1|    |*|    |3|     ")
    print("---------------------------")
  else:
    print("---------------------------")
    print("     |1|    |2|    |*|     ")
    print("---------------------------")
dengi = 1000
while True:
  chislo = random.randint(1, 3)
  print('В какой коробке алмазик?')
  print("---------------------------")
  print("     |1|    |2|    |3|     ")
  print("---------------------------")
  print("tvoi dengi:", dengi)
  stavka = int(input("vvedi stavky:"))
  if(stavka <= dengi):
    if(int(input("vvedi nomer:")) == chislo):
      vivod(chislo)
      print("Ti ygadal")
      dengi += stavka
    else:
      vivod(chislo)
      print("Ne ygadal")
      dengi -= stavka
  else:
    print("Vi vveli bolshe chem y vas est")
  if dengi <= 0:
    print("Ti bancrot")
    break
  elif dengi >= 10000:
    print("Ti razbagatel")
    break