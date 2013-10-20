__author__ = 'Carol'


class Carrega_arq:

    @classmethod
    def carrega_arquivo(cls):
        linhas = []
        arquivo = open('movies.txt', 'r')
        arq = arquivo.readlines()
        for linha in arq:
            linha = linha.split(';')
            linha.reverse()
            linha.pop()
            linha[0] = linha[0].strip()
            linhas.append(linha)
        return linhas
