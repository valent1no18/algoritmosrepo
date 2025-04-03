def caracteres_list(string):
    if not string:
        return 0
    else:
        list_characters = caracteres_list(string[0])
        return list_characters + caracteres_list(string[::-1]) 
    
#:: Selecciona todos los elementos de la cadena.
#:: Omitir el índice de inicio (comienza desde el principio).
#-1: Indica un paso de -1, lo que significa que itera a través de la cadena desde el final hacia el principio.




print( caracteres_list('-/+'))