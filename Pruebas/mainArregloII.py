#edades = [20, 41, 6, 18, 23]
##Ejemplo 1#####

#recorriendo los elementos

# for edad in edades:
#     print(edad)
    
# #recorriendo los índices    
# for i in range(len(edades)):
#     print(edad[i])

# #con while y los índices    
# indice = 0 

# while indice < len(edades):
#     print(edades[indice])
#     indice +=1












   
##Ejemplo 2####

#creamos las listas (vacias al comienzo)

nombres = []
identificadores = []

#Definimos el tamaño para las listas 
#Lo puedes cambiar si quieres 

tamaño = 3

#Leemos los datos y los agregamos a la lista

    
for i in range(tamaño):
    print("Ingrese los datos de la persona porfavor")
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")
    
    nombres.append(nombre)
    identificadores.append(identificación)
    
#Ahora mostramos las listas
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)
    
print("Nombre:", nombres[i])
print("Identificación:", identificadores[i])
     