#exercicio python 3 - Estrutura de Repetição
#https://wiki.python.org.br/EstruturaDeRepeticao

# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = ''
while (len(nome) < 3):
    nome = input('Informe o nome: ')
    if (len(nome) <= 3):
        print('Nome deve ser maior do que 3 caracteres')

idade = -1
while (idade < 0) or (idade > 150):
    idade = int(input('Informe a idade: '))
    if (idade < 0) or (idade > 150):
        print('Informe uma idade entre 0 e 150 anos.')

salario = -1
while (salario <= 0):
    salario = int(input('Informe o salário: '))
    if (salario <= 0):
        print('O salário deve ser maior do que 0.')

sexo = ''
while (sexo != 'F') and (sexo != 'M'):
    sexo = input('Informe o sexo (F - feminino / M - masculino): ').upper()
    if (sexo != 'F') and (sexo != 'M'):
        print('Sexo deve ser F para Feminino ou M para Masculino')

est_civil = ''
while (est_civil != 'S') and (est_civil != 'V') and (est_civil != 'C') and (est_civil != 'D'):
    est_civil = input('Informe o estado civil: ').upper()
    if (est_civil != 'S') and (est_civil != 'V') and (est_civil != 'C') and (est_civil != 'D'):
        print('Informe o estado civil: S - solteiro / V - viúvo / C - casado / D - divorciado.')