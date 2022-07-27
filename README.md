# ATIVIDADE AVALIATIVA 4

#### TAD0203 GESTÃO DE QUALIDADE DE SOFTWARE - EAJ/UFRN

## OBJETIVO 🎯
  - Praticar o TDD (Test Driven Development)
  - Criar testes unitários a partir dos requisitos do sistema
 
## REQUISITOS DO SISTEMA ⚠
  - Utilizar a linguagem Python
  
## FUNCIONALIDADES DO SISTEMA 🛠
### Testes sem Banco de Dados:
1. Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
[[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
da função o id de uma turma (id_turma), indicar o número de alunos matriculados nela.
2. Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
[[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
da função o id do aluno (id_aluno), indicar os ids das turmas nas quais ele está matriculado.
3. Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
[[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Indicar a turma com o maior
número de alunos.
4. Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
[[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
da função o id de uma turma (id_turma), indicar se todos os alunos estão matriculados nela.

### Testes com Banco de Dados:
1. Listar o nome de todas as turmas que a aluna 'Carla' está matriculada
2. Listar todos os alunos da escola
3. Listar todas as turmas da disciplina 'Geografia'
4. Listas todos os alunos que cursam uma turma de 'Geografia'

### BANCO DE DADOS
1. Fazer um acesso ao banco de dados, criando as seguintes tabelas:
    - Turma: id (PK), nome, turno, id_disciplina (FK)
    - Disciplina: id (PK), nome
    - Aluno: id (PK), nome
    - Matricula: id (PK), id_aluno (FK), id_turma (FK)
2. Popular o banco de dados de teste:
    - Criar 4 turmas
        - Sendo 2 delas de 'Geografia'
    - Criar 4 disciplina
        - Sendo uma delas 'Geografia'
    - Criar 8 alunos
        - Sendo um deles 'Carla'
    - Criar várias matrículas
        - 'Carla' deve estar matriculada em 2 turmas
        
### ENTREGA
  - Escolher 3 testes de cada tipo para fazer.
  - Enviar um arquivo zipado com os seguintes arquivos (apenas um membro da dupla deve enviar o
documento):
    - Projeto com os testes e com os arquivos
    - Documento explicando a escolha dos casos de teste
