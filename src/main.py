from prod_lib import functions as fc
from prod_lib.pessoa import Pessoa
from config import settings as st


def main(arquivo='./entrada.txt'):

    with open(arquivo, 'r', encoding="utf-8") as f:
        linhas = f.readlines()
        pessoas = []
        for linha in linhas:
            linha = linha.replace("\n", "").strip()
            print("\n>>", linha)

            if '=' in linha:
                comando, atributo = linha.split('=')

                if comando in st.comandos:

                    match comando:
                        case "BUBBLESORT":
                            pessoas = fc.bubble_sort(pessoas, atributo)
                            print(pessoas[0])
                        case "MERGESORT":
                            pessoas = fc.merge_sort(pessoas, atributo)
                            print(pessoas[0])

                        case "BUSCABINARIA":
                            rt = fc.busca_binária(pessoas, atributo)
                            print(rt)

                        case "BUSCALINEAR":
                            atributo, valor = atributo.split(';')
                            atributo = atributo.strip()
                            valor = valor.strip()
                            rt = fc.busca_linear(pessoas, atributo, valor)
                            print(rt)

                        case "IDX":
                            rt = fc.idx(pessoas, atributo)
                            print(rt)

            else:
                nome, idade, profissão, renda = linha.split(';')
                pessoas.append(Pessoa(nome, idade, profissão, renda))


main(st.arquivo)
