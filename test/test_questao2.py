# Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
# da função o id do aluno (id_aluno), indicar os ids das turmas nas quais ele está matriculado.

import unittest
from questao2 import turmasMatriculadas

class idTurmaMatriculadas(unittest.TestCase):
    def testTrumaMatriculada(self):
        list = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)]
        self.assertEqual(turmasMatriculadas(1, list), [[1], [2]])
        self.assertEqual(turmasMatriculadas(2, list), [[1]])
        self.assertEqual(turmasMatriculadas(3, list), [[1]])
        self.assertEqual(turmasMatriculadas(4, list), [[2]])
