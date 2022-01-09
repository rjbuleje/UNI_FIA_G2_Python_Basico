# Un sólo factor
NIVELES = [ 2, 4, 6, 8, 10] #DQO
CUERPOS = [ 1, 3.5, 6, 8.25, 11, 15, 20] #cantidad de cuerpos

def grey_inicial( valor, var_1, var_2):
    
    if valor <= var_1:
        return 1
    elif valor >= var_2:
        return 0
    else:
        return (var_2 - valor) / ( var_2 - var_1)
    

def grey_intermedio( valor, var_1, var_2, var_3):
    
    if  valor <= var_1 or valor >= var_3:
        return 0
    elif valor > var_2:
        return (var_3 - valor) / (var_3 - var_2)
    else:
        return  (valor - var_1) / (var_2 - var_1) 
    

def grey_final( valor, var_1, var_2):
   
    if valor >= var_2 :
        return 1
    elif var_1 >= valor:
        return 0
    else:
        return (valor - var_1) / ( var_2 - var_1)

    

def grey_clustering(niveles, cuerpos):
    resultados = []
    num_niveles = len(niveles)
    num_cuerpos = len(cuerpos)

    for c in range(num_cuerpos):
        resultados_intermedios = []
        for n in range(num_niveles):
            if n == 0:
                resultados_intermedios.append(grey_inicial( cuerpos[c], niveles[n], niveles[n+1]))
            elif n == (num_niveles-1):
                resultados_intermedios.append(grey_final(cuerpos[c], niveles[n-1] , niveles[n]))
            else:
                resultados_intermedios.append(grey_intermedio(cuerpos[c], niveles[n-1], niveles[n], niveles[n+1]))
        resultados.append(resultados_intermedios)

    return resultados

def grey_clustering_2(niveles, cuerpos):
    resultados = []
    num_niveles = len(niveles)
    num_cuerpos = len(cuerpos)

    for c in range(num_cuerpos):
        resultados_intermedios = []
        for n in range(num_niveles):
            if n == 0 and cuerpos[c] <= niveles[0]:
                resultados_intermedios.append(1)
            elif n == 0 and cuerpos[c] >= niveles[1]:
                resultados_intermedios.append(0)
            elif n == 0:
                resultados_intermedios.append((niveles[1] - cuerpos[c]) / (niveles[1] - niveles[0]))
            elif n == (num_niveles - 1) and cuerpos[c] >= niveles[num_niveles-1]:
                resultados_intermedios.append(1)
            elif n == (num_niveles - 1) and cuerpos[c] <= niveles[num_niveles-2]:
                resultados_intermedios.append(0)
            
            elif n == (num_niveles - 1):
                resultados_intermedios.append((cuerpos[c] - niveles[num_niveles-2] ) / (niveles[num_niveles-1] - niveles[num_niveles-2]))
            elif cuerpos[c] <= niveles[n-1] or cuerpos[c] >= niveles[n+1]:
                resultados_intermedios.append(0)
            elif cuerpos[c] <= niveles[n] and cuerpos[c] >= niveles[n-1]:
                resultados_intermedios.append( (cuerpos[n] - niveles[n-1] ) / (niveles[n] - niveles[n-1]))
            else:
                resultados_intermedios.append( (niveles[n+1] - cuerpos[c]) / (niveles[n+1] - niveles[n]))
            
        resultados.append(resultados_intermedios)

    return resultados


def run():
    print(NIVELES)
    print(CUERPOS)
    print(grey_clustering(NIVELES, CUERPOS))
    print(grey_clustering_2(NIVELES, CUERPOS))

if __name__ == "__main__":
    run()


