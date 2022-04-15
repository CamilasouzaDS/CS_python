number = input('Please, provide an integer number')

if number.isdigit():
    number = (int(number))
    result = number % 2
    if result == 0:
        print("even number")
    else:
        print('odd number')
else:
    print('Not a integer number bro ')




