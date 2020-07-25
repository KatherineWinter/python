# Strings

```
str1 = '548'
str2 = "eight"
str_multiple_lines = '''
this is a
multiple line string

multiple lines!
'''
str_formatted f'formatted string {str1}'
```

# Integers

apple = 8

# Floats

apple = 4.4

# Booleans

dog = True
Ivan = False


# Arrays

* SQUARE brackets
* commas seperated values
* takes values of a type

```
list_of_strings = ['katherine', 'rob', 'curtis']
list_of_ints = [0, 1, 5, 6, 43, 56]
list_of_floats = [0.4 , 3.6 , 8.3]
```

# Operators

* Adding a number to another number
`item += 1`
* Number is greater than other number
`item > 10`
* Number is less than other number
`item < 10`
* Number is equal to other number
`item == 20`
* Number is greater than or equal to other number
`item >= 10`
* Number is less than or equal to other number
`item <= 10`


# Loops

**While loop**

```
x = 0
while x < 10:
x += 1
```

**For loops**

```
list_of_strings = ['katherine', 'rob', 'curtis']
for item in list_of_strings:
print(item)
```

# Getting user input

**Getting a number**
```
userAge = input('What is your age? ')
if userAge.isdigit():
  print(f'in 10 years, your age will be {int(userAge) + 10}')
else:
  print('please only use a number for age')
```

**Getting a string**

```
name = input('What is your name ')
print(f'Hello {name}')
```

# Indenting

"if you use a : the next line will be indented"

```
if True:
  print('hello')
elif True:
  print('hello')
else:
  print('hello')

while True:
  print('hello')

for item in ['hello']:
  print('hello')

def hello ():
  print('hello')
```

# 3D Array [x][y]

```
battleShip = [
  [2, 5, 0, 1],
  [1, 0, 0, 1],
  [1, 0, 0, 10],
  [1, 0, 0, 0]
]

print(battleShip[0][0]) # 2
print(battleShip[0][1]) # 5
print(battleShip[2][3]) # 10
```
