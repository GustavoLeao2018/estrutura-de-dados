from random import randint


class Node:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None


class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, valor):
        if self.tail is None:
            self.head = self.tail = Node(valor)
        else:
            self.tail.proximo = Node(valor)
            self.tail = self.tail.proximo

    def mostrar(self):
        i = self.head
        while i is not None:
            print(f"Nó: {i.dado}")
            i = i.proximo

    def addFirst(self, valor):
        no = Node(valor)
        no.proximo = self.head
        self.head = no

    def removeFirst(self):
        i = self.head
        self.head = i.proximo

    def removeLast(self):
        i = self.head
        anterior = None
        while i is not None:
            if i.proximo is None:
                break
            anterior = i
            i = i.proximo

        anterior.proximo = None


class Main:
    def __init__(self):
        print("Criando lista encadeada!")

        lista = ListaEncadeadaSimples()

        for item in range(5):
            lista.append(randint(0, 100))

        lista.mostrar()
        print("="*100)

        lista.removeFirst()

        print("="*100)
        lista.mostrar()



if __name__ == '__main__':
    Main()


# estudar
# http://www.algoritmosempython.com.br/capitulos/estruturas-dados/listas
