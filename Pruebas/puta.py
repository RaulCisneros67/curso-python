edad = 19
cartilla = False
#if anidado (Validar si se cumple una condicion anterior)

if (edad >= 19):
    print("Ya puedes tomar")

    if (cartilla == True):
        print("ya cumples con todo")
    elif (cartilla == False):
        print("Sacate la verga")
        
    else :
        print("no puedes tomar")
        
else:
    print("No eres mayor de edad")