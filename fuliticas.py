'''
fuliticas.py implementação de FUnções e soluções
anaLITICAS para testar os métodos implementados no
môdulo menudos.py
'''
import numpy as np

# 4. Soluções de Equações com Uma Variável

def f_exem4_1(x):
    return x**3 + 4*x**2 - 10


def fExemplo_01(t, y):
    return y - t**2 + 1

def sExemplo_01(t):
    return (t+1.0)**2 - 0.5*np.exp(t)

def dfdtExemplo_01(t, y):
    return y - t**2 - 2*t + 1

def d2fdt2Exemplo_01(t, y):
    return y - t**2 - 2*t - 1

d3fdt3Exemplo_01 = d2fdt2Exemplo_01

taylorF = [fExemplo_01, dfdtExemplo_01, d2fdt2Exemplo_01, d3fdt3Exemplo_01]

def sExercicio5_2_1_a(t):
    return 0.20*(t*np.exp(3*t) - 0.20*np.exp(3*t) + 0.25*np.exp(-2*t)) 

def fExercicio5_2_1_a(t, y):
    return t*np.exp(3*t) - 2*y

def sExercicio5_2_1_b(t):
    return t + 1 / (1 - t)

def fExercicio5_2_1_b(t, y):
    return 1 + (t - y)**2

def sExercicio5_2_1_c(t):
    return t * np.log(t) + 2*t

def fExercicio5_2_1_c(t, y):
    return 1 + y/t

def sExercicio5_2_1_d(t):
    return 0.5*np.sin(2*t) - (1/3)*np.cos(3*t) + (4/3)

def fExercicio5_2_1_d(t, y):
    return np.cos(2*t) + np.sin(3*t)



