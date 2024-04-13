import random
while True:
  Ru = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ы','ъ','э','ю','я','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Э','Ю','Я')

  En = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

  Sim = ('!','#','$','%','^','&','*','(',')','-','_','=','+','*','/','|','"','№',';',':','?')

  Chisla = ('1','2','3','4','5','6','7','8','9','0')

  Pr = ('@gmail.com','@gmail.ru','@gmail.by',)

  space = [" "]
  word = []
  word.extend(space)
  word.extend(En)
  word.extend(Ru)
  word.extend(Sim)
  word.extend(Chisla)
  print(word)

  email = ""
  kolSimvol = int(input("Из скольки символов будет email:"))
  for i in range(kolSimvol):
    k = random.randint(0, len(word))
    print(k)
    email += word[k]
  print("Ваш email:",email,random.choice(Pr)) 