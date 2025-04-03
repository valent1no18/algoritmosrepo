def deci_bin(n):
    if n==0:  
        return '0'
    elif n==1:
        return '1'
    else:
        return deci_bin(n//2) + str(n%2) #el str(n%2) es para convertir resto de la division en un string y concatenarlo al resultado de la llamada recursiva
num_decimal = 10
num_binario = deci_bin(num_decimal)
print(f'El numero decimal {num_decimal} en binario es: {num_binario}')
