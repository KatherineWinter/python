
while True:
  age = input('What is your age? ')
  if age.isdigit() == False:
    print('Age must be a number')
    continue
  castAge = int(age)
  if castAge < 0 or castAge > 120:
    print('Age is invalid. Must be between 0-120')
    continue

  print(f'Thank you for submitting your age: {age}')
  break