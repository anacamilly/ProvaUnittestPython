def alunosMatriculado(id_turma, dados):
	resultado = 0
	for i in range(len(dados)):
		if id_turma == dados[i][0]:
			resultado = resultado + 1
	print(resultado)
	return resultado

