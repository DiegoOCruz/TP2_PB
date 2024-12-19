def troco(moedas, troco_a_dev):

    dp = [float('inf')] * (troco_a_dev + 1)
    dp[0] = 0  # Base: 0 moedas para o valor 0


    for i in range(1, troco_a_dev + 1):
        for coin in moedas:
            if i - coin >= 0:  # Verificar se a moeda pode ser usada
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[troco_a_dev]

def main(moedas, valor):
    print(f"Quantidade mínima de moedas: {troco(moedas, valor)}")

if __name__ == "__main__":
    main([1, 5, 10, 25, 50], 66)
    main([1, 5, 10, 25], 95)
    main([1, 5, 10, 50], 38)
    main([1, 5, 25, 50], 44)


