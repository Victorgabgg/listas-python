"""
#Aprovando empréstimo de uma casa, a prestação não pode passar 30% do salário. 12
valor = int(input('Digite o valor da casa: '))
sal = int(input('Digite o salário do comprador: '))
anos = int(input('Quantos anos de financiamento:  '))

meses = anos * 12
prestação = valor/meses

print(f'O valor da parcela mensal ficará R$ {prestação:.2f} ')
if prestação > sal * 0.30:
    print('O empréstimo foi NEGADO!')
else:
    print('O empréstimo foi CONCEDIDO!')
"""

#Conversor de bases numéricas
num = int(input('Digite o número para ser convertido: '))
print('''Escolha a sua opção de conversão:
[1] Converter para binário.
[2] Converter para octal.
[3] Converter para Hexadecimal ''')
op = int(input('Sua opção: '))
if op == 1:
    print(f'O número convertido é {bin(num)[2:]}')
elif op == 2:
    print(f'O número convertido é {oct(num)[2:]}')
elif op == 3:
    print(f'O número convertido é {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente')

