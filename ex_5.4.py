import random
import time
from multiprocessing import Pool, cpu_count
import random

# Função para encontrar o máximo sequencialmente
def max_sequencial(lista):
    max_val = lista[0]
    for num in lista:
        if num > max_val:
            max_val = num
    return max_val

# Função para encontrar o máximo em uma sublista
def max_parcial(sublista):
    return max(sublista)

# Dividir a lista em partes iguais
def dividir_lista(lista, num_processos):
    tamanho = len(lista)
    return [lista[i * tamanho // num_processos: (i + 1) * tamanho // num_processos] for i in range(num_processos)]

# Função para encontrar o máximo usando paralelismo
def max_paralelo(lista):
    num_processos = cpu_count()  # Usar todos os processos disponíveis
    partes = dividir_lista(lista, num_processos)
    with Pool(num_processos) as pool:
        resultados = pool.map(max_parcial, partes)
    return max(resultados)

if __name__ == "__main__":
    lista = []
    for i in range(1,10_000_000):
        lista.append(random.randint(0,10_000_000))
       
    # Versão sequencial
    start_time = time.time()
    max_val_seq = max_sequencial(lista.copy())
    end_time = time.time()
    print(f"Máximo (sequencial): {max_val_seq}")
    print(f"Tempo sequencial: {end_time - start_time:.6f} segundos")

    # Versão paralela
    start_time = time.time()
    max_val_par = max_paralelo(lista.copy())
    end_time = time.time()
    print(f"Máximo (paralelo): {max_val_par}")
    print(f"Tempo paralelo: {end_time - start_time:.6f} segundos")