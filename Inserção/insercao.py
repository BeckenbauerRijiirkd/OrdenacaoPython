def insercao(array):
    for p in range (0, len(array)):
        while p > 0:
            if array[p - 1] > array[p]:
                array[p - 1], array[p] = array[p], array[p - 1]
            else:
                break
            p -=1
    print(array)

lista = [11,3,7,2,8,5,9,22,14,90,88]

insercao(lista)