"""
import math
#Programa que mostra a raiz quadrada com o valor arredondado com ceil
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num}, é {math.ceil(raiz)}')

#Programa que transforma float em int
num = float(input('Digite um número float: '))
print(math.trunc(num))
#print(math.int(num)) math.floor

#Catetos e hipotenusa
c1 = float(input('Digite o cateto oposto: '))
c2 = float(input('Digite o cateto adjacente: '))
#hi = (c1 ** 2 + c2 ** 2) ** (1/2) --- Padrão
hi = math.hypot(c1,c2)
print(f'O valor da hipotenusa é {hi}')

#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')
print(f'Seu nome em maiúsculo fica: {nome.upper()}')
print(f'Seu nome em minúsculo fica {nome.lower()}')
letras = len(nome) - nome.count(' ')
print(f'Seu nome ao todo tem {letras} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]}, ele tem {len(separa[0])} letras')

#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite um número de 0 até 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')

#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
city = str(input('Digite o nome da cidade: ')).strip()
print(city[:5].upper() == 'SANTO')

#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
name = str(input('Digite seu nome completo: ')).strip()
print('silva' in name.lower())

#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print(f'Analisando quantas letras A tem: {frase.count("A") }')
print(f'A primeira letra A apareceu na posição {frase.find("A")}')
print(f'A última letra A apareceu na posição {frase.rfind("A")}')
"""

#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: '))
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]}')
print('Seu último nome é {}'.format(nome[len(nome)-1]) )
