#exercicio python 2 - Estrutura de Repetição
#https://wiki.python.org.br/EstruturaDeRepeticao

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
#uma mensagem de erro e voltando a pedir as informações

usuario = ''
password = ''
while (password == usuario):
    usuario = input('Informe seu nome do usuário: ')
    password = input('Informe sua senha: ')
    if (password == usuario):
        print('Password não pode ser igual ao nome do usuário')
    else:
        print('Usuário e senha cadastrados com sucesso')