def alunosMatriculados(id_turma, dados):
	resultado1 = 0
	resultado2 = 0
	for i in range(len(dados)):
		if id_turma == dados[i][0]:
			resultado1 = resultado1 + 1
		else:
			resultado2 = resultado2 + 1
	if resultado1 > 0 and resultado2 == 0:
		return (True)
	else:
		return (False)