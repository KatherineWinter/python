import random

totalChances = 30
days = totalChances
totalFly = 0
while days > 0:
  days -= 1
  rain = random.randint(0, 1)
  if rain:
    print("poor ryan, no fly")
  else:
    print("happy ryan, sad katherine")
    totalFly += 1

print(f'ryan flew {totalFly}/{totalChances} times.')
