def alunosMatriculado(id_turma, dados):
	resultado = 0
	for i in range(len(dados)):
		if id_turma == dados[i][0]:
			resultado = resultado + 1
	print('O número de alunos matriculados na turma de id =', id_turma, 'é:', resultado)
	return resultado

