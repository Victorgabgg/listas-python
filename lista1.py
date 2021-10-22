"""
#Ordem de precedência: (), **, *,/,//,%, + e -

#Programa que recebe o nome
nome = input('digite seu nome ')
print('prazer em conhecer, {} '.format(nome))

#Programa que lê dois valores
n1 = int(input('digite o primeiro num '))
n2 = int(input('digite o segundo num '))
n3 = n1 + n2
print(n3)

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))



#Programa que mostra o sucessor e antecessor do número
num = int(input('Digite um número '))
antecessor = num - 1
sucessor = num + 1
print('Analisando o número {}. Seu sucessor é {} e seu antecessor {}.'.format(num, sucessor, antecessor))
# print('Analisando o número {}. Seu sucessor é {} e seu antecessor {}.'.format(num,(n+1),(n-1)))
# print (f'O seu antecessor é {n1 - 1} e o seu sucessor é {n1 + 1}' )


#Programa que mostra o dobro, triplo e raiz quadrada
num = int(input('Digite um número: '))
print(f'O dobro do número é {num*2} o triplo {num*3} e a raiz quadrada {num**(0.5)}')
#print(f'O dobro de {num} é {num*2}.\nO triplo é {num*3}\nA raiz quadrada é {num**(1/2):.2f}.')


#Media aritmética
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média do aluno foi {media:.1f}')
"""

#Conversor de medidas
dist = int(input('Digite um valor em metros: '))
print(f'O valor em kilômetro {dist/1000}\ndecâmetro {dist/10}\nhectômetro {dist/100}\ncentímetro {dist*100}\nmilímetro {dist*1000}')