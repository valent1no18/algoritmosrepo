#n * m= n * producto(n, m - 1) --> producto(n, m) m = 1 = n

def producto(n,m):
    
    if m == 1:
        return n
    else:
        return n + producto(n, m - 1)
    
print(producto(2,1))


#potencia(m, n)= m ** potencia(m, n - 1) --> ptencia