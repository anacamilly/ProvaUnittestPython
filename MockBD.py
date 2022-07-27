import sqlite3
import sys
from unittest import TestCase

from conexaoBD import *

sys.path.insert(0, '..')

BD = "TestBD.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()

        # Turma: id (PK), nome, turno, id_disciplina (FK)
        # Disciplina: id (PK), nome
        # Aluno: id (PK), nome
        # Matricula: id (PK), id_aluno (FK), id_turma (FK)
        query_create_turma = """CREATE TABLE Turma(
        id int NOT NULL PRIMARY KEY ,
        nome text NOT NULL,
        turno text NOT NULL,
        id_disciplina int NOT NULL,
        FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
        )"""
        query_create_disciplina = """CREATE TABLE Disciplina(
                id int NOT NULL PRIMARY KEY ,
                nome text NOT NULL
                )"""
        query_create_aluno = """CREATE TABLE Aluno(
                        id int NOT NULL PRIMARY KEY ,
                        nome text NOT NULL
                        )"""
        query_create_matricula = """CREATE TABLE Matricula (
                        id int NOT NULL PRIMARY KEY,
                        id_aluno int NOT NULL,
                        id_turma int NOT NULL,
                        FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
                        FOREIGN KEY (id_turma) REFERENCES Turma(id)
                        )"""
        try:
            cursor.execute(query_create_aluno)
            cursor.execute(query_create_turma)
            cursor.execute(query_create_disciplina)
            cursor.execute(query_create_matricula)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_disciplina = """INSERT INTO Disciplina (id, nome)
                                VALUES
                                (1, 'Geografia'),
                                (2, 'Ingles'),
                                (3, 'Portugues'),
                                (4, 'Artes')
                                """

        query_insert_turma = """INSERT INTO Turma (id, nome, turno, id_disciplina)
                                VALUES
                                (1, 'turma1', 'manha', '1'),
                                (2, 'turma2', 'manha', '1'),
                                (3, 'turma3', 'tarde', '2'),
                                (4, 'turma4', 'tarde', '2')"""

        query_insert_aluno = """INSERT INTO Aluno (id, nome)
                                            VALUES
                                            (1, 'Carla'),
                                            (2, 'Ana'),
                                            (3, 'Léo'),
                                            (4, 'Clara'),
                                            (5, 'João'),
                                            (6, 'Maria'),
                                            (7, 'Leonardo')
                                            """

        query_insert_matricula = """INSERT INTO Matricula (id, id_aluno, id_turma)
                                                        VALUES
                                                        (1, 1, 1),
                                                        (2, 1, 3),
                                                        (3, 2, 2),
                                                        (4, 3, 2),
                                                        (5, 4, 4),
                                                        (6, 2, 3)
                                                        """

        try:
            cursor.execute(query_insert_aluno)
            cursor.execute(query_insert_disciplina)
            cursor.execute(query_insert_turma)
            cursor.execute(query_insert_matricula)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig = {
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE Matricula")
            cursor.execute("DROP TABLE Disciplina")
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Aluno")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)
