#Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
#[[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
#da função o id de uma turma (id_turma), indicar se todos os alunos estão matriculados nela

import unittest
from questao4 import alunosMatriculados

class TodosAlunosMatric(unittest.TestCase):
	def testAlunosMatriculados(self):
		list = [(1, 1), (1 ,2), (1, 3), (2, 1), (2, 4)]
		self.assertEqual(alunosMatriculados(1, list), (False))
