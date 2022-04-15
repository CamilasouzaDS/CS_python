
while True:
    num_1 = input('Write a number: ')
    num_2 = input('Write another number: ')
    operator = input('Choose a operator, example (+, - , / and *: ')
    exit = input('Do you want to exit? ')

    if exit == 's':
        break

    if not num_2.isnumeric() or not num_1.isnumeric():
        print('Please provide a valid number')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '/':
        print(num_1 / num_2)
    elif operator == '*':
        print(num_1 * num_2)
    else:
        print('Invalid operator')

