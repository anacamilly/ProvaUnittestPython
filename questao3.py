def todosalunosMatriculados(dados):
	resultado1 = []
	resultado2 = []
	a = 0
	b = 0
	for i in range(len(dados)):
		if dados[1][0] == dados[i][0]:
			resultado1 = dados[i][0]
			a = a + 1
		else:
			resultado2 = dados[i][0]
			b = b + 1
	if a > b:
		print('A turma de id =', resultado1, 'é a maior')
		return(resultado1)
	else:
		print('A turma de id =', resultado2, 'é a maior')
		return (resultado2)