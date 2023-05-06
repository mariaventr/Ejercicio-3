from manejadorRegistro import ManejadorRegistro

def test():
    lista=ManejadorRegistro()
    lista.cargarDatos("Archivo.csv")
    #lista.mostrarDatos()
    while True:
        print("Bienvenido al menú de opciones")
        print("1. Mostrar para cada variable el día y hora de menor y mayor valor.")
        print("2. Indicar la temperatura promedio mensual por cada hora.")
        print("3. Lista de los valores de las tres variables para cada hora del día.")
        print("4. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            print("Mostrar para cada variable el día y hora de menor y mayor valor.")
            lista.mostrarMayoryMenor()
        elif opcion == "2":
            print("Indicar la temperatura promedio mensual por cada hora")
            lista.tempMensual()
        elif opcion == "3":
            print("Lista de los valores de las tres variables para cada hora del día dado")
            dia=int(input("Ingresasr dia: "))
            lista.obtenerValoresPorDia(dia)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

 
if __name__ == '__main__':
    test()
    
