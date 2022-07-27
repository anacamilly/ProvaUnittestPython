def alunosMatriculados(id_turma, dados):
	resultado = []
	for i in range(len(dados)):
		if id_turma == dados[i][0]:
			resultado.append([dados[i][1]])
	print('Ids de alunos matriculados:')
	print(resultado)
	print('Nem todos os alunos estão cadastrados nessa turma.')
	return resultado