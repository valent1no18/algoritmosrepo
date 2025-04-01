
#potencia(m, n)= m ** potencia(m, n - 1) --> potencia(m, n) n = 1 = m

def potencia(m,n):
    
    if n == 1:
        return m
    else:
        return m * potencia(m, n - 1)
    
print("potencia:", potencia(2,1))