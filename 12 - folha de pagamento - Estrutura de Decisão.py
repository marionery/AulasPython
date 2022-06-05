#exercicio python 12 - Estrutura de Decisão
#https://wiki.python.org.br/EstruturaDeDecisao

# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, como o exemplo abaixo:

# Salário Bruto: (5 * 220)        : R$ 1100,00
# (-) IR (5%)                     : R$   55,00
# (-) INSS ( 10%)                 : R$  110,00
# FGTS (11%)                      : R$  121,00
# Total de descontos              : R$  165,00
# Salário Liquido                 : R$  935,00

valor_hora = float(input('Informe o valor da hora de trabalho: R$ '))
horas_trabalhadas = int(input('Informe o número de horas trabalhadas: '))
salario_bruto =  (valor_hora * horas_trabalhadas)

desconto_IR = (salario_bruto * .05)
desconto_INSS = (salario_bruto * .10)
fgts = (salario_bruto * .11)
total_descontos = (desconto_IR + desconto_INSS)
salario_liquido = (salario_bruto - total_descontos)

print('-----------------------------')
print(f'Salário Bruto ({valor_hora:,.2f} x {horas_trabalhadas}):     R$ {salario_bruto:,.2f}')
print(f'(-)IR (5%):                     R$ {desconto_IR:,.2f}')
print(f'(-)INSS (10%):                  R$ {desconto_INSS:,.2f}')
print(f'FGTS (11%):                     R$ {fgts:,.2f}')
print(f'Total descontado:               R$ {total_descontos:,.2f}')
print(f'Salário Líquido:                R$ {salario_liquido:,.2f}')
print('-----------------------------')

