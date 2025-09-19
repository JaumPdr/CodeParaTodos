import sys
import time
from collections import deque

"""Classe responsável pela formatação de texto e cálculo da méida"""
class Utils:

    filaAlunos = deque()

    @staticmethod
    def formatarTexto(texto, velocidade):
        """
        Exibe o texto no console como se estivesse sendo digitado.
        Cada caractere aparece com um pequeno atraso definido por 'velocidade'.
        """
        for letra in texto:
            sys.stdout.write(letra) # escreve cada letra sem pular linha
            sys.stdout.flush() # garante que a letra apareça imediatamente
            time.sleep(velocidade) # pausa para efeito de digitação
        print() # adiciona quebra de linha no final

    @staticmethod
    def media(nota1, nota2):
        """
        Calcula a média simples entre duas notas.
        Retorna o valor numérico da média com 2 casas decimais.
        """
        return round((nota1 + nota2) / 2, 2)
