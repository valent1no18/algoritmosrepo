#n * m= n * producto(n, m - 1) --> producto(n, m) m = 1 = n

def producto(n,m):
    
    if m == 1:
        return n
    else:
        return n + producto(n, m - 1)
    
print("producto:", producto(2,1))


