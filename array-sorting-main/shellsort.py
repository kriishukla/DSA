 #O(n)  O((n log(n)) ^ 2)  O((n log(n)) ^ 2)


def shell_sort(lista, n, inc, num):
    num-=1
    while(num >= 0):
        h = inc[num]
        hcnt = h
        while(hcnt < 2*h):
            j = hcnt
            while(j < n):
                tmp = lista[j]
                k = j
                while(k - h >= 0 and tmp < lista[k-h]):
                    lista[k] = lista[k - h]
                    k-=h
                lista[k] = tmp

                j+=h
            hcnt+=1


        num-=1
