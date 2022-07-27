def turmasMatriculadas(id_aluno, dados):
	resultado = []
	for i in range(len(dados)):
		if id_aluno == dados[i][1]:
			resultado.append([dados[i][0]])
	print('O aluno de id =', id_aluno, 'está matriculado nas seguintes máterias:', resultado)
	return resultado