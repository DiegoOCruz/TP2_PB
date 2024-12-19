def quickselect(array, low, high, k):
    # Caso base: se o array tiver apenas um elemento
    if low == high:
        return array[low]
    
    # Particiona o array e obtém o índice do pivô
    pivot_index = partition(array, low, high)
    
    # Caso em que o pivô é o k-ésimo menor elemento
    if k == pivot_index:
        return array[k]
    # Caso o k-ésimo elemento esteja à esquerda do pivô
    elif k < pivot_index:
        return quickselect(array, low, pivot_index - 1, k)
    # Caso o k-ésimo elemento esteja à direita do pivô
    else:
        return quickselect(array, pivot_index + 1, high, k)

def partition(array, low, high):
    # Escolhe o pivô como o último elemento
    pivot = array[high]
    i = low - 1  # Índice do menor elemento
    
    for j in range(low, high):
        # Se o elemento atual for menor ou igual ao pivô
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Troca os elementos
    
    # Coloca o pivô na posição correta
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def find_median(array):
    n = len(array)
    if n % 2 == 1:
        # Ímpar: retorna o elemento central
        return quickselect(array, 0, n - 1, n // 2)
    else:
        # Par: encontra os dois valores centrais
        left_mid = quickselect(array, 0, n - 1, n // 2 - 1)
        right_mid = quickselect(array, 0, n - 1, n // 2)
        return (left_mid + right_mid) / 2

# Exemplo de uso
array = [10, 4, 5, 8, 6, 11, 26, 30, 35, 12, 14]
mediana = find_median(array.copy())  
print(f"A mediana é: {mediana}")

def quickselect_k_smallest(array, k):
    # Posiciona o k-ésimo menor elemento na posição correta
    quickselect(array, 0, len(array) - 1, k - 1)
    # Retorna os k menores elementos (parte inicial do array)
    return sorted(array[:k])  # Opcional: ordena os k menores para exibição

# Exemplo de uso
array = [10, 4, 5, 8, 6, 11, 26, 30, 35, 12, 14]
k = 5
k_menores = quickselect_k_smallest(array.copy(), k) 
print(f"Os {k} menores elementos são: {k_menores}")
