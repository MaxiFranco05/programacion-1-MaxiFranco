##Ejercicios de Tarea - Condicionales
from condicionales_py.utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero, pedir_float,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)
from colorama import init, Fore, Style
import sys
#Ejercicio 1 — Clasificación de impuestos
def ejercicio_1():
    nombre = pedir_texto("Inserte su nombre completo: ")
    edad = pedir_entero("Inserte su edad: ", 13, 110)
    ingreso = pedir_float("Inserte el total de sus ingresos anuales: ", 0.0)
    mayor = edad > 65
    tax = 0.0

    if ingreso < 500000:
        print(f"Nombre: {nombre}\nIngresos: ${ingreso}\nEdad:{edad} años\nImpuesto Anual: $0.0")
        info("No debe pagar impuestos.")
    elif 500000 <= ingreso < 2000000:
        tax = 0.05 if mayor else 0.1
        print(f"Nombre: {nombre}\nIngresos: ${ingreso}\nEdad:{edad} años\nImpuestos: ${ingreso*tax}")
        warn("Debe pagar el 10""%"" de sus ingresos.")
        if mayor:
            info("Al ser mayor de 65 años, su impuesto se reduce al 50%")
    elif 2000000 <= ingreso < 5000000:
        tax = 0.1 if mayor else 0.2
        print(f"Nombre: {nombre}\nIngresos: ${ingreso}\nEdad:{edad} años\nImpuestos: ${ingreso*tax}")
        warn("Debe pagar el 20""%"" de sus ingresos.")
        if mayor:
            info("Al ser mayor de 65 años, su impuesto se reduce al 50%")
    elif 5000000 <= ingreso:
        tax = 0.175 if mayor else 0.35
        print(f"Nombre: {nombre}\nIngresos: ${ingreso}\nEdad:{edad} años\nImpuestos: ${ingreso*tax}")
        warn("Debe pagar el 35""%"" de sus ingresos.")
        if mayor:
            info("Al ser mayor de 65 años, su impuesto se reduce al 50%")

#Ejercicio 2 — Sistema de calificaciones con promoción
def ejercicio_2():
    nombre = pedir_texto("Inserte su nombre: ")
    legajo = pedir_entero("Inserte número de legajo: ", 0)
    notas = []

    for i in range(0, 3):
        notas.append(pedir_float(f"Inserte su nota #{i+1}: ", 0, 10))
    promedio = (sum(notas) / 3)
    if promedio < 4:
        print("Promedio: ", promedio)
        error("Desaprobado directo.")
    elif promedio < 6:
        print("Promedio: ", promedio)
        error("Desaprobado.")
    elif 6 < promedio < 7:
        print("Promedio: ", promedio)
        warn("Aprobado con final.")
    elif promedio >= 8:
        print("Promedio: ", promedio)
        ok("Promocionado.")

#Ejercicio 3 — Simulador de cajero automático
def ejercicio_3():
    pin_real = 1234
    count = 0
    nombre = pedir_texto("Inserte nombre de usuario: ")
    pin = pedir_entero("Inserte PIN (4 dígitos): ",None,9999)
    while 5 <= len(str(pin)) < 4 or pin != pin_real:
        pin = pedir_entero(Fore.RED + Style.BRIGHT + 
        f"Inserte el PIN correcto o uno válido (quedan {3 - count} intentos): " + Fore.RESET + Style.RESET_ALL, None, 9999)
        if pin == pin_real:
            break
        count += 1
        if count == 3:
            sys.exit(Fore.RED + Style.BRIGHT + "¡Alcanzaste el máximo de intentos!")
    saldo = pedir_entero("Indique saldo de su cuenta: ", 1000)
    while saldo % 1000 != 0:
        saldo = pedir_entero(Fore.RED + "ERROR: " + Fore.RESET + "Inserte un valor divisible por 1000: ")
    def retirar(saldo):
        print(Fore.GREEN + Style.BRIGHT + f"¡BIENVENIDO {nombre.upper()}!" + Fore.RESET + Style.RESET_ALL + f"\nSu saldo disponible es: ${saldo}")
        if saldo >= 1000:
            retiro = pedir_entero(Fore.CYAN +"¿Cuánto desea retirar?: " + Fore.RESET + Style.RESET_ALL, 1000, saldo)
            if retiro % 1000 == 0:
                if retiro > 20000:
                    if confirmar(Fore.CYAN + "¿Desea confirmar? (s/n) " + Fore.LIGHTBLACK_EX + Style.DIM +"\n(Su retiro supera los $20.000 y requiere una comisión del 2%): " + Fore.RESET + Style.RESET_ALL):
                        saldo -= retiro + (retiro * 0.02)
                elif confirmar(Fore.CYAN + "¿Desea confirmar? (s/n): " + Fore.RESET + Style.RESET_ALL):
                    saldo -= retiro
            else:
                print(Fore.RED + Style.BRIGHT + "¡Solo puede retirar múltiplos de 1000!\nej. 1000/2000/.../10000/etc.")
        print(Fore.CYAN + Style.BRIGHT + "¡Muchas gracias por operar con nostros!" + Fore.RESET + Style.RESET_ALL + f"\nSu saldo final es: ${saldo}")
        if confirmar("¿Desea hacer otro retiro?: "):
            retirar(saldo)
    saldo = retirar(saldo)

