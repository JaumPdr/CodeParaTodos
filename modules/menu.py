from modules.utils import Utils
from modules.cadastro import Cadastro
import time
import getpass
import re

"""Classe que gerencia todos os menus do CodeParaTodos, incluindo apresentação, login e menus de disciplinas."""
class Menu:
    """
    Exibe a apresentação do CodeParaTodos com informações sobre funcionalidades
    e uma mensagem de boas-vindas ao professor.
    """
    @staticmethod
    def apresentacao():
        print("🔹" * 30)
        Utils.formatarTexto("\n            🎓  BEM-VINDO AO CodeParaTodos  🎓\n", velocidade=0.04)
        print("🔹" * 30)
        Utils.formatarTexto("\n  Um sistema acadêmico simples e eficiente, desenvolvido", velocidade=0.04)
        Utils.formatarTexto("  para auxiliar professores na gestão de alunos.\n", velocidade=0.04)
        print("🔻" * 30)
        Utils.formatarTexto("  Funcionalidades principais:", velocidade=0.04)
        Utils.formatarTexto("  1) Menu com disciplinas disponíveis", velocidade=0.04)
        Utils.formatarTexto("  2) Cadastro de alunos por disciplina", velocidade=0.04)
        Utils.formatarTexto("  3) Registro de notas e cálculo automático da média", velocidade=0.04)
        Utils.formatarTexto("  4) Geração de arquivo CSV com os dados dos alunos", velocidade=0.04)
        print("🔺" * 30)
        Utils.formatarTexto("\n  Projeto acadêmico desenvolvido com foco em praticidade", velocidade=0.04)
        Utils.formatarTexto("  e inovação no ensino. 🚀\n", velocidade=0.04)
        print("🔹" * 30)
        print()

    @staticmethod
    def login():
        """Solicita usuário e senha para acessar o CodeParaTodos."""
        usuario = "professor"
        senha = "123456"

        # Salva o usuário no CSV
        Cadastro.salvarUsuario(usuario, senha)

        Utils.formatarTexto("👉 Para acessar o CodeParaTodos, faça seu login abaixo:\n", velocidade=0.04)
        while True:
            print("             👤")
            usuarioInserido = input("          Usuário: ").strip().lower()
            senhaInserida = getpass.getpass("          Senha: ").strip()

            if usuarioInserido == usuario and senhaInserida == senha:
                Utils.formatarTexto(f"\n✅ Acesso concedido! Bem-vindo(a) ao CodeParaTodos, {usuario}.", velocidade=0.04)
                break
            else:
                print("\n❌ Usuário ou senha incorretos. Tente novamente!\n")

    @staticmethod
    def despedida():
        """Exibe mensagem de saída e encerra o programa."""
        Utils.formatarTexto("\nSaindo do Sistema...🔄", velocidade=0.05)
        time.sleep(1)
        print("\n" + "🔹" * 30)
        Utils.formatarTexto("\n    👋 Até logo! Obrigado por usar o CodeParaTodos. 🎓\n", velocidade=0.04)
        print("🔹" * 30)
        time.sleep(1.5)
        exit()

    @staticmethod
    def menuPrincipal():
        """Menu principal do CodeParaTodos que direciona para o menu de disciplinas ou encerra o sistema."""
        while True:
           Utils.formatarTexto("   \n⬇️   Escolha uma das opções abaixo ⬇️\n", velocidade=0.04)
           print("           (1) Menu ☰")
           print("           (0) Sair 🛑")
           
           escolhaMenuPrincipal = input("\nDigite a opção desejada: ").strip().lower()

           if escolhaMenuPrincipal in ["1", "menu"]:
               Utils.formatarTexto("\nAcessando Menu...🔄", velocidade=0.05)
               time.sleep(1)
               print()
               Menu.menuDisciplinas()

           elif escolhaMenuPrincipal in ["0", "sair"]:
               Menu.despedida()
           else:
               Utils.formatarTexto("\n⚠️  Opção inválida! Tente novamente.", velocidade=0.03)

    @staticmethod
    def menuDisciplinas():
        """
        Menu com a lista de disciplinas. 
        Permite escolher uma disciplina para entrar no menu interno ou voltar ao menu principal.
        """
        disciplinas = ["Voltar ao menu principal", "Pensamento lógico computacional", "Segurança digital", "Programação em Python"]

        while True:
            print("🔹" * 19)
            Utils.formatarTexto("\n        📚 MENU DE DISCIPLINAS\n", velocidade=0.04)
            print("🔹" * 19)
            print("\n")
            for i, disciplina in enumerate(disciplinas, start=1):
                print(f"     ({i}) {disciplina}")
                time.sleep(0.02)
            print("     (0) Sair 🛑")

            escolhaDisciplina = input("\nDigite a opção desejada: ").strip().lower()

            if escolhaDisciplina in ["0", "sair"]:
                Menu.despedida()
            elif escolhaDisciplina in ["1", "voltar", "Voltar ao menu principal\n"]:
                print("🔹" * 19)
                break
            elif escolhaDisciplina in [str(i) for i in range(1, len(disciplinas)+1)]:
                idx = int(escolhaDisciplina) - 1
                disciplinaEscolhida = disciplinas[idx]     
                Menu.menuDaDisciplinaEscolhida(disciplinaEscolhida)
            else:
                Utils.formatarTexto("\n⚠️  Opção inválida! Tente novamente.\n", velocidade=0.03)

    
    @staticmethod
    def menuDaDisciplinaEscolhida(disciplina):
        """
        Menu interno de cada disciplina. Permite:
        1) Cadastrar aluno
        2) Voltar ao menu de disciplinas
        3) Sair do sistema
        """
        while True:
            print("\n" + "🔹" * 24)
            Utils.formatarTexto(f"\n🎓 DISCIPLINA: {disciplina}\n", velocidade=0.03)
            Utils.formatarTexto(f"✨ Bem-vindo ao menu da disciplina! ✨", velocidade=0.03)
            print("\n" + "🔹" * 24)
            Utils.formatarTexto("\nEscolha uma opção abaixo para continuar: \n", velocidade=0.03)
            print("        (1) Cadastrar aluno 📝")
            time.sleep(0.03)
            print("        (2) Voltar ao menu de disciplinas 🔙")
            time.sleep(0.03)
            print("        (0) Sair 🛑\n")
            time.sleep(0.03)
            opcao = input("\nEscolha uma opção: ").strip().lower()
            print("\n")
            if opcao in ["1", "cadastrar"]:
                Menu.solicitarDados(disciplina)
            elif opcao in ["2", "voltar"]:
                break
            elif opcao in ["0", "sair"]:
                Menu.despedida()
            else:
                Utils.formatarTexto("\n⚠️  Opção inválida. Tente novamente.\n", velocidade=0.03)

    @staticmethod
    def solicitarDados(disciplina):
        """
        Solicita dados do aluno e registra no CSV.
        Verifica:
        - Campos obrigatórios preenchidos
        - Notas válidas (0 a 10)
        """

        maxNome = 60  # limite de caracteres

        Utils.formatarTexto("\nDigite os dados do aluno:", velocidade=0.04)
        
         # Solicita e valida campos obrigatórios
        while True:
            nome = input("👤  Nome: ").strip().upper()
            # Verifica se o nome contém apenas letras e espaços
            if re.search(r"\d", nome):
                Utils.formatarTexto("\n⚠️  O nome deve conter apenas letras. Tente novamente.\n", velocidade=0.03)
                continue  # volta para pedir de novo

            # Verifica o tamanho do nome
            if len(nome) > maxNome:
                Utils.formatarTexto(f"\n⚠️  O nome não pode ter mais que {maxNome} caracteres!\n", velocidade=0.03)
                continue

            ra = input("🆔  RA: ").strip().upper()
            turma = input("🏫  Turma: ").strip().upper()

            if nome and ra and turma:
                break
            else:
                Utils.formatarTexto("\n⚠️  Todos os campos devem ser preenchidos. Tente novamente.\n", velocidade=0.03)

        while True:
            try:
                nota1_str = input("📊 Nota 1: ").strip()
                nota2_str = input("📊 Nota 2: ").strip()

                # Regex: número inteiro ou decimal com ponto ou vírgula, até 2 casas decimais, sem negativos
                padrao = r'^\d+([.,]\d{1,2})?$'

                # Verifica formato
                if not (re.match(padrao, nota1_str) and re.match(padrao, nota2_str)):
                    Utils.formatarTexto("\n⚠️  Digite as notas corretamente (0 a 10) e com no máximo 2 casas decimais.\n",velocidade=0.03)
                    continue

                # Converte vírgula para ponto
                nota1 = float(nota1_str.replace(',', '.'))
                nota2 = float(nota2_str.replace(',', '.'))

                # Verifica intervalo válido
                if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
                    Utils.formatarTexto("\n⚠️  As notas devem estar entre 0 e 10.\n",velocidade=0.03)
                    continue

                # Se chegou aqui, está tudo certo
                break
            except ValueError:
                Utils.formatarTexto("\n⚠️  Por favor, digite um número válido para as notas.", velocidade=0.03)

        # Pergunta se deseja salvar
        while True:
            resposta = input("\nDeseja salvar 💾 o aluno? (s/n): ").strip().lower()
            if resposta in ["s", "sim"]:
                aluno = Cadastro.cadastrarAluno(nome, ra, turma, nota1, nota2, disciplina)
                Utils.formatarTexto(f"\n✅  Aluno {nome} cadastrado com sucesso na disciplina {disciplina}!", velocidade=0.04)
                break  # sai do loop
            elif resposta in ["n", "não", "nao"]:
                Utils.formatarTexto("\n🚫  Aluno não cadastrado!", velocidade=0.03)
                break  # sai do loop e volta ao menu
            else:
                Utils.formatarTexto("\n⚠️  Opção inválida. Digite 's' para sim ou 'n' para não.", velocidade=0.03)

