def logaritmo(n,b):   #n= numero entero, b= base
    if n<b:
        return 0 #si el numero es menor que la base, el logaritmo es 0
    else:
        return 1 + logaritmo(n/b,b) #se divide el numero entre la base y se suma 1 al resultado de la llamada recursiva


numero = 10
base = 2 
print(f'El logaritmo de {numero} de base {base} es: {logaritmo(numero,base)}')