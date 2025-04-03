def caracteres_list(secuencia):
    if len(secuencia) <= 1:
        return secuencia
    else:
        return caracteres_list(secuencia[1:]) + [secuencia[0]]


characters = [1, 5, 8, 2]
reversed_list = caracteres_list(characters)
print(f'Lista original: {characters}')
print(f'Lista revertida: {reversed_list}')