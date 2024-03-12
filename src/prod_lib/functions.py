def bubble_sort(lista: list, atributo: str):
    i = len(lista)

    while i > 0:
        flag = False
        for idx in range(len(lista) - 1):
            val1 = getattr(lista[idx], atributo.lower())
            val2 = getattr(lista[idx + 1], atributo.lower())

            if val1.isdigit():
                val1 = int(val1)
                val2 = int(val2)

            if val1 > val2:
                flag = True
                lista[idx], lista[idx + 1] = lista[idx + 1], lista[idx]
        if not flag:
            break
        i -= 1
    return lista


def merge_sort(lista: list, atributo: str):
    if len(lista) <= 1:
        return lista

    start, end = 0, len(lista)
    mid = len(lista) // 2

    esq = merge_sort(lista[start:mid], atributo)
    dir = merge_sort(lista[mid:end], atributo)
    return merge(esq, dir, atributo)


def merge(esq, dir, atributo: str):
    lista = []
    i, j = 0, 0
    if not esq:
        return dir
    if not dir:
        return esq

    while i < len(esq) and j < len(dir):

        val1 = getattr(esq[i], atributo.lower())
        val2 = getattr(dir[j], atributo.lower())

        if val1.isdigit():
            val1 = int(val1)
            val2 = int(val2)

        if val1 < val2:
            lista.append(esq[i])
            i += 1
        else:
            lista.append(dir[j])
            j += 1

    if i < len(esq):
        lista += esq[i:]
    if j < len(dir):
        lista += dir[j:]
    return lista


def busca_binária(lista: list, atributo):  # Add Valor
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


def busca_linear(lista: list, atributo: str, valor):
    """
    Função busca linear recebe lista e elemento buscado (x)
    e retorna 2 valores: (se encontrou ou não) e índice
    """
    for i, pessoa in enumerate(lista):
        if valor in getattr(pessoa, atributo.lower()):
            return True, i
    return False, -1


def idx(lista: list, atributo: int):
    try:
        idx = int(atributo)
        ret = lista[idx]
        return ret
    except Exception as e:
        print("\nErro: ", e)
