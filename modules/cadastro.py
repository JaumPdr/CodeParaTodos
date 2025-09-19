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
        try:
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

        except Exception as e:
            print(f"❌  Erro ao salvar Aluno: {e}")

    @staticmethod
    def salvarUsuario(usuario, senha, arquivo=r"C:\PIM\usuario\usuario.csv"):
        """Salva o usuário e senha em CSV com cabeçalho, sem duplicatas."""
        try:
            # Cria a pasta se não existir
            os.makedirs(os.path.dirname(arquivo), exist_ok=True)

            # Verifica se o arquivo já existe
            arquivoExiste = os.path.isfile(arquivo)

            # Lê usuários existentes
            usuarioExistente = set()
            if arquivoExiste:
                with open(arquivo, mode="r", newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        usuarioExistente.add(row['Login'].lower())

            # Adiciona apenas se não existir
            if usuario.lower() not in usuarioExistente:
                with open(arquivo, mode="a", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=["Login", "Senha"])
                    # Escreve cabeçalho se arquivo não existia
                    if not arquivoExiste:
                        writer.writeheader()
                    writer.writerow({"Login": usuario, "Senha": senha})

        except Exception as e:
            print(f"❌  Erro ao salvar usuário: {e}")