import random

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n -1)

def main():
    for _ in range(0,10):
        n = random.randint(1,20)
        print(f'O fatorial de {n} é igual a: {fatorial(n)}')

if __name__ == "__main__":
    main()
    print('Código possui complexidade O(n) pois cada chamada recursiva processa uma operação multiplicativa.')


              
        
