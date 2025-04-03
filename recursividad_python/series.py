def calculo_serie(n):
    if n==1:
        return 1
    elif n>1:
        return calculo_serie(n-1) + 1/n
    

n_terinos = 3
resultado = calculo_serie(n_terinos)
print(f"El resultado de la serie es: {resultado}")




    