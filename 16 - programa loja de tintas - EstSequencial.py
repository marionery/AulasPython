#exercicio python 16 - Estrutura Sequencial
#https://wiki.python.org.br/EstruturaSequencial

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Informe o tamanho da área a ser pintada em M²: '))
valor_lata = float(input('Informe o valor da lata de 18L: '))

rendimento = 18 * 3
quant_latas = (area / rendimento)
custo_total = (quant_latas * valor_lata)

if quant_latas <= 1:
    print('Você só precisará comprar uma lata')
elif area > rendimento:
    print(f'A quantidade de latas é: {quant_latas:,.2f}')

if quant_latas <= 1:
    print(f'O valor total da compra será: R$ {valor_lata:,.2f}')
elif quant_latas > 1.01:
    print(f'O valor total da compra será: R$ {custo_total:,.2f}')