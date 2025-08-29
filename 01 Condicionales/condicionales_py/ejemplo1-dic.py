PLANES = {"estandar": 100000.0, "premium": 140000.0}
MODALIDADES = {"presencial": 1.0, "virtual": 0.9}

plan = input("Ingrese el plan (estandar/premium): ").lower()
modalidad = input("Ingrese la modalidad (presencial/virtual): ").lower()

if plan in PLANES and modalidad in MODALIDADES:
    precio = PLANES[plan]
    precio_final = precio * MODALIDADES[modalidad]
    print(f"El precio final es: ${precio_final}")
else:
    print("Plan o modalidad inválida")
