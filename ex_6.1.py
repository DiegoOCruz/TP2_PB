def knapsack(pesos, valores, capacidade, n, memo):
    if n == 0 or capacidade == 0:
        return 0

    if (n, capacidade) in memo:
        return memo[(n, capacidade)]

    if pesos[n - 1] > capacidade:
        memo[(n, capacidade)] = knapsack(pesos, valores, capacidade, n - 1, memo)
    else:
        incluir_item = valores[n - 1] + knapsack(pesos, valores, capacidade - pesos[n - 1], n - 1, memo)
        excluir_item = knapsack(pesos, valores, capacidade, n - 1, memo)
        memo[(n, capacidade)] = max(incluir_item, excluir_item)

    return memo[(n, capacidade)]

pesos = [1, 2, 4, 8]
valores = [2, 3, 7, 9]
capacidade = 7
quantidade_itens = len(pesos)
memo = {}

valor_maximo = knapsack(pesos, valores, capacidade, quantidade_itens, memo)
print("Valor máximo:", valor_maximo)

