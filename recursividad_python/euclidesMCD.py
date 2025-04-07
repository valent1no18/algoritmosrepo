def euclides(a, b):
    """
    Función que calcula el Máximo Común Divisor (MCD) de dos números enteros positivos
    utilizando el algoritmo de Euclides.
    """
    if b == 0: 
        return a 
    else:
        return euclides(b, a % b) #b es el nuevo a y a % b es el nuevo b

num_a= 48
num_b= 18
mcd = euclides(num_a,num_b) 
print(f'El MCD de {num_a} y {num_b} es: {mcd}')