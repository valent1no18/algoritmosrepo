def euclides(a, b):
    """
    Función que calcula el Máximo Común Divisor (MCD) de dos números enteros positivos
    utilizando el algoritmo de Euclides.
    """
    if b == 0: 
        return a 
    else:
        return euclides(b, a % b) #b es el nuevo a y a % b es el nuevo b


def MCM(a, b):
    """
    Función que calcula el Mínimo Común Múltiplo (MCM) de dos números enteros positivos
    utilizando la relación entre MCD y MCM.
    """
    mcd= euclides(a, b)

    return (a * b) // mcd #MCM(a,b) = (a*b)/MCD(a,b)


num_a= 48
num_b= 18
mcm = MCM(num_a,num_b)
print(f'El MCM de {num_a} y {num_b} es: {mcm}')
