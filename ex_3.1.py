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

# Criação da lista encadeada
linked_list = LinkedList()

# Inserção de elementos
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(40)
linked_list.insert_at_end(50)
linked_list.insert_at_end(60)
linked_list.insert_at_beginning(5)
# Exibe a lista
print("Lista após inserções:")
linked_list.traverse()

# Remove um elemento
linked_list.remove(20)
print("Lista após remoção de 20:")
linked_list.traverse()

linked_list.remove(50)
print("Lista após remoção de 50:")
linked_list.traverse()

