#exercicio python 25 - Estrutura de Decisão
#https://wiki.python.org.br/EstruturaDeDecisao

# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

telefonou = input('Telefonou para a vítima? Sim (S) ou Não (N)? ').upper()
local = input('Esteve no local do crime? Sim (S) ou Não (N)? ').upper()
mora = input('Mora perto da vítima? Sim (S) ou Não (N)? ').upper()
devia = input('Devia algum dinheiro para vítima? Sim (S) ou Não (N)? ').upper()
trabalhou = input('Já trabalhou para vítima? Sim (S) ou Não (N)? ').upper()

respostas = [telefonou, local, mora, devia, trabalhou]

sim = []
for resposta in respostas:
    if resposta == 'S':
        sim.append(resposta)

if len(sim) == 2:
    status = 'Suspeito'
elif len(sim) == 3 or len(sim) == 4:
    status = 'Cúmplice'
elif len(sim) == 5:
    status = 'Assassino'
else:
    status = 'Inocente'

print('-----------------------------')
print('As respostas foram:', respostas)
print('Essa pessoa é:', status)
print('-----------------------------')

