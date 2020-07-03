while True:
  num = input('Give me a number: ')
  if num.isdigit() == False:
    print('invalid input')
    continue

  if int(num) % 2 == 0:
    print(f'{num} is an even number\n')
  else:
    print(f'{num} is an odd number\n')
