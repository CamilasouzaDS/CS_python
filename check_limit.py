name = input('Qual seu nome? ')
age = int(input('Qual sua idade? '))
minimal_age = 18 #idade minima
maximium_age = 50 #idade maxima

if minimal_age <= age <= maximium_age:
    print(f'Congratulations {name} your request was approved')
elif True:
    print('unfortunately you are too young :( ')
else:
    print('none')
