#creando una lista con list
lista = list(["hola","raul",35])

#devuelve la cantidad de elementos de la lista
cadena = "hola"
cantidad_elementos = len(cadena)

print(cantidad_elementos)


#agreganto un elemento ala lista
lista.append("JAJAJAJA")

#agregando un elemento ala lista en un indice especifico
lista.insert(2,"Toma papa")

#agregando varios elementos ala lista
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice), eliminar el ultimo elemento o ante ultimo(-1)(-2)
lista.pop(0)

#removiendo un elemnto de la lista por  su valor
lista.remove("Toma papa") 

#ordenanando la lista (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

elemento_encontrado = lista.index(35)

print(lista)