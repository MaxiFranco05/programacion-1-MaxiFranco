# -*- coding: utf-8 -*-
from utiles_es import (
    titulo, ok, error, warn, info,
    pedir_texto, pedir_opcion, pedir_entero,
    pedir_email, pedir_cuit, confirmar, FlujoCancelado
)

PLANES = {"estandar": 100000.0, "premium": 140000.0}
MODALIDADES = {"presencial": 1.0, "virtual": 0.9}
MEDIOS_PAGO = {
    "transferencia": {"descuento": 0.05, "recargo": 0.0},
    "debito": {"descuento": 0.02, "recargo": 0.0},
    "credito": {"descuento": 0.0, "recargo": 0.07}
}

def calcular_costo(plan, modalidad, medio, tiene_beca, porc_beca, cuotas):
    base = PLANES[plan] * MODALIDADES[modalidad]
    imponible = base

    # beca
    if tiene_beca:
        imponible *= (1 - porc_beca/100.0)

    # medio de pago
    desc = MEDIOS_PAGO[medio]["descuento"]
    rec = MEDIOS_PAGO[medio]["recargo"]
    if desc > 0:
        imponible *= (1 - desc)
    elif rec > 0:
        imponible *= (1 + rec)

    # percepción fija 2%
    total = imponible * 1.02
    cuota = total / cuotas
    return base, imponible, total, cuota

def formulario_inscripcion():
    titulo("Formulario de inscripción — escriba 'CANCELAR' para salir")

    try:
        nombre = pedir_texto("Nombre y apellido: ")
        email = pedir_email("Email: ")
        cuit = pedir_cuit("CUIT/CUIL (ej 20-12345678-9): ")

        plan = pedir_opcion("Plan (estandar/premium): ", PLANES.keys())
        modalidad = pedir_opcion("Modalidad (presencial/virtual): ", MODALIDADES.keys())
        medio = pedir_opcion("Medio de pago (transferencia/debito/credito): ", MEDIOS_PAGO.keys())

        tiene_beca = pedir_opcion("¿Tiene beca? (si/no): ", ["si", "no"]) == "si"
        porc_beca = 0
        if tiene_beca:
            porc_beca = pedir_entero("Porcentaje de beca (0-100): ", minimo=0, maximo=100)

        cuotas = 1
        if medio == "credito":
            cuotas = pedir_entero("Cantidad de cuotas (1-12): ", minimo=1, maximo=12)

        base, imponible, total, cuota = calcular_costo(plan, modalidad, medio, tiene_beca, porc_beca, cuotas)

        titulo("Resumen de inscripción")
        print(f"Alumno: {nombre}")
        print(f"Email: {email}")
        print(f"CUIT: {cuit}")
        print(f"Plan: {plan} | Modalidad: {modalidad} | Medio de pago: {medio}")
        print(f"Beca: {'Sí' if tiene_beca else 'No'} {f'({porc_beca}%)' if tiene_beca else ''}")
        print(f"Cuotas: {cuotas}")

        ok("Costo calculado correctamente")
        print(f"  Base:               ${base:,.2f}")
        print(f"  Imponible:          ${imponible:,.2f}")
        print(f"  Total con percepción: ${total:,.2f}")
        print(f"  Valor por cuota:    ${cuota:,.2f}")

        if confirmar("¿Confirmar inscripción? (s/n): "):
            ok("¡Inscripción confirmada!")
        else:
            warn("Inscripción cancelada por el usuario.")

    except FlujoCancelado:
        error("El usuario canceló el formulario.")

if __name__ == "__main__":
    formulario_inscripcion()
