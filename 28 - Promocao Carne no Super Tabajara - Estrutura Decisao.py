#exercicio python 28 - Estrutura de Decisão
#https://wiki.python.org.br/EstruturaDeDecisao

# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
# pagamento, valor do desconto e valor a pagar.

print('Promoção de Carnes do Mercado Tabajara')
print('--------------------------------------')
tipoCarne = int(input('Informe o tipo de carne comprada (1 = Filé / 2 = Alcatra / 3 = Picanha): '))
quantidadeCarne = float(input('Informe a quantidade de carne comprada em KG: '))
cartaoTabaj = int(input('Pagamento com Cartão Tabajara? (1 = SIM / 2 = NÃO): '))

if (tipoCarne == 1):
    print('')
    if (quantidadeCarne <= 5):
        preco = 4.90
        valorBruto = (quantidadeCarne * preco)
    else:
        (quantidadeCarne > 5)
        preco = 5.80
        valorBruto = (quantidadeCarne * preco)

elif (tipoCarne == 2):
    print('')
    if (quantidadeCarne <= 5):
        preco = 5.90
        valorBruto = (quantidadeCarne * preco)
    else:
        (quantidadeCarne > 5)
        preco = 6.80
        valorBruto = (quantidadeCarne * preco)

elif (tipoCarne == 3):
    print('')
    if (quantidadeCarne <= 5):
        preco = 6.90
        valorBruto = (quantidadeCarne * preco)
    else:
        (quantidadeCarne > 5)
        preco = 7.80
        valorBruto = (quantidadeCarne * preco)

if (cartaoTabaj == 1):
    valorDesconto = (valorBruto / 100) * 5
    valorFinal = valorBruto - valorDesconto
else:
    valorDesconto = 0.00
    valorFinal = valorBruto

print('-------------------------------------')
print('CUPOM FISCAL - SUPERMERCADO TABAJARA')
print('-------------------------------------')

if (tipoCarne == 1):
    print('Carne escolhida: Filé Duplo')
elif (tipoCarne == 2):
    print('Carne escolhida: Alcatra')
else:
    print('Carne escolhida: Picanha')
print('Quantidade comprada (Kg): ', quantidadeCarne)
print(f'Valor bruto: R$ {valorBruto:,.2f}')
if (cartaoTabaj == 1):
    print('Forma de pagamento: Cartão Tabajara')
else:
    print('Forma de pagamento: Outra')
print(f'Valor do desconto: R$ {valorDesconto:,.2f}')
print('-------------------------------------')
print(f'VALOR TOTAL A PAGAR: R$ {valorFinal:,.2f}')
print('-------------------------------------')
print('OBRIGADO E VOLTE SEMPRE')
