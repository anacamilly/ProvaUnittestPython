from MockBD import *

from conexaoBD import *
from queries import *

#QUESTÕES COM BANCO DE DADOS
class TestDB(MockBD):

    # QUESTÃO 1 - Listar o nome de todas as turmas que a aluna 'Carla' está matriculada
    def testListarTurmaCarlaMatriculada(self):
        self.assertEqual(listarTurmaCarlaMatriculada(self.mock_db_config.get('bd'), 1), [('turma1',), ('turma3',)])

    # QUESTÃO 2 - Listar todos os alunos da escola
    def testListarAlunos(self):
        self.assertEqual(listarAlunos(self.mock_db_config.get('bd')),
                         [(1, 'Carla',), (2, 'Ana',), (3, 'Léo',), (4, 'Clara',), (5, 'João',), (6, 'Maria',),
                          (7, 'Leonardo',)])

    # QUESTÃO 3 - Listar todas as turmas da disciplina 'Geografia'
    def testFiltrarTurmasGeografia(self):
        self.assertEqual(filtrarTurmasGeografia(self.mock_db_config.get('bd'), 1), [(1,),( 2,)])

    # QUESTÃO 4 - Listas todos os alunos que cursam uma turma de 'Geografia'
    def testFiltrarAlunosCursamGeografia(self):
        self.assertEqual(filtrarAlunosCursamGeografia(self.mock_db_config.get('bd'), 1), [(1,)])
