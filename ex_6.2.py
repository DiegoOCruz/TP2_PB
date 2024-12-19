def lcs(pattern_1, pattern_2):
    m = len(pattern_1)
    n = len(pattern_2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Construindo a tabela dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern_1[i - 1] == pattern_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruindo a subsequência
    i, j = m, n
    lcs_result = []
    while i > 0 and j > 0:
        if pattern_1[i - 1] == pattern_2[j - 1]:
            lcs_result.append(pattern_1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs_result))

def main():
    pattern_1 = "RGBGARGA"
    pattern_2 = "BGRARG"

    length, sequence = lcs(pattern_1, pattern_2)
    print("Comprimento:", length)
    print("Sequência:", sequence)

if __name__ == "__main__":
    main()
