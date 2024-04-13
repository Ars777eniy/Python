fraza = "Умная земля, привет мир."
print(fraza)
letters = list(fraza)
for i in letters[-4:-1]:
  print("\t", i)
print()
for i in letters[-11:-4]:
  print("\t" * 2, i)
print()
for i in letters[6:11]:
  print("\t" * 3, i)
print()
for i in letters[:5]:
  print("\t" * 4, i)
print()