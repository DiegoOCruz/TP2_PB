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
        
# Exemplo de Uso
# Criação da lista duplamente encadeada
dll = DoublyLinkedList()

# Inserção de elementos
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

# Percorrimento da lista
print("Percorrendo da frente para trás:")
dll.traverse_forward()

print("Percorrendo de trás para frente:")
dll.traverse_backward()

# Remoção de um elemento
dll.remove(20)
print("Lista após remoção de 20 (frente para trás):")
dll.traverse_forward()
