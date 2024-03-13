from config import settings as st
from prod_lib import functions as fc
from prod_lib.pessoa import Pessoa


def show(pessoas: Pessoa, atributo: str):
    print('\nidx\t|', atributo)
    print(20 * '-')
    for idx, pessoa in enumerate(pessoas):
        print(idx, '\t|', getattr(pessoa, atributo.lower()))


def main(arquivo='./entrada.txt'):

    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        pessoas = []
        for linha in linhas:
            linha = linha.replace('\n', '').strip()
            print('\n>>', linha)

            if '=' in linha:
                comando, atributo = linha.split('=')
                comando = comando.strip()
                atributo = atributo.strip()

                if comando in st.comandos:

                    match comando:
                        case 'BUBBLESORT':
                            pessoas = fc.bubble_sort(pessoas, atributo)
                            show(pessoas, atributo)

                        case 'MERGESORT':
                            pessoas = fc.merge_sort(pessoas, atributo)
                            show(pessoas, atributo)

                        case 'BUSCABINARIA':
                            atributo, valor = atributo.split(';')
                            atributo = atributo.strip()
                            valor = valor.strip()
                            rt = fc.busca_binária(pessoas, atributo, valor)
                            print(rt)

                        case 'BUSCALINEAR':
                            atributo, valor = atributo.split(';')
                            atributo = atributo.strip()
                            valor = valor.strip()
                            rt = fc.busca_linear(pessoas, atributo, valor)
                            print(rt)

                        case 'IDX':
                            rt = fc.idx(pessoas, atributo)
                            print(rt)

            else:
                nome, idade, profissão, renda = linha.split(';')
                nome = nome.strip()
                idade = idade.strip()
                profissão = profissão.strip()
                renda = renda.strip()

                pessoas.append(Pessoa(nome, idade, profissão, renda))


main(st.arquivo)
