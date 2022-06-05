#exercicio python 14 - Estrutura Sequencial
#https://wiki.python.org.br/EstruturaSequencial

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

limite = 50.00
multa = 4.00

peso_pescado = float(input('Informe o peso pescado em KG: '))

if peso_pescado <= 50:
    print('Peso dentro do limite da cota estabelecida. Sem multa.')
else:
    excedente = (peso_pescado - limite)
    valor_multa = (excedente * multa)
    print('O excedente foi de', excedente, 'Kgs.')
    print(f'A multa devida é R$ {valor_multa:,.2f}')