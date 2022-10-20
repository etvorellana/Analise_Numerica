import numpy as np

def bisection_IT(f, a, b, TOL, N):
    '''
        Implementação do algorítmo da Bissecção de acordo com o 
        algorítmo 2.1 proposto no Burden
        OBJETIVO: Encontrar uma solução para f(x) = 0 dada a função f 
        contínua no intervalo [a, b], onde f(a) e f(b) têm sinais opostos
        ENTRADA: função f; pontos extremos a, b; tolerância TOL; número 
        máximo de iterações N.
        CRITERIO DE PARADA: Tamanho do intervalo menor que TOL;
        SAÌDA: Solução aproximada p, quantidade de iterações e tamanho 
        do último intervalo de busca.
    '''
    it = 1               # Passo 1: Inicialização
    FA = f(a)
    print("n \t a_n \t\t b_n \t\t P_n \t\t f(p_n)") 
    while( it < N):      # Passo 2: Verificando o limite de iotarações 
        h = (b - a)*0.5  
        p = a + h        # Passo 3: determinando o meio do intervalo 
        FP = f(p)
        print("{:d} \t {:.9f} \t {:.9f} \t {:.9f} \t {:.9f}".format(it, a, b, p, FP))
        if((FP == 0) or (h < TOL)): # Passo 4: Avaliando os criterios de parada 
            return (p, it, h)       # SAÍDA se satisfeito o criterio de parada
        it += 1          # Passo 5: Incrementando o cntador de iterações  
        if(np.sign(FA)*np.sign(FP) > 0):   # Passo 6: Determinando o novo intervalo 
            a = p
            FA = FP
        else:
            b = p
    return (p, it-1, h)    # Passo 7: SAÍDA após exceder o limite de iterações 


def bisection_TI(f, a, b, TOL, N):
    '''
        Implementação do algorítmo da Bissecção de acordo com o algorítmo 
        2.1 proposto no Burden
        OBJETIVO: Encontrar uma solução para f(x) = 0 dada a função f 
        contínua no intervalo [a, b], onde f(a) e f(b) têm sinais opostos
        ENTRADA: função f; pontos extremos a, b; tolerância TOL; número 
        máximo de iterações N.
        CRITERIO DE PARADA: Tamanho do intervalo (TI) menor que TOL;
        SAÌDA: Solução aproximada p, quantidade de iterações e tamanho do 
        último intervalo de busca.
    '''
    it = 1               # Passo 1: Inicialização
    FA = f(a)
    while( it < N):      # Passo 2: Verificando o limite de iotarações 
        h = (b - a)*0.5  
        p = a + h        # Passo 3: determinando o meio do intervalo 
        FP = f(p)
        if((FP == 0) or (h < TOL)): # Passo 4: Avaliando os criterios de parada 
            return (p, it, h)       # SAÍDA se satisfeito o criterio de parada
        it += 1          # Passo 5: Incrementando o cntador de iterações  
        if(np.sign(FA)*np.sign(FP) > 0):   # Passo 6: Determinando o novo intervalo 
            a = p
            FA = FP
        else:
            b = p
    return (p, it-1, h)    # Passo 7: SAÍDA após exceder o limite de iterações 


def bisection_TA(f, a, b, TOL, N):
    '''
        Implementação do algorítmo da Bissecção de acordo com o algorítmo 
        2.1 proposto no Burden
        OBJETIVO: Encontrar uma solução para f(x) = 0 dada a função f 
        contínua no intervalo [a, b], onde f(a) e f(b) têm sinais opostos
        ENTRADA: função f; pontos extremos a, b; tolerância TOL; número 
        máximo de iterações N.
        CRITERIO DE PARADA: Tamanho absoluto (TA) do intervalo menor que TOL;
        SAÌDA: Solução aproximada p, quantidade de iterações e tamanho do 
        último intervalo de busca.
    '''
    it = 1               # Passo 1: Inicialização
    FA = f(a)
    p = a
    while( it < N):      # Passo 2: Verificando o limite de iotarações 
        h = (b - a)*0.5
        err = p 
        p = a + h        # Passo 3: determinando o meio do intervalo          
        FP = f(p)
        err = np.abs(p - err)
        if(FP == 0) or (err < TOL) : # Passo 4: Avaliando os criterios de parada  
            return (p, it, err)       # SAÍDA se achou P
        it += 1          # Passo 5: Incrementando o cntador de iterações  
        if(np.sign(FA)*np.sign(FP) > 0):   # Passo 6: Determinando o novo intervalo 
            a = p
            FA = FP
        else:
            b = p
    return (p, it-1, err)    # Passo 7: SAÍDA após exceder o limite de iterações 



def bisection_TR(f, a, b, TOL, N):
    '''
        Implementação do algorítmo da Bissecção de acordo com o algorítmo 
        2.1 proposto no Burden
        OBJETIVO: Encontrar uma solução para f(x) = 0 dada a função f 
        contínua no intervalo [a, b], onde f(a) e f(b) têm sinais opostos
        ENTRADA: função f; pontos extremos a, b; tolerância TOL; número 
        máximo de iterações N.
        CRITERIO DE PARADA: Tamanho relativo (TR) do intervalo menor que TOL;
        SAÌDA: Solução aproximada p, quantidade de iterações e tamanho do 
        último intervalo de busca.
    '''
    it = 1               # Passo 1: Inicialização
    FA = f(a)
    p = a
    while( it < N):      # Passo 2: Verificando o limite de iotarações 
        h = (b - a)*0.5
        err = p 
        p = a + h        # Passo 3: determinando o meio do intervalo          
        FP = f(p)
        err = np.abs(p - err)/np.abs(p)
        if(FP == 0) or (err < TOL) : # Passo 4: Avaliando os criterios de parada  
            return (p, it, err)       # SAÍDA se achou P
        it += 1          # Passo 5: Incrementando o cntador de iterações  
        if(np.sign(FA)*np.sign(FP) > 0):   # Passo 6: Determinando o novo intervalo 
            a = p
            FA = FP
        else:
            b = p
    return (p, it-1, err)    # Passo 7: SAÍDA após exceder o limite de iterações 


def bisection_FP(f, a, b, TOL, N):
    '''
        Implementação do algorítmo da Bissecção de acordo com o algorítmo 
        2.1 proposto no Burden
        OBJETIVO: Encontrar uma solução para f(x) = 0 dada a função f 
        contínua no intervalo [a, b], onde f(a) e f(b) têm sinais opostos
        ENTRADA: função f; pontos extremos a, b; tolerância TOL; 
        número máximo de iterações N.
        CRITERIO DE PARADA: f(p) menor que TOL;
        SAÌDA: Solução aproximada p, quantidade de iterações e tamanho 
        do último intervalo de busca.
    '''
    it = 1               # Passo 1: Inicialização
    FA = f(a)
    while( it < N):      # Passo 2: Verificando o limite de iotarações 
        h = (b - a)*0.5  
        p = a + h        # Passo 3: determinando o meio do intervalo 
        FP = f(p)
        err = np.abs(FP)
        if((FP == 0) or (err < TOL)): 
                                    # Passo 4: Avaliando os criterios de parada 
            return (p, it, err)       # SAÍDA se satisfeito o criterio de parada
        it += 1          # Passo 5: Incrementando o cntador de iterações  
        if(np.sign(FA)*np.sign(FP) > 0):   # Passo 6: Determinando o novo intervalo 
            a = p
            FA = FP
        else:
            b = p
    return (p, it-1, err)    # Passo 7: SAÍDA após exceder o limite de iterações

def bisection(f, a, b, TOL, N, out = 0):
    '''
        Implementação do algorítmo da Bissecção de acordo com o algorítmo 
        2.1 proposto no Burden
        OBJETIVO: Encontrar uma solução para f(x) = 0 dada a função f 
        contínua no intervalo [a, b], onde f(a) e f(b) têm sinais opostos
        ENTRADA: função f; pontos extremos a, b; tolerância TOL; número 
        máximo de iterações N, tipo criterio de parada;
            0 -> TI com saida passo a passo; 
            1 -> TI; 
            2 -> TA; 
            3 -> TR; 
            4 -> FP;
        SAÌDA: Solução aproximada p, quantidade de iterações e tamanho 
        do último intervalo de busca.
'''              

    imp = [bisection_IT, bisection_TI, bisection_TA, bisection_TR, bisection_FP]
    return imp[out](f, a, b, TOL, N)


def qStepsBesection(a, b, prec):
    '''
        A seguinte função permite determinar o número máximo de iterações 
        necessárias para, utilizando o método de Bissecção, conseguir uma 
        precisão específica. A implementação se baseia nos cálculos 
        apresentados no Exemplo 2 do Burden
        ENTRADA: pontos extremos a, b; prec precisão desejada;
        SAÌDA: Quantidade necessária  de iterações 
    '''
    return (-1*np.log10(prec) / np.log10(2*(b - a)))