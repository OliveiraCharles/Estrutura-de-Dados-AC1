def executa(comando, atributo, lista):
    match comando:
        case "BUBBLESORT":
            bubble_sort(lista, atributo)

        case "MERGESORT":
            merge_sort(lista, atributo)

        case "BUSCABINARIA":
            busca_binária(lista, atributo)

        case "BUSCALINEAR":
            busca_linear(lista, atributo)

        case "IDX":
            idx(lista, atributo)


def bubble_sort(lista: list, atributo):
    i = len(lista)
    while i > 0:
        flag = False
        for idx, num in enumerate(lista):
            if idx+1 < len(lista) and lista[idx].nome > lista[idx+1].nome:
                flag = True
                lista[idx], lista[idx+1] = lista[idx+1], lista[idx]
        if not flag:
            break
        i = i-1
    return lista


def merge_sort(lista: list, atributo):
    if len(lista) <= 1:
        return lista

    start, end = 0, len(lista)
    mid = len(lista) // 2

    esq = merge_sort(lista[start:mid])
    dir = merge_sort(lista[mid:end])
    return merge(esq, dir)


def merge(esq, dir):
    lista = []
    i, j = 0, 0
    if not esq:
        return dir
    if not dir:
        return esq
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            lista.append(esq[i])
            i += 1
        else:
            lista.append(dir[j])
            j += 1
    if i < len(esq):
        lista += esq[i:]
    if j < len(dir):
        lista += dir[j:]

    for i, pessoa in enumerate(lista):
        print(pessoa.nome)

    return lista


def busca_binária(lista: list, atributo):
    """
    Função busca binaria recebe lista e elemento buscado (x)
    e retorna 2 valores: (se encontrou ou não) e índice
    """
    x = int(atributo)
    start = 0
    end = len(lista)
    mid = (end - start) // 2 + start

    while start != end:

        if lista[mid] == x:
            return True, mid
        else:
            if x > lista[mid]:
                start = mid + 1
            else:
                end = mid
            mid = (end - start) // 2 + start

    return False, -1


def busca_linear(lista: list, atributo):
    """
    Função busca linear recebe lista e elemento buscado (x)
    e retorna 2 valores: (se encontrou ou não) e índice
    """
    x = atributo
    for i, pessoa in enumerate(lista):
        p = [pessoa.nome, pessoa.idade, pessoa.profissão, pessoa.renda]
        if x in p:
            return True, i

    return False, -1


def idx(lista: list, atributo: int):
    idx = int(atributo) - 1
    try:
        ret = lista[idx]
        return ret
    except Exception as e:
        print("Erro: ", e)
