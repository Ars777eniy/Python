import random

while True:
  zvania = ["самая", "самая-самая", "лучшая", "наилучшая", "добрая", "хорошая", "умная"]
  name = input("vvedi ima, mama:")
  a = random.choice(zvania)
  print("Приветствую", "тебя", "моя", a, name, "!!!", sep ="_")

  print(f"Приветствую тебя моя {a}, {name}, !!!")