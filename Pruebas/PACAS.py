print("------------------PACAS:)----------------------------")
pacas = int(input("Precio de la paca: "))
print("-----------------------------------------------------")

#Variable precio Dollar
a = 20

#Primero calculamos lo que vale la paca y multiplicamos por el precio del dolar
calculo = pacas * a
resultado = print(f"El precio en pesos es: {calculo} MXN")
print("-----------------------------------------------------")

#Dividimos el precio de la paca por la cantidad de piezas que tiene
pza = int(input("Cuantas piezas tiene la paca?: "))

cant = calculo // pza
print("-----------------------------------------------------")

Pre = print(f"Este es el precio de cada una de las piezas: {cant} MXN")
print("-----------------------------------------------------")

#Multiplicamos el precio de la pieza que nosotros otorgamos por la cantidad de piezas que tiene la paca
con = int(input("Precio de la pieza?: "))

lop = con * 3
loop= print(f"Su ganancia triplicada seria: {lop}")



gan = lop * pza
sum = gan - calculo

print("-----------------------------------------------------")

res = print(f"Su ganancia estimada seria de: {sum}MXN")
print(f"La suma de su ganancia mas gasto de compra da un total de: {gan}MXN")




print("-----------------------------------------------------")



if gan >= 200000:
    print("Usted es rico su negocio va fluyendo de maravilla felicidades :)")
elif gan >= 60000:
    print("Usted esta alcanzando la fortuna señor") 
elif gan >= 40000:
    print("Usted va muy bien siga asi")
elif gan >= 20000:
    print("Hay la lleva que buena inversion esta logrando")
elif gan >= 15000:
    print("usted sigale de algo se empieza")
elif gan >= 7000:
    print("Buena eleccion para empezar a emprender")
else:
    print("execelente manera de pensar buen negocio")











