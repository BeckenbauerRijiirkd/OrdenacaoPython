def bubble(vetor):
    aux = 0 #VARIAVEL AUXILIAR PARA ARMAZENAGEM DO ELEMENTO TEMPORARIAMENTE
    cont = 0 #VARIAVEL CONTADORA DE VERIFICAÇÕES
    for i in range (0, (len(vetor)-1)): #PRIMEIRO LAÇO PERCORRENDO TOD O VETOR
        for j in range (0, ((len(vetor)-1)-i)): #LAÇO INTERNO DA TROCA OU NAO DE POSIÇÕES.

            #APRIMORAMENTO DO ALGORITMO, SUBTRAÇÃO DA QUANTIDADE DE PASSAGENS FEITA PELO PRIMEIRO LAÇO
            #REDUZINDO ASSIM O TOTAL DE VERIFICAÇÕES JA REALIZADAS.
            
            if vetor[j] > vetor[j+1]: #CONDIÇÃO PARA TROCA DE POSIÇÃO.
                aux = vetor[j+1] #VARIAVEL AUXILIAR ARMAZENA O ELEMENTO POSTERIOR, IDENTIFICADO COMO MENOR.
                vetor[j+1] = vetor[j] #ELEMENTO POSTERIOR RECEBE O ELEMENTO ANTERIOR. 
                vetor[j] = aux # ELEMENTO ANTERIOR RECEBE O VALOR DA VARIAVEL AUXILIAR
                print(vetor[j+1], "TROCOU COM: ", vetor[j])
            else:
                print(vetor[j], "NÃO TROCOU COM: ", vetor[j+1])
            cont = cont + 1
            print(vetor,"\n")

    print("VETOR ORDENADO: ", vetor,"\nTOTAL DE VERIFICAÇÕES: ",cont  )