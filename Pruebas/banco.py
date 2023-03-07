        
print("Menu")
print("---------------------------")
print("1.-Retiro")
print("2.-Depositos")
print("3.-Consultas")
print("0.-Salir")
opcion = int(input("Indique la opcion: "))

while opcion !=0:  
   if(opcion == 1):
     print("Realice su retiro")
   elif(opcion == 2):
     print("Realice su deposito")
   elif(opcion == 3):
     print("Realice su consulta deseada")
   
                
print("saliste del menu")


                



monto = 5000

co = monto 


Retiro = opcion == 1 
print("tu saldo es de:" , monto)

print("Deseas hacer un retiro?")
respuesta = input()




if respuesta == 'si':
        print("Cantidad a retirar")
        dinero = int(input())
        
        print("Tu saldo restante es")
        print(dinero-co)
    
else:
    print("no tienes dinero")
    
    
