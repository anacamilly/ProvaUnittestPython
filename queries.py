from conexaoBD import *

# QUESTÃO 1
def listarTurmaCarlaMatriculada(bd, id_aluna):
    return ler_bd(bd, "SELECT t.nome FROM turma t, matricula m where m.id_turma = t.id and m.id_aluno=?", (id_aluna,))

# QUESTÃO 2
def listarAlunos(bd):
    return ler_bd(bd, "SELECT * FROM aluno")

# QUESTÃO 3
def filtrarTurmasGeografia(bd, id_disciplina):
    return ler_bd(bd, "SELECT id FROM turma where id_disciplina=?", (id_disciplina,))

# QUESTÃO 4 Listas todos os alunos que cursam uma turma de 'Geografia'
def filtrarAlunosCursamGeografia(bd, id_turma):
    return ler_bd(bd, "SELECT id_aluno FROM matricula where id_turma=?", (id_turma,))
