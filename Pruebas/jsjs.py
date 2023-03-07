array = [{
    'Producto':'Coca',
    'Imagen':'Img/coca.jpg',
    'Precio': 35
},
         {
    'Producto':'gancito',
    'Imagen':'Imgjj/gancito.jpg',
    'Precio': 15
},
         {
    'Producto':'Sabritas',
    'Imagen':'Imggg/sabritas.jpg',
    'Precio': 18
}]

print("Bienvenido")
Pre = input("Que producto desea comprar: ")
for i in array:
    if Pre == i['Producto']:
        print(i['Precio'])
        print(i['Imagen'])
        


     

Res = input("Desea comprar el producto?: ")




if Res == 'si':
    monto = int(input("Con cuanto pagara: "))
    cambio = i['Precio'- monto] 
    print(f"Su cambio seria: {cambio}")



   
