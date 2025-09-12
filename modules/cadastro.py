from modules.utils import Utils
import csv
import os

"""Classe responsável pelo cadastro de alunos e criação/atualização de arquivos CSV por disciplina."""
class Cadastro:
    @staticmethod
    def cadastrarAluno(nome, ra, turma, nota1, nota2, disciplina):
        """
        Cadastra um aluno, calcula a média, adiciona na fila e grava em CSV.
        Parâmetros:
        - nome, ra, turma → dados do aluno
        - nota1, nota2 → notas do aluno
        - disciplina → nome da disciplina para criar o CSV correspondente
        """

        # Calcula a média
        media = Utils.media(nota1, nota2)

        # Cria um dicionário do aluno
        aluno = {
            "Nome" : nome,
            "RA" : ra,
            "Turma" : turma,
            "Nota1" : nota1,
            "Nota2" : nota2,
            "Média" : media,
        }

        # Adiciona o aluno na fila
        Utils.filaAlunos.append(aluno)

        # Pasta onde os CSVs serão salvos
        pasta = r"C:\PIM\disciplinas"
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        # Nome do arquivo CSV da disciplina
        arquivoCsv = os.path.join(pasta, f"{disciplina}.csv")

        # Verifica se o arquivo existe
        fileExist = os.path.isfile(arquivoCsv)

        # Campos do CSV
        campos = ["Nome", "RA", "Turma", "Nota1", "Nota2", "Média",]

        # Abre o CSV no modo append ou cria se não existir
        with open (arquivoCsv, mode='a', newline = '', encoding = 'utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos)

            # Se o arquivo não existir, escreve o cabeçalho
            if not fileExist:
                writer.writeheader()
            
            # Escreve o aluno no CSV
            writer.writerow(aluno)