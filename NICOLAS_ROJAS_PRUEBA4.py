'''NOTA: en los ejemplos, las letras con negrita y en rojo significan que son datos
ingresados por teclado.
Haga un programa que permita generar un menú de reservas para la tienda
“Zapatillas Strike”. El menú principal debe permitir mostrar 4 opciones:
TOTEM AUTOATENCIÓN RESERVA STRIKE
1.- Reservar zapatillas
2.- Buscar zapatillas reservadas.
3.- Ver stock de reservas.
4.- Salir.
Todas las opciones del menú deben estar implementadas mediante funciones
separadas del código principal (main).
Al ingresar a la opción 1.- Comprar entrada, se debe permitir ingresar
nombre de comprador y s elección de función por separado. Para que la
compra sea exitosa se debe cumplir lo siguiente:
a) El nombre de comprador no debe estar repetido,
b) Para realizar la reserva el cliente, debe digitar la frase secreta
“EstoyEnListaDeReserva” respetando las mayúsculas y minúsculas.
c) hay un stock máximo de 20 reservas, solo una reserva por comprador.
En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
Al ingresar la opción 2.- Buscar zapatillas reservadas, el menú debe permitir
buscar las reservas mediante el nombre. Si la reserva existe, preguntar si pagar un
adicional por la reserva VIP, el cual permite reservar 2 pares de zapatillas
2
Al ingresar la opción 3.- Ver Stock de reservas, el menú debe permitir observar el
stock de zapatillas ya reservadas y cuantas quedan por reservar.
Al ingresar la opción 4.- Salir, el programa debe terminar mostrando:
Programa terminado...
Si se ingresa una opción distinta (que no sea 1, 2, 3 o 4), debe mostrarse:
Debe ingresar una opción válida!!'''





stock_total = 20
reservas = {}  # Diccionario: nombre -> cantidad (1 o 2)

frase_secreta = "EstoyEnListaDeReserva"

while True:
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print("-- Reservar Zapatillas --")
        nombre = input("Nombre del comprador: ")
        clave = input("Digite la palabra secreta para confirmar la reserva: ")
        if clave != frase_secreta:
            print("Error: palabra clave incorrecta. Reserva no realizada.")
        elif nombre in reservas:
            print(f"{nombre} ya tiene una reserva.")
        elif stock_total >= 1:
            reservas[nombre] = 1
            stock_total -= 1
            print(f"Reserva realizada exitosamente para {nombre}.")
        else:
            print("No hay stock disponible para nuevas reservas.")

    elif opcion == "2":
        print("-- Buscar Zapatillas Reservadas --")
        nombre = input("Nombre del comprador a buscar: ")
        if nombre in reservas:
            cantidad = reservas[nombre]
            tipo = "VIP" if cantidad == 2 else "estándar"
            print(f"Reserva encontrada: {nombre} - {cantidad} par(es) ({tipo}).")
            if cantidad == 1:
                vip = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
                if vip == "s":
                    if stock_total >= 1:
                        reservas[nombre] = 2
                        stock_total -= 1
                        print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
                    else:
                        print("No hay stock suficiente para actualizar a VIP.")
                else:
                    print("Manteniendo reserva actual.")
        else:
            print("No se encontró ninguna reserva con ese nombre.")

    elif opcion == "3":
        print("-- Ver Stock de Reservas --")
        reservados = sum(reservas.values())
        disponibles = 20 - reservados
        print(f"Pares reservados: {reservados}")
        print(f"Pares disponibles: {disponibles}")

    elif opcion == "4":
        print("Programa terminado.")
        break

    else:
        print("Debe ingresar una opción válida!!")
