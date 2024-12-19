import time
from multiprocessing import Process, Value
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parallel_search(root, target):
    def search_subtree(node, target, found):
        if node is None or found.value:
            return
        if node.value == target:
            found.value = True
            return
        search_subtree(node.left, target, found)
        search_subtree(node.right, target, found)

    found = Value('b', False)
    left_proc = Process(target=search_subtree, args=(root.left, target, found))
    right_proc = Process(target=search_subtree, args=(root.right, target, found))

    left_proc.start()
    right_proc.start()
    left_proc.join()
    right_proc.join()

    return found.value

# Função para construir uma árvore binária completa com um número específico de nós
def generate_tree(n):
    nodes = [TreeNode(i) for i in range(n)]
    for i in range(n // 2):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

# Testar com diferentes tamanhos de árvore
tamanhos = [1, 2, 4, 8, 16, 32, 64, 128]
tempo_tot = []

for n in tamanhos:
    tree = generate_tree(n)
    tempo_ini = time.perf_counter()
    parallel_search(tree, 7)  
    tempo_fim = time.perf_counter()
    print(f"Tamanho da árvore: {n}, Tempo de execução: {tempo_fim - tempo_ini:.6f} segundos")
    tempo_tot.append(tempo_fim - tempo_ini)


plt.plot(tamanhos, tempo_tot, marker='o', linestyle='-', color='b')
plt.xlabel('Tamanho da árvore')
plt.ylabel('Tempo de execução (segundos)')
plt.title('Tempo de Execução do Algoritmo de Busca Paralela')
plt.grid(True)
plt.show()
