#exercicio python 9 - Estrutura de Decisão
#https://wiki.python.org.br/EstruturaDeDecisao

#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

lista = [num1, num2, num3]
lista.sort(reverse=True)
lista_str = str(lista)[1:-1]
print('Resultado da lista em ordem decrescente:', lista_str)