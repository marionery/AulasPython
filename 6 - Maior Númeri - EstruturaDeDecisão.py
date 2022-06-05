#exercicio python 6 - Estrutura de Decisão
#https://wiki.python.org.br/EstruturaDeDecisao

#Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

if (num1 > num2) and (num1 > num3):
    print('O primeiro número é o maior número')
elif (num2 > num1) and (num2 > num3):
    print('O segundo número é o maior número')
else:
    print('O terceiro número é o maior número')