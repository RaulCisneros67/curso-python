#***********************SIRVE PARA LEER VALORES DEL TECLADO*********************************************

print('Quieres saber tu masa corporal?')
respuesta = input()

if respuesta =='si':


    print('Ingresa tu estatura')
    a = c = float(input())

    print('Ingresa tu peso')
    p = d = int(input())





    c = a**2
    d = p // c







    print('Calculando......')
    print('Tu masa corporal es:' , d)
    
    if d >= 24:
        print("Tienes sobre peso")

        if d <= 15:
            print("Tu peso es demasiado bajo")

        elif d == 20:
            print("es tu peso ideal")

        else:
            print("necesitas ir al medico")

    else:

      print("Estas en tu masa corporal ideal")
    
else:
    print("ADios PAAA")


