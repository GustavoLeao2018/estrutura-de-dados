from random import randint

class Node:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None


class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None
        self.tamanho = 0

    def size(self):
        return self.tamanho

    def __len__(self):
        return self.size()

    def append(self, valor):
        if self.final is None:
            self.inicial = self.final = Node(valor)
        else:
            self.final.proximo = Node(valor)
            self.final = self.final.proximo
        self.tamanho += 1

    def addFirst(self, valor):
        no = Node(valor) # Cria o nó com o valor
        no.proximo = self.inicial # Atribui ao nó o nó inicial com sendo próximo
        self.inicial = no # Atribui ao nó inicial o nó criado acima
        self.tamanho += 1

    def pop(self):
        iter = self.first()
        anterior = None
        while iter is not None:
            if iter.proximo is None:
                break
            anterior = iter
            iter  = iter.proximo
        anterior.proximo = None
        self.tamanho -= 1
        return anterior.dado  # TODO Revisar! (Errado o conceito)

    def removeFirst(self):
        if self.inicial is self.final:
            pass
        self.inicial = self.inicial.proximo # TODO Revisar! (Tem bug)

    def remove(self, valor):  # TODO Revisar! (Deve estar certo, mas nao e o melhor.)
        iter = self.first()
        anterior = None
        while iter is not None:
            if iter.dado == valor and anterior is not None:
                anterior.proximo = iter.proximo
            anterior = iter
            iter = iter.proximo

        iter = self.first()
        while iter is not None:
            if iter.dado == valor:
                self.inicial = iter.proximo
            iter = iter.proximo

    def first(self):
        return self.inicial

    def last(self):
        return self.final

    def list(self):
        print("="*10,"[Lista:]","="*10)
        iter = self.first()
        while iter is not None:
            print(iter.dado)
            iter = iter.proximo
        print("="*30)

    def insert(self, valor):
        if self.first() is None:
            self.append(valor)
        elif valor < self.first().dado:
            self.addFirst(valor)
        elif valor > self.last().dado:
            self.append(valor)
        else:
            iter = self.first()
            anterior = proximo = None
            while iter is not None:
                anterior = iter
                proximo = iter.proximo
                if iter.proximo is not None:
                    if valor > anterior.dado and valor < proximo.dado:
                        no = Node(valor)
                        no.proximo = proximo
                        anterior.proximo  = no
                elif iter.proximo is None:
                    print(valor)
                iter = iter.proximo


if __name__ == '__main__':
    lista = Lista()

    for i in range(randint(10, 50)):
        lista.insert(randint(0, 100))

    lista.list()