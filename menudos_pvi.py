import numpy as np

'''
menudos_pvi.py

modulo que implementa MEtodos NUméricos para 
equações Diferenciais OrdináriaS - Problemas de 
Valor Inicial
'''

def metEuler(f, a, b, N, y0):
    #Permite aproximar a solução do problema de valor inicial
    # em N+1 pontos uniformemente espaçados no intervalo fechado [a, b]
    # Entrada: f(t,y), o intervalo [a, b], N, y0 condição inicial
    # Saida: a aproximação w_i da fdunção y(t_i) para os N+1 pontos
    # Passo 1 Faça h = (b - a) / N
    h = (b - a)/N
    t = np.linspace(a, b, N+1)
    #t = np.arange(a, b, h)
    w = np.zeros_like(t)
    #w = np.zeros(t.shape)
    w[0] = y0;
    # SAIDA (t, w)
    # Passo 2 Para i = 0, 1, 2,..., N-1 fazer 
    for i in range(N): 
        #Passo 3 w = w + hf(t, w)
        w[i+1] = w[i] + h*f(t[i], w[i])  
    return (t, w)

def metTaylor(F, a, b, N, y0):
    #Permite aproximar a solução do problema de valor inicial
    # em N+1 pontos uniformemente espaçados no intervalo fechado [a, b]
    # utilizando o método de Taylor de ordem n
    # Entrada: Uma lista com as funções f(t,y), f'(t,y), ..., f^(n-1)(t,y), 
    # o intervalo [a, b], N, y0 condição inicial
    # Saida: a aproximação w_i da fdunção y(t_i) para os N+1 pontos
    # Passo 1 Faça h = (b - a) / N
    h = (b - a)/N
    t = np.linspace(a, b, N+1)
    w = np.zeros_like(t)
    w[0] = y0;
    # SAIDA (t, w)
    # Passo 2 Para i = 0, 1, 2,..., N-1 fazer 
    for i in range(N): 
        #Passo 3 w = w + hf(t, w)
        fat = 1
        for j in range(len(F)):
            fat *= (j+1)
            w[i+1] += ((h**j)/fat)*F[j](t[i], w[i])
        w[i+1] *= h    
        w[i+1] += w[i]
    return (t, w)

