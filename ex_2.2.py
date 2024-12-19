class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"{self.nome}: {self.nota}"

def quicksort(lista):
   
    if len(lista) <= 1:  
        return lista

    pivo = lista[0]  # Primeiro elemento como pivô
     # Particiona o array em sub-arrays de elementos menores, iguais e maiores que o pivô
    menores = [x for x in lista[1:] if x.nota <= pivo.nota]  
    maiores = [x for x in lista[1:] if x.nota > pivo.nota]  

    return quicksort(menores) + [pivo] + quicksort(maiores)

def main():
  
    estudantes = [
        Estudante("Diego", 10.0),
        Estudante("Calos", 7.3),
        Estudante("Henrique", 2.1),
        Estudante("Carol", 7.5),
        Estudante("Paulo", 8.8),
        Estudante("Paula", 7.6),
        Estudante("Jessica", 9.5),
        Estudante("Poliana", 8.1),
        Estudante("Catarina", 6.1),
        Estudante("Ana", 7.9)
    ]

    # Ordena os estudantes
    estudantes_ordenados = quicksort(estudantes)

    print("\nLista ordenada por nota (usando o primeiro elemento como pivô):")
    for e in estudantes_ordenados:
        print(e)


if __name__ == "__main__":
    main()
