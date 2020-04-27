class Heap:
    """Classe que cria um heap de minimo a partir de uma lista.
    Essa classe busca encapsular o uso de um heap de minimo oferecendo métodos de
    push() com custo assintótico de O(log(n)) e pop() com o mesmo custo,
    o custo de criação do heap a partir de uma lista é de O(n).
    Além disso oferece uma função de ordenação com custo O(n*log(n)).
    Onde "n" é o numero de elementos no heap
    Para a representação do Heap em forma de lista seguimos a seguinte regra:
        O pai de um elemento na posição "i" é dado por: ((i - 1) // 2)
        O filho a esquerda(fe) é:  i * 2 + 1
        o filho a direita(fd): fe + 1
    TODO: Implementar Heap de máximo
    """

    def __init__(self, lista: list = None):
        '''cria o Heap.
        O heap é inicializado com uma lista vazia se nenhuma lista for recebida,
        se uma lista for recebida cria a partir de uma cópia dela.
        Criação em O(n), isso ocorre porque a criação da lista temos custo = O(n) e,
        para organizar a lista usando o método "_tidy_down" temos custo <= O(n*const)
        assim, O(n + n*const)) = O(n)
        prova formal: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
        Args:
            lista: lista de numeros, parametro opcional
        '''
        if lista == None:
            self._heap_list = []
        else: # TODO: Adicionar verificações para garantir que é uma lista valida
            self._heap_list = lista[:]
            meio = (len(lista) // 2) - 1
            for i in range(meio, -1, -1): # intervalo: [meio, meio-1, ... ,0]
                self._tidy_down(i)

    def _tidy_down(self, i: int):
        '''Método que matém a propriedade do pai ser menor que os filhos
        A partir de um elemento l[i] verificamos se o menor dos filhos é menor que l[i]
        Em caso positivo fazemos o swap dos elementos e continuamos a partir
        do indice do filho que foi substuído 
        Em caso negativo o loop é interrompido e o método retorna
        Condiçoes de parada: pai ser menor que os filhos, "pai" não ter filhos

        Args:
            i: indice do elemento, inteiro de [0 a n]
        '''
        fe = i * 2 + 1
        fd = fe + 1
        tam = len(self._heap_list)

        while fe < tam:
            smallest_index = fe  # vai guardar o indice do menor dos filhos
            if fd < tam:
                if self._heap_list[fd] < self._heap_list[fe]:
                    smallest_index = fd
            if self._heap_list[smallest_index] < self._heap_list[i]:
                self._heap_list[smallest_index], self._heap_list[i] = self._heap_list[i], self._heap_list[smallest_index]
                i = smallest_index # alteramos o indice corrente para onde estava o menor filho
            else: # pai é menor que os filho propriedade do heap mantida
                break
            fe = i * 2 + 1
            fd = fe + 1

    def _tidy_up(self, i: int):
        '''Método recursivo que matém a propriedade do pai ser menor que os filhos
        A partir de um elemento l[i] verificamos se o pai do elemento é maior que ele
        Em caso positivo fazemos o swap dos elementos e continuamos a partir
        do indice do pai que foi substuído 
        Em caso negativo a recursão é interrompida e o método retorna
        Condiçoes de parada: pai ser menor que o elemento, elemento o primeiro da lista
        
        Args:
            i: indice do elemento, inteiro de [0 a n]
        '''
        pai = (i - 1) // 2
        if (i == 0):
            return
        if (self._heap_list[i] < self._heap_list[pai]):
            self._heap_list[i], self._heap_list[pai] = self._heap_list[pai], self._heap_list[i] # swap com o pai
            self._tidy_up(pai) # repete o processo a partir do indice do pai
            return
        return

    def pop(self):
        '''Método que retira o elemento do topo do heap e retorna-o
        A função primeiro troca o elemento[0](min) do heap com o elemento do final
        remove o min e reorganiza o heap a partir do elemento[0]
        Custo O(log(n))

        Returns:
            O menor numero do heap
        '''
        if self._heap_list == []:
            return None
        self._heap_list[0], self._heap_list[-1] = self._heap_list[-1], self._heap_list[0]
        aux = self._heap_list.pop()
        self._tidy_down(0) # reorganiza o heap a partir da raiz. O(log(n))
        return aux

    def push(self, el):
        '''Método para inserir um elemento no Heap
        O elemento é inserido na ultima posição do Heap e 
        rodamos a função "_tidy_up" para reorganizaro o heap
        Custo O(log(n)). Obs: custo interno ao python de crescer o array não contabilizado 
        
        Args:
            numero a ser inserido no heap
        '''
        self._heap_list.append(el)
        self._tidy_up(len(self._heap_list) - 1) # reorganiza o heap a partir do último elemento. O(log(n))


    def heap_sort(lista: list):
        '''Ordena os elementos de uma lista de forma ascendente
        Utiliza a classe Heap para fazer a ordenação em O(n*log(n))

        Args:
            Lista com numeros a serem ordenados
        Returns
            Lista com os numeros ordenados
        '''
        h = Heap(lista)
        sorted_list = [0] * len(lista)
        for i in range(len(lista)):
            sorted_list[i] = h.pop()
        return sorted_list


# teste simples da classe
if __name__.find("main"): # foi chamada diretamente
    import random
    n = 100
    my_list = [ random.randint(0,1000) for i in range(n) ] # cria uma lista com n elementos aleatórios
    sorted_list = sorted(my_list) # "Oráculo"
    heap_sorted_list = Heap.heap_sort(my_list) # lista utilizando a classe implementada

    if sorted_list.__eq__(heap_sorted_list):
        print("Success")
    else:
        print("Error")
        print(heap_sorted_list)
