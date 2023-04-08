#exercicio python 1 - Estrutura de Repetição
#https://wiki.python.org.br/EstruturaDeRepeticao

#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.

nota = int(input('Informe uma nota:'))
while (nota < 0) or (nota > 10):
    print('nota inválida')
    nota = int(input('Informe uma nota:'))
else:
    print('Nota válida:', nota)


<<<<<<< HEAD
#OUTRA SAIDA
=======
#OUTRA POSSIBILIDADE
>>>>>>> 08973cad2c0475b8edb1e6142aac261255296a1d

# nota = -1
# while (nota < 0) or (nota > 10):
#     nota = int(input('Informe uma nota:'))
#     if (nota < 0) or (nota > 10):
#         print('Nota Inválida')
#     else:
#         print('Nota válida:', nota)