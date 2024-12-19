import time
import matplotlib.pyplot as plt

# Função Torres de Hanói
def hanoi(disc, ori, dest, aux):
    if disc == 1:
        print('Move disco {} da torre {} para a torre {}'.format(disc, ori, dest))
        return

    hanoi(disc - 1, ori, aux, dest)
    print('Move disco {} da torre {} para a torre {}'.format(disc, ori, dest))
    hanoi(disc - 1, aux, dest, ori)

# Medir tempos para diferentes números de discos
discos = [1,10,15]
tempos = []

for n in discos:
    inicio = time.time()
    hanoi(n, 'A', 'B', 'C')
    fim = time.time()
    tempos.append(fim - inicio)

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(discos, tempos, marker='o', label='Tempo de execução')
plt.title('Tempo de execução para Torres de Hanói')
plt.xlabel('Número de discos')
plt.ylabel('Tempo (segundos)')
plt.grid()
plt.legend()
plt.show()

# Comentário sobre complexidade
print("A complexidade do algoritmo é O(2^n), e o tempo cresce exponencialmente com o número de discos.")
