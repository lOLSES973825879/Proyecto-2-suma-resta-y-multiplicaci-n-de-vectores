#Proyecto
#Introducción
print("Bienvenido al programa de operaciones con vectores")

#Variables
x1 = int(input("Ingrese la coordenada x del primer vector: "))
y1 = int(input("Ingrese la coordenada y del primer vector: "))
x2 = int(input("Ingrese la coordenada x del segundo vector: "))
y2 = int(input("Ingrese la coordenada y del segundo vector: "))
operación = input("Ingrese la operación que desea realizar (suma(+), resta(-), producto(*) ): ")
ses = int
En_caso_bucle = str

def operaciones(x1,y1,x2,y2,operación,ses,En_caso_bucle):
    #Iniciamos el programa
    for i in range(100):
        #En caso de suma...
        if operación == "+":
            ses = x1 + x2, y1 + y2
            ses = str(ses)
            print("Resultado es: ", ses)
        
        #En caso de resta...
        if operación == "-":
            ses = x1 - x2, y1 - y2
            ses = str(ses)
            print("Resultado es: ", ses)
        
        #En caso de multiplicación...
        if operación == "*":
            ses = x1 * x2, y1 * y2
            ses = str(ses)
            print("Resultado es: ", ses)
        
        En_caso_bucle = input("¿Desea realizar otra operación? (si(s)/no(n)): ")
        
        #En caso de que el usuario quiera hacer otra operación...
        if En_caso_bucle == "s":
            x1 = int(input("Ingrese la coordenada x del primer vector: "))
            y1 = int(input("Ingrese la coordenada y del primer vector: "))
            x2 = int(input("Ingrese la coordenada x del segundo vector: "))
            y2 = int(input("Ingrese la coordenada y del segundo vector: "))
            operación = input("Ingrese la operación que desea realizar (suma(+), resta(-), producto(*) ): ")
        
        #En caso de que el usuario no quiera hacer otra operación...
        if En_caso_bucle == "n":
            input(print("Gracias por usar mi programa, presione espacio para salir"))
            break
#Función 1

def diferente_de_enteros(x1,x2,y1,y2,operación):
    #Excepciones
    if x1 != int or y1 != int or x2 != int or y2 != int:
        print("Error, ingrese solo números enteros")
        x1 = int(input("Ingrese la coordenada x del primer vector: "))
        y1 = int(input("Ingrese la coordenada y del primer vector: "))
        x2 = int(input("Ingrese la coordenada x del segundo vector: "))
        y2 = int(input("Ingrese la coordenada y del segundo vector: "))
    
    if operación != "+" or "-" or "*":
        print("Error, ingrese una operación válida")
        operación = input("Ingrese la operación que desea realizar (suma(+), resta(-), producto(*) ): ")
#Función 2

diferente_de_enteros(x1,x2,y1,y2,operación)
operaciones(x1,y1,x2,y2,operación,ses,En_caso_bucle)