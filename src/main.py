from prod_lib import functions as fc
from prod_lib.pessoa import Pessoa
from config import settings as st


def main(arquivo='./entrada.txt'):

    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        pessoas = []
        for linha in linhas:
            linha = linha.replace("\n", "").strip()
            print(">>", linha)

            if '=' in linha:
                comando, atributo = linha.split('=')

                if comando in st.comandos:

                    match comando:
                        case "BUBBLESORT":
                            rt = fc.bubble_sort(pessoas, atributo)
                            print(rt)
                        case "MERGESORT":
                            fc.merge_sort(pessoas, atributo)

                        case "BUSCABINARIA":
                            fc.busca_binária(pessoas, atributo)

                        case "BUSCALINEAR":
                            fc.busca_linear(pessoas, atributo)

                        case "IDX":
                            fc.idx(pessoas, atributo)

            else:
                nome, idade, profissão, renda = linha.split(';')
                pessoas.append(Pessoa(nome, idade, profissão, renda))


main(st.arquivo)
