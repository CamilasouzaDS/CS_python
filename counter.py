'''counter = 0
accumulator = 0

while counter <= 10:
    print(counter, accumulator)
    if counter > 5:
        break
    accumulator = accumulator + counter
    counter += 1
else:
    print('arrived on else')
'''

phase = 'I love you'
counter = 0
length = len(phase)
new_phase = ''

user_input = input('Which letter do you want to upper? ')
while counter < length:
    letter = phase[counter]
    if letter == user_input:
        new_phase += letter.upper()
    else:
        new_phase += letter
        counter += 1
    print(new_phase)



