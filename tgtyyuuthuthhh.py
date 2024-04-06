money = 1000
while True:
  print('Игра "АВТОМАТ ЖЕЛАНИЙ"!')
  print('Осталось денег:', money)
  buy = int(input('    Сколько хотите потратить? '))

  if buy <= 0:
    print('К сожалению, на это ничего не купишь!')
    money -= buy
  elif buy >= 1 and buy <= 10:
    print('Опа, лови яблочко!')
    money -= buy
  elif buy >= 11 and buy <= 100:
    print('Эта сумма потянет на Iphone!')
    money -= buy
  elif buy >= 101 and buy <= 1000:
    print('Оранжевая Ламба твоя!')
    money -= buy
  elif buy == ('Пока'):
    print('До скорых встреч!')
  else:
    print('Что за шутки?!')
  if money <= 0:
    print('Денег больше нет!:(')
    break