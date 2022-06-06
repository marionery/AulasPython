#exercicio python 26 - Estrutura de Decisão
#https://wiki.python.org.br/EstruturaDeDecisao

# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# ------------------------
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# ------------------------
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# ------------------------
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
# da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

tipo_combust = input('Informe o tipo de combustível (A = álcool / G = gasolina): ').upper()
quantidade_combust = float(input('Informe a quantidade do combustível comprado em litros: '))

if (tipo_combust == 'A'):
    preco = 1.90
    if quantidade_combust <= 20:
        desconto = .03
    else:
        desconto = .05
else:
    preco = 2.50
    if quantidade_combust <= 20:
        desconto = .04
    else:
        desconto = .06

total_desconto = (preco * quantidade_combust) * desconto
total_pagar = (preco * quantidade_combust) - total_desconto

print(f'Total a pagar: R$ {total_pagar:,.2f}')
print(f'Desconto de: R$ {total_desconto:,.2f}', '(',(desconto * 100),'% )')