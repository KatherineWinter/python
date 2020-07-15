import random
departments = ['sales', 'marketing', 'support', 'engineering', 'HR', 'Ops', 'IT','Security', 'Janitor', 'Shipping']
correctDepartment = 2
randomDepartment = -1
tries = 0
while True:
    randomDepartment = random.randint(0, 9)
    print(f'you\'ve reached {departments[randomDepartment]}')
    tries += 1

    if randomDepartment == correctDepartment:
        print("Oh thank god, I need to fix my phone, please help!")   
        break

    if tries == 4:
        print(f"FDSFDS THIS! I'VE TRIED {tries} TIMES TO GET TO SUPPORT! I'M OUT!")
        break
