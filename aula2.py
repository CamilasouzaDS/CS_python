nome = 'Camila'
idade = 21
ano_atual = 2022
altura = 1.60
peso = 64.50
imc = peso / altura ** 2
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O imc da {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
ano_nascimento = 2019 - int(idade)

print(nome, type(nome))