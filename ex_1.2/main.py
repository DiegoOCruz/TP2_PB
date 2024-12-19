from multiprocessing import Pool, cpu_count
import random
import time
import numpy as np 
from parallel_sum import parallel_sum  
import matplotlib.pyplot as plt 

# calcular a soma de um bloco
def sum_chunk(chunk):
    return sum(chunk)


def parallel_sum_multiprocessing(data):
    chunk_size = len(data) // cpu_count()
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    with Pool(processes=cpu_count()) as pool:
        return sum(pool.map(sum_chunk, chunks))

def main():
    data = []
    for _ in range(1,10_000):
        data.append(random.randint(1, 100_000))

    tempos = {}

    #Soma sequencial
    start_time = time.time()
    soma_sequencial = sum(data)
    tempo_sequencial = time.time() - start_time
    print(f"Soma sequencial: {soma_sequencial}")
    print(f"Tempo sequencial: {tempo_sequencial:.6f} segundos")
    tempos['Sequencial'] = tempo_sequencial

    #Soma paralela com multiprocessing 
    start_time = time.time()
    soma_paralela_mp = parallel_sum_multiprocessing(data)
    tempo_paralelo_mp = time.time() - start_time
    print(f"Soma paralela (multiprocessing): {soma_paralela_mp}")
    print(f"Tempo paralelo (multiprocessing): {tempo_paralelo_mp:.6f} segundos")
    tempos['Multiprocessing'] = tempo_paralelo_mp

    #Soma paralela com Cython
    np_data = np.array(data, dtype=np.int32)  # Converte para numpy.ndarray de int32
    start_time = time.time()
    soma_paralela_cython = parallel_sum(np_data)
    tempo_paralelo_cython = time.time() - start_time
    print(f"Soma paralela (Cython): {soma_paralela_cython}")
    print(f"Tempo paralelo (Cython): {tempo_paralelo_cython:.6f} segundos")
    tempos['Cython'] = tempo_paralelo_cython

    #Gera o gráfico comparativo
    plt.bar(tempos.keys(), tempos.values(), color=['blue', 'orange', 'green'])
    plt.xlabel('Método')
    plt.ylabel('Tempo (segundos)')
    plt.title('Comparação de Tempos de Execução')
    plt.tight_layout()
    plt.show() 

if __name__ == "__main__":
    main()
