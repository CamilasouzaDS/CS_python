secret = 'Camila'
letter = []
chances = 3

while True:
    letra = input('Choose one character: ')

    if len(letra) > 1:
        print('Oh sorry, only one character')
        continue
    letter.append(letra)

    if letra in secret:
        print(f'Uhu {letra} is one of the characters in the secret')
    else:
        print('Sorry, this letter don´t exist in secret')
        letter.pop()

    temporary_word = ''
    for secret_letter in secret:
        if secret_letter in letter:
            temporary_word += secret_letter
        else:
            temporary_word += '*'

    if temporary_word == secret:
        print(f"Mama call, congratulations, secret word was {secret}")
    else:
        print(f"secret word is {temporary_word}")

    if letra not in secret and chances > 0:
        chances -= 1
        print(f'You still have {chanc s}')
    else:
        print('No more chances, sorry :(')
