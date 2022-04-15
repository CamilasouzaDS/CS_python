user_Hour = input('What time is it? ')

if user_Hour.isdigit():
    user_Hour = int(user_Hour)

    if 0 < user_Hour < 12:
        print('Good morning')
    elif 13 < user_Hour < 17:
        print('Good evening')
    elif 18 < user_Hour < 23:
        print('Good night')
    else:
        print('You live on earth, we just have 24 hours per day')
else:
    print('Please provide a real time')