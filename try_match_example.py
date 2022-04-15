valor_aposta = input('Digite o valor apostado= ')
numero_jogador = input('Digite o número do jogador= ')

try:
    valor_aposta = float(valor_aposta)
    numero_jogador = float(numero_jogador)

except:
    print('error')
