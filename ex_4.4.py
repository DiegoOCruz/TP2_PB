def permutacoes_string(string):
    if len(string) <= 1:
        return [string]

    permutacoes = set()  
    for i, char in enumerate(string):
        restante = string[:i] + string[i+1:]
        for p in permutacoes_string(restante):
            permutacoes.add(char + p)  
    return list(permutacoes)  

def main():
    string = "diego"
    print("Permutações da string:")
    resultado = permutacoes_string(string)
    print(resultado)

if __name__ == "__main__":
    main()



