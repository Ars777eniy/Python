while True:
  grades = input("Vvedi grades: ")
  mas = grades.split()

  n = len(mas)
  sum = 0
  for i in range(n):
    if mas[i].isnumeric() == False:
      print('Вы ввели не число!')
      break
    chislo = int(mas[i])
    if chislo < 0 or chislo > 10:
      print('Вы не ввели оценку от 1 до 10!:(')
      break
    sum = sum + chislo
  print(sum/n)


