import multiprocessing
import time
import random

# Função para mesclar 
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Função MergeSort sequencial
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Função MergeSort paralelo 
def merge_sort_parallel(arr, pool):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = pool.map(merge_sort, [arr[:mid], arr[mid:]])
    return merge(left, right)

def comparacao(arr):  
    #sequencial
    start_time = time.time()
    sorted_arr = merge_sort(arr)
    sequential_time = time.time() - start_time
    print(f"Tempo de execução sequencial: {sequential_time:.5f} segundos")
    
    #paralela
    pool = multiprocessing.Pool(processes=2)
    start_time = time.time()
    sorted_arr_parallel = merge_sort_parallel(arr, pool)
    parallel_time = time.time() - start_time
    print(f"Tempo de execução paralelo: {parallel_time:.5f} segundos")
    pool.close()
    pool.join()
    
if __name__ == '__main__':
    lista = []
    for _ in range(1, 10_000_000):
        lista.append(random.randint(0,10_000_000))
    comparacao(lista)
