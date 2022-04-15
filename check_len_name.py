name = str(input('What´s your name? '))
characters = len(name)

if characters < 4:
    print('your name is too short')
elif 5 <= characters < 8:
    print('Your name is normal')
else:
    print('your name is too long')
