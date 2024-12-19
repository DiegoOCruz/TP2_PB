# Definição do nó
class Node:
    def __init__(self, data):
        self.data = data       # Armazena o valor do nó
        self.next = None       # Ponteiro para o próximo nó
        self.prev = None       # Ponteiro para o nó anterior

# Definição da Lista Duplamente Encadeada
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Referência ao primeiro nó da lista

    # Inserção no início
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:  # Atualiza o ponteiro do nó atual
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # Inserção no final
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # Lista vazia
            self.head = new_node
            return
        current = self.head
        while current.next:  # Percorre até o final da lista
            current = current.next
        current.next = new_node
        new_node.prev = current

    # Remoção de um nó pelo valor
    def remove(self, key):
        current = self.head
        while current and current.data != key:  # Procura o nó pelo valor
            current = current.next
        if current is None:  # Valor não encontrado
            return
        if current.prev:  # Ajusta o ponteiro do nó anterior
            current.prev.next = current.next
        if current.next:  # Ajusta o ponteiro do próximo nó
            current.next.prev = current.prev
        if current == self.head:  # Se o nó removido for o head
            self.head = current.next

    # Percorrimento da lista (frente para trás)
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Percorrimento da lista (trás para frente)
    def traverse_backward(self):
        current = self.head
        if not current:  # Lista vazia
            print("None")
            return
        while current.next:  # Vai até o último nó
            current = current.next
        while current:  # Percorre de trás para frente
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    # 1. Ordenação usando Bubble Sort
    def bubble_sort(self):
        if not self.head or not self.head.next:
            return  # Lista vazia ou com apenas um elemento
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    # Troca os valores
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    # 2. Mesclagem de duas listas duplamente encadeadas ordenadas
    @staticmethod
    def merge_sorted_lists(list1, list2):
        merged_list = DoublyLinkedList()

        # Ponteiros para percorrer as duas listas
        current1 = list1.head
        current2 = list2.head

        # Mescla os valores em ordem
        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next

        # Adiciona os elementos restantes da lista 1
        while current1:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next

        # Adiciona os elementos restantes da lista 2
        while current2:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

        return merged_list

# Testes
# Criação de listas duplamente encadeadas
dll1 = DoublyLinkedList()
dll2 = DoublyLinkedList()

# Inserção de elementos na lista 1
dll1.insert_at_end(40)
dll1.insert_at_end(10)
dll1.insert_at_end(30)
dll1.insert_at_end(20)

print("Lista 1 antes da ordenação:")
dll1.traverse_forward()

# Ordenação da lista 1
dll1.bubble_sort()
print("Lista 1 após a ordenação:")
dll1.traverse_forward()

# Inserção de elementos na lista 2
dll2.insert_at_end(25)
dll2.insert_at_end(5)
dll2.insert_at_end(15)
dll2.insert_at_end(35)

print("Lista 2 antes da ordenação:")

# Ordenação da lista 2
dll2.bubble_sort()
print("Lista 2 após a ordenação:")
dll2.traverse_forward()

# Mesclagem das listas ordenadas
merged_list = DoublyLinkedList.merge_sorted_lists(dll1, dll2)
print("Lista mesclada:")
merged_list.traverse_forward()
