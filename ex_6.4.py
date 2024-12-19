def contagem_pintura(N, C):
    #cadeira i está pintada com a cor j
    dp = [[0 for _ in range(C)] for _ in range(N)]
    
    # Inicialização: qualquer cadeira pode ser pintada de qualquer cor inicialmente
    for j in range(C):
        dp[0][j] = 1
    
    # Preenchendo a tabela dp
    for i in range(1, N):
        for j in range(C):
            dp[i][j] = sum(dp[i-1][k] for k in range(C) if k != j)
    
    
    return sum(dp[N-1][j] for j in range(C))

def main(qdt_cadeira, qtd_cores):
    print(f"Quantidade de maneiras de pintar {qdt_cadeira} cadeiras com {qtd_cores} cores: {contagem_pintura(qdt_cadeira, qtd_cores)}")

if __name__ == "__main__":
    main(2,3)



