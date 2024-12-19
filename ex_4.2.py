import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memo(n, memo={}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def main():
    numero = 30

    # Tempo para a função sem memorização.
    tempo_ini_recursao = time.time()
    result_recursao = fibonacci(numero)
    tempo_final_recursao = time.time()
    tempo_recursive = tempo_final_recursao - tempo_ini_recursao

    # Tempo para a função com memorização.
    tempo_ini_memo = time.time()
    result_memo = fibonacci_memo(numero)
    tempo_final_memo = time.time()
    tempo_memo = tempo_final_memo - tempo_ini_memo

    # Resultados formatados
    print(f'n = {numero}')
    print(f"Sem memoization: resultado = {result_recursao}, tempo = {tempo_recursive:.6f} segundos")
    print(f"Com memoization: resultado = {result_memo}, tempo = {tempo_memo:.6f} segundos")

if __name__ == "__main__":
    main()
