# Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Indicar a turma com o maior
# número de alunos.

import unittest
from questao3 import todosalunosMatriculados

class TodosAlunosMatriculados(unittest.TestCase):
    def testAlunosMatric(self):
        listTurmaAlunos1 = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)]
        listTurmaAlunos2 = [(1, 1), (1, 2), (2, 3), (2, 1), (2, 4)]
        self.assertEqual(todosalunosMatriculados(listTurmaAlunos1), 1)
        self.assertEqual(todosalunosMatriculados(listTurmaAlunos2), 2)

