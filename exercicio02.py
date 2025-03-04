import random

def gerar_lista(n):    
    return [random.randint(1, 1000) for _ in range(n)]

def busca_binaria(lista, alvo):    
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio  
        elif lista[meio] < alvo:
            esquerda = meio + 1  
        else:
            direita = meio - 1  
    
    return -1  

def main():    
    while True:
        try:
            n = int(input("Digite a quantidade de números aleatórios a serem gerados: "))
            if n > 0:
                break
            else:
                print("Erro: O número deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")
    
    lista = gerar_lista(n)
    lista.sort()

    print("\nLista ordenada:")
    print(lista)
    
    while True:
        try:
            alvo = int(input("\nDigite um número inteiro para buscar na lista: "))
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido.")
    
    indice = busca_binaria(lista, alvo)
    
    if indice != -1:
        print(f"O número {alvo} foi encontrado na posição {indice}.")
    else:
        print(f"O número {alvo} não está na lista.")

if __name__ == "__main__":
    main()
