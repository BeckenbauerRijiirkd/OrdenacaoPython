def bubble(vetor):
    aux = 0 
    for i in range (0, (len(vetor)-1)): #PRIMEIRO LAÇO PERCORRENDO TOD O VETOR
        for j in range (0, (len(vetor)-1)): #LAÇO INTERNO DA TROCA OU NAO DE POSIÇÕES.
            if vetor[j] > vetor[j+1]: #CONDIÇÃO PARA TROCA DE POSIÇÃO.
                aux = vetor[j+1] #VARIAVEL AUXILIAR ARMAZENA O ELEMENTO POSTERIOR, IDENTIFICADO COMO MENOR.
                vetor[j+1] = vetor[j] #ELEMENTO POSTERIOR RECEBE O ELEMENTO ANTERIOR. 
                vetor[j] = aux # ELEMENTO ANTERIOR RECEBE O VALOR DA VARIAVEL AUXILIAR
    print(vetor)

lista = [10,4,7,3,2,1]

bubble(lista)