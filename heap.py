class Heap:

    def __init__(self, lista=None):
        '''cria o Heap, vazio se nenhuma lista for passada ou a partir da lista passada'''
        if lista == None:
            self.hp = []

        else:
            self.hp = lista[:]
            m = (len(lista) // 2) - 1
            for i in range(m, -1, -1):
                self._tidy_down(i)

    def _tidy_down(self, i):
        fe = i * 2 + 1
        fd = fe + 1
        tam = len(self.hp)

        while fe < tam:
            aux = fe  # vou pegar o menor dos fiilhos e colocar em aux pra comparar
            if fd < tam:
                if self.hp[fd] < self.hp[fe]:
                    aux = fd
            if self.hp[aux] < self.hp[i]:
                self.hp[aux], self.hp[i] = self.hp[i], self.hp[aux]
                i = aux
            else:
                break
            fe = i * 2 + 1
            fd = fe + 1

    def pop(self):
        '''retira o elemento do topo do heap e retorna-o'''
        if self.hp == []:
            return None
        self.hp[0], self.hp[-1] = self.hp[-1], self.hp[0]
        aux = self.hp.pop()
        self._tidy_down(0)
        return aux

    def _tidy_up(self, i):
        pai = (i - 1) // 2
        if (i == 0):
            return
        if (self.hp[i] < self.hp[pai]):
            self.hp[i], self.hp[pai] = self.hp[pai], self.hp[i]
            self._tidy_up(pai)
            return
        return

    def push(self, el):
        self.hp.append(el)
        self._tidy_up(len(self.hp) - 1)


    def heap_sort(lista):
        '''Ordena os elementos de uma lista recebida'''
        h = Heap(lista)
        for i in range(len(lista)):
            lista[i] = h.pop()
        return