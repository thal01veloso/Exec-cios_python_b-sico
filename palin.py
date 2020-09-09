# Author: Thales veloso/thal01veloso@gmail.com
#https://www.youtube.com/user/tthhal01/
#Descrição
#Esse programa é um verificador de palindromo
#O usuário digita uma frase e a frase é escrita de 
#trás para frente
#=========================================================
o = "1"
b = []
s = ''
while o == "1":
	a = input("Digite uma frase para analisar:\n ").lower()
	tm = len(a)
	for i in range(tm):
		b.append(a[tm-1-i])
	b = s.join(b)
	print(b)
	if b == a:
		print('A frase é um palindromo: ')
	else:
		print('A Frase não é um palindromo')
	o = input(""" Escolha uma opção abaixo:
[1] Continuar
[2] Sair 
.
.
.
""")

