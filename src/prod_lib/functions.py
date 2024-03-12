def bubble_sort(lista: list, atributo: str):
    i = len(lista)

    while i > 0:
        flag = False
        for idx in range(len(lista) - 1):
            # usando getattr para acessar o valor dos atributos dinamicamente
            if (getattr(lista[idx], atributo.lower())
                    > getattr(lista[idx + 1], atributo.lower())):
                flag = True
                lista[idx], lista[idx + 1] = lista[idx + 1], lista[idx]
        if not flag:
            break
        i -= 1
    return lista

    # match atributo:

    #     case "Nome":
    #         while i > 0:
    #             flag = False
    #             for idx, num in enumerate(lista):
    #                 if idx+1 < len(lista) and lista[idx].nome > lista[idx+1].nome:
    #                     flag = True
    #                     lista[idx], lista[idx+1] = lista[idx+1], lista[idx]
    #             if not flag:
    #                 break
    #             i = i-1
    #         return lista

    #     case "Idade":
    #         while i > 0:
    #             flag = False
    #             for idx, num in enumerate(lista):
    #                 if idx+1 < len(lista) and lista[idx].idade > lista[idx+1].idade:
    #                     flag = True
    #                     lista[idx], lista[idx+1] = lista[idx+1], lista[idx]
    #             if not flag:
    #                 break
    #             i = i-1
    #         return lista

    #     case "Profissão":
    #         while i > 0:
    #             flag = False
    #             for idx, num in enumerate(lista):
    #                 if idx+1 < len(lista) and lista[idx].profissão > lista[idx+1].profissão:
    #                     flag = True
    #                     lista[idx], lista[idx+1] = lista[idx+1], lista[idx]
    #             if not flag:
    #                 break
    #             i = i-1
    #         return lista

    #     case "Renda":
    #         while i > 0:
    #             flag = False
    #             for idx, num in enumerate(lista):
    #                 if idx+1 < len(lista) and lista[idx].renda > lista[idx+1].renda:
    #                     flag = True
    #                     lista[idx], lista[idx+1] = lista[idx+1], lista[idx]
    #             if not flag:
    #                 break
    #             i = i-1
    #         return lista


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
        if (getattr(esq[i], atributo.lower())
                < getattr(dir[j], atributo.lower())):
            lista.append(esq[i])
            i += 1
        else:
            lista.append(dir[j])
            j += 1

    # match atributo:
    #     case "Nome":
    #         while i < len(esq) and j < len(dir):
    #             if esq[i].nome < dir[j].nome:
    #                 lista.append(esq[i])
    #                 i += 1
    #             else:
    #                 lista.append(dir[j])
    #                 j += 1
    #     case "Idade":
    #         while i < len(esq) and j < len(dir):
    #             if esq[i].idade < dir[j].idade:
    #                 lista.append(esq[i])
    #                 i += 1
    #             else:
    #                 lista.append(dir[j])
    #                 j += 1
    #     case "Profissão":
    #         while i < len(esq) and j < len(dir):
    #             if esq[i].profissão < dir[j].profissão:
    #                 lista.append(esq[i])
    #                 i += 1
    #             else:
    #                 lista.append(dir[j])
    #                 j += 1
    #     case "Renda":
    #         while i < len(esq) and j < len(dir):
    #             if esq[i].renda < dir[j].renda:
    #                 lista.append(esq[i])
    #                 i += 1
    #             else:
    #                 lista.append(dir[j])
    #                 j += 1

    if i < len(esq):
        lista += esq[i:]
    if j < len(dir):
        lista += dir[j:]

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


def busca_linear(lista: list, atributo: str, valor):
    """
    Função busca linear recebe lista e elemento buscado (x)
    e retorna 2 valores: (se encontrou ou não) e índice
    """
    for i, pessoa in enumerate(lista):
        if valor in getattr(pessoa, atributo.lower()):
            return True, i
    return False, -1

    # match atributo:
    #     case "Nome":
    #         for i, pessoa in enumerate(lista):
    #             if valor in pessoa.nome:
    #                 return True, i
    #         return False, -1

    #     case "Idade":
    #         for i, pessoa in enumerate(lista):
    #             if valor in pessoa.idade:
    #                 return True, i
    #         return False, -1

    #     case "Profissão":
    #         for i, pessoa in enumerate(lista):
    #             if valor in pessoa.profissão:
    #                 return True, i
    #         return False, -1

    #     case "Renda":
    #         for i, pessoa in enumerate(lista):
    #             if valor in pessoa.renda:
    #                 return True, i
    #         return False, -1


def idx(lista: list, atributo: int):
    idx = int(atributo)
    try:
        ret = lista[idx]
        return ret
    except Exception as e:
        print("Erro: ", e)
