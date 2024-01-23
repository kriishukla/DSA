#O(n log(n)) O(n log(n)) O(n^2)


def partition(lista, esq, dir, pivot):
    while(esq <= dir):
        while(lista[esq] < pivot):
            esq+=1

        while(lista[dir] > pivot):
            dir-=1

        if(esq <= dir):
            lista[esq], lista[dir] = lista[dir], lista[esq] # Swap
            esq+=1
            dir-=1

    return esq

def quick_sort(lista, esq, dir):
    if(esq >= dir):
        return
    pivot = lista[ (esq + dir) / 2]
    index = partition(lista, esq, dir, pivot)
    quick_sort(lista, esq, index-1)
    quick_sort(lista, index, dir)

