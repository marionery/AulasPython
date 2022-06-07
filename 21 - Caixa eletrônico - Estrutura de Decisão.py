#exercicio python 21 - Estrutura de Decisão
#https://wiki.python.org.br/EstruturaDeDecisao

# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
# é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5
# e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
# uma nota de 5 e quatro notas de 1.

bemvindo = print('SEJA BEM VINDO AO BANCO TABAJARA')
disponivel = print('As notas disponíveis neste caixa são: R$ 1, 5, 10, 50 e 100')
print('---------------------------------------------------')
saque = float(input('Informe o valor do seu saque: R$ '))
print('---------------------------------------------------')

while (saque < 5) or (saque > 600):
    print('Valor inválido. Valor sacado deve estar entre R$ 5 e R$ 600')
    saque = float(input('Informe o valor do seu saque: R$ '))
else:
    unidade = saque % 10
    dezena = saque / 10 % 10
    centena = saque / 100 % 100

if unidade > 5:
    cinco = 1
    unidade = unidade - 5
else:
    cinco = 0

if dezena > 5:
    cinquenta = 1
    dezena = dezena - 5
else:
    cinquenta = 0

print ('Notas fornecidas: %d notas de 100, %d notas de 50, %d notas de 10, %d notas de 5 e %d notas de 1' % (centena, cinquenta, dezena, cinco, unidade))