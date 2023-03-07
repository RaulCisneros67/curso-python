#Le pedimos al usuario que nos diga una frace (o varias)
frase = input("Dime algo pibe y te calculo cuanto tardarias si tuvieras que deciarla: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en una lista 
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para wey no es diccionario")
    

#Calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diria en {cantidad_de_palabras/2*1.3} segundos en decirlo')


