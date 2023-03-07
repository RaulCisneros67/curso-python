diccionario = {
    "nombre" : 'Raul',
    "apellido" : 'Cisneros',
    "subs" : 1000000
    
}


#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un objeto con get(), (si no encuentra nada el programa continua)
valor_de_nombre = diccionario.get("nombre")

#eliminando todo del diccionario
diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(valor_de_nombre)