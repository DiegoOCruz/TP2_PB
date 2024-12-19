import time
from multiprocessing import Pool
import random
import matplotlib.pyplot as plt

# Soma sequencial
def soma_sequencial(lista):
    return sum(lista)

# Soma paralela
def soma_paralela(lista):
    with Pool() as pool:
        chunk_size = len(lista) // 4
        chunks = [lista[i:i + chunk_size] for i in range(0, len(lista), chunk_size)]
        results = pool.map(sum, chunks)
    return sum(results)

def main():
    lista = []
    for _ in range(0, 10_000_000):
        lista.append(random.randint(1, 10_000_000))

    # Soma sequencial
    inicio_sequencial = time.time()
    soma_seq = soma_sequencial(lista)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial

    print(f"Soma Sequencial: {soma_seq}")
    print(f"Tempo Sequencial: {tempo_sequencial:.6f} segundos")

    # Soma paralela
    inicio_paralelo = time.time()
    soma_par = soma_paralela(lista)
    fim_paralelo = time.time()
    tempo_paralelo = fim_paralelo - inicio_paralelo

    print(f"Soma Paralela: {soma_par}")
    print(f"Tempo Paralelo: {tempo_paralelo:.6f} segundos")

    # Criando o gráfico
    metodos = ['Sequencial', 'Paralela']
    tempos = [tempo_sequencial, tempo_paralelo]

    plt.bar(metodos, tempos, color=['blue', 'green'])
    plt.xlabel('Método')
    plt.ylabel('Tempo (segundos)')
    plt.title('Comparação de Desempenho: Soma Sequencial vs Paralela')
    plt.show()

if __name__ == "__main__":
    main()
