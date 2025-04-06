def cantdigitos(n):
    if n==0:
        return 0
    else:
        return 1 + cantdigitos(n//10) # n//10 elimina el último dígito del número en cada llamada recursiv
    
digitos= 345
cantidad = cantdigitos(digitos)
print(f'La cantidad de digitos en el numero {digitos} es: {cantidad}')
