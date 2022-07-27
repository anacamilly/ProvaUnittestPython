# Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
# da função o id de uma turma (id_turma), indicar o número de alunos matriculados nela.

import unittest
from questao1 import alunosMatriculado

class numeroAlunosMatriculado(unittest.TestCase):
    def testAlunosMatriculado(self):
        list = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)]
        self.assertEqual(alunosMatriculado(1, list), 3)
        self.assertEqual(alunosMatriculado(2, list), 2)
