def primo(n):	
	#n = int(input("Escreva o seu número: "))
	p = []
	for i in range(1,n+1):
		if (n)%i==0:
			p.append(i)
	if len(p)==2:
		print("O número {} é primo".format(p[1]))
	else:
		print("O número {} não é primo ".format(n))
