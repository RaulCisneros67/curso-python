import hashlib


tarjeta = 123456
nip = 4819
monto = 5000




datos = int(input("Numero de tarjeta: "))


salida = hashlib.sha256(b"").hexdigest()
print(salida)

if datos == tarjeta:
    print("bienvenido señor Raul gilberto")
    con = int(input("Nip: "))
    if con == nip:
        print(f"Acceso correcto este es su monto: {monto}MXN ")
    else:
        print("El nip es incorrecto")
else:
    print("El numero de targeta no existe")


