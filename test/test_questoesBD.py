from MockBD import *

from conexaoBD import *
from queries import *

#QUESTÕES COM BANCO DE DADOS
class TestDB(MockBD):
    # QUESTÃO 2
    def testListarAlunos(self):
        self.assertEqual(listarAlunos(self.mock_db_config.get('bd')),
                         [(1, 'Carla',), (2, 'Ana',), (3, 'Léo',), (4, 'Clara',), (5, 'João',), (6, 'Maria',),
                          (7, 'Leonardo',)])
    # QUESTÃO 3
    def testFiltrarTurmasGeografia(self):
        self.assertEqual(filtrarTurmasGeografia(self.mock_db_config.get('bd'), 1), [(1,),( 2,)])

    # QUESTÃO 4
    def testFiltrarAlunosCursamGeografia(self):
        self.assertEqual(filtrarAlunosCursamGeografia(self.mock_db_config.get('bd'), 1), [(1,)])
