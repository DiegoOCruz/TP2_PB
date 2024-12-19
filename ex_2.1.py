import time
import random
import matplotlib.pyplot as plt

# Função QuickSort para pivô dinâmico
def quicksort(array, pivot_type):
    if len(array) <= 1:
        return array

    # Escolhe o pivô com base no tipo especificado
    if pivot_type == "primeiro":
        pivot = array[0]
        restantes = array[1:]
    elif pivot_type == "ultimo":
        pivot = array[-1]
        restantes = array[:-1]
    elif pivot_type == "mediano":
        pivot = sorted([array[0], array[len(array)//2], array[-1]])[1]
        restantes = [x for x in array if x != pivot]
    else:
        raise ValueError("Tipo de pivô inválido")

    # Particiona o array em sub-arrays de elementos menores, iguais e maiores que o pivô
    menores = [x for x in restantes if x <= pivot]
    maiores = [x for x in restantes if x > pivot]

    # Chama o quicksort recursivamente e concatena os resultados
    return quicksort(menores, pivot_type) + [pivot] + quicksort(maiores, pivot_type)

# Testa o desempenho do QuickSort
def medir_tempo(array, pivot_type):
    inicio = time.time()
    quicksort(array, pivot_type)
    return time.time() - inicio

def main():
    # Tamanho do array e inicialização dos dados
    tamanho_array = 10_000
    array_original = [random.randint(1, 100_000_000) for _ in range(tamanho_array)]

    # Testa para diferentes tipos de pivô
    tipos_pivo = ["primeiro", "ultimo", "mediano"]
    tempos = []

    for tipo in tipos_pivo:
        array = array_original.copy()
        tempo = medir_tempo(array, tipo)
        tempos.append(tempo)
        print(f"Tempo com pivô {tipo}: {tempo:.5f} segundos")

    # Gera o gráfico comparativo
    plt.bar(tipos_pivo, tempos, color=["blue", "green", "orange"])
    plt.xlabel("Estratégia de Pivô")
    plt.ylabel("Tempo de Execução (s)")
    plt.title("Comparação do Desempenho do QuickSort com Diferentes Pivôs")
    plt.show()

if __name__ == "__main__":
    main()

