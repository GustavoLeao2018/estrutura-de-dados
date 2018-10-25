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
        return self.tamanho

    def append(self, valor):
        if self.final is None:
            self.inicial = self.final = Node(valor)
            self.tamanho += 1
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
        return self.last()

    def removeFirst(self):
        self.inicial = self.inicial.proximo

    def remove(self, valor):
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


if __name__ == '__main__':
    lista = Lista()

    for item in range(10):
        lista.append(item)

    lista.append(5)
    lista.addFirst(5)
    lista.list()
    lista.remove(5)
    lista.list()