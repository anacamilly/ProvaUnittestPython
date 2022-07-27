from conexaoBD import *

# QUESTÃO 2
def listarAlunos(bd):
    return ler_bd(bd, "SELECT * FROM aluno")

# QUESTÃO 3
def filtrarTurmasGeografia(bd, id_disciplina):
    return ler_bd(bd, "SELECT id FROM turma where id_disciplina=?", (id_disciplina,))

# QUESTÃO 4
def filtrarAlunosCursamGeografia(bd, id_matricula):
    return ler_bd(bd, "SELECT id_aluno FROM matricula where id=?", (id_matricula,))
