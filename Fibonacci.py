import numpy as np

def fibonacci(n):
    """ Algoritmo matricial para calcular o n-ésimo número da sequência de Fibonacci.
        Entrada:
            n inteiro não negativo diferente de zero.
        Saída:
            inteiro contendo o valor do n-ésimo número da sequência de Fibonacci.
    """
    assert n>=0
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        M1 = np.array([[0,1],[1,1]])
        M2 = M1
        for i in range(1,n):
            M2 = np.dot(M1,M2)
        return M2[0,1]

#teste da função
fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

for i in range(16):
    print(f"O {i+1}° número da sequência de Fibonacci é: {fibonacci(i+1)}")
    print(fibonacci_sequence[i]==fibonacci(i+1)) #comparando os valores da função com o array