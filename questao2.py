def turmasMatriculadas(id_aluno, dados):
	resultado = []
	for i in range(len(dados)):
		if id_aluno == dados[i][1]:
			resultado.append([dados[i][0]])
	return resultado