def alunosMatriculados(id_turma, dados):
	resultado = []
	for i in range(len(dados)):
		if id_turma == dados[i][0]:
			resultado = True
		else:
			resultado = False
	return (resultado)