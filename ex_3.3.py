# Definição do nó
class Node:
    def __init__(self, data):
        self.data = data  # Armazena o valor do nó
        self.next = None  # Ponteiro para o próximo nó

# Definição da Lista Encadeada
class LinkedList:
    def __init__(self):
        self.head = None  # Referência ao primeiro nó da lista

    # Inserção no início
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # O novo nó aponta para o atual 'head'
        self.head = new_node  # Atualiza o 'head' para o novo nó

    # Inserção no final
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # Se a lista estiver vazia
            self.head = new_node
            return
        current = self.head
        while current.next:  # Percorre até o final da lista
            current = current.next
        current.next = new_node  # O último nó aponta para o novo nó

    # Remoção de um nó pelo valor
    def remove(self, key):
        current = self.head
        prev = None
        while current and current.data != key:  # Procura pelo nó com o valor
            prev = current
            current = current.next
        if current is None:  # Valor não encontrado
            return
        if prev is None:  # O nó a ser removido é o primeiro
            self.head = current.next
        else:
            prev.next = current.next  # Pula o nó atual na ligação

    # Percorrimento da lista
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indica o final da lista

 # Método para buscar um nó pelo valor
    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position  # Retorna a posição do nó encontrado
            current = current.next
            position += 1
        return -1  # Retorna -1 se o valor não for encontrado

    # Método para inverter a lista encadeada
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Armazena o próximo nó
            current.next = prev  # Inverte a direção do ponteiro
            prev = current  # Avança o ponteiro 'prev'
            current = next_node  # Avança para o próximo nó
        self.head = prev  # Atualiza o 'head' para o novo início da lista

# Testando as funcionalidades
linked_list = LinkedList()

# Inserindo elementos
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)

print("Lista inicial:")
linked_list.traverse()

# Testando o método de busca
print("Posição de 20:", linked_list.search(20))  # Esperado: 0
print("Posição de 40:", linked_list.search(40))  # Esperado: 3
print("Posição de 50:", linked_list.search(50))  # Esperado: -1 (não encontrado)

# Testando a inversão da lista
print("Lista antes de inverter:")
linked_list.traverse()

linked_list.reverse()
print("Lista após inverter:")
linked_list.traverse()