"""
#Jogo de advinhar o número
from random import random, randint
rand = randint(0, 5)
num = int(input('Tente advinhar o número que o computador gerou de 0 até 5: '))
if rand == num:
    print(f'Você ganhou!! o número é: {rand}')
else:
    print(f'Você perdeu!! o número é: {rand}')


#Programa que lê a velocidade do carro e multa se for acima de 80km em 7 reais a cada km a mais.
vel = int(input('Digite a velocidade do carro '))
if vel > 80:
    valor = vel - 80
    multa = valor * 7
    print(f'Você ultrapassou o limite de 80km, multado em R$ {multa}.')
else:
    print(f'Você não passou do limite, está em {vel}.')


#Par ou impar
n = int(input('Digite um numero inteiro qualquer: '))
if n%2==0:
    print('O número é par')
else:
    print('O número é impar')


#Programa que pergunta a distância da viagem e cobra R$ 0.50 para viagens até 200km e 0.45 para viagens mais longas
km = (int(input('Digite o valor em Km da viagem total: ')))
if km <= 200:
    total = km * 0.50
    print(f'O total da viagem até 200 km ficou: {total}')
else:
    total = km * 0.45
    print(f'O total da viagem maior que 200 km ficou: {total}')


#Calculo de ano bissexto
ano = (int(input('Digite o ano para checar se é bissexto: ')))
if ano % 4 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')


#Programa que lê três valores e diz o maior e menor entre eles
n1 = (int(input('Digite o primeiro valor: ')))
n2 = (int(input('Digite o segundo valor: ')))
n3 = (int(input('Digite o terceiro valor: ')))

numeros = [n1,n2,n3]
print(f'O maior valor digitado foi {max(numeros)}')
print(f'O menor valor digitado foi {min(numeros)}')
"""

#Programa que aumenta o salário de funcionários se > 1.250 aumenta 10% e para <= 1.250, 15%.
sal = int(input('Digite o valor do seu salário: '))
if sal > 1250:
    aumento = sal * 0.10
    sal = sal + aumento
else:
    aumento = sal * 0.15
    sal = sal + aumento
print(f'Seu salário ficou {sal}')

