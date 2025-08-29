plan = input("Ingrese el plan (estandar/premium): ").lower()
modalidad = input("Ingrese la modalidad (presencial/virtual): ").lower()

if plan == "estandar":
    precio = 100000
    if modalidad == "presencial":
        precio_final = precio
    elif modalidad == "virtual":
        precio_final = precio * 0.9
    else:
        print("Modalidad inválida")
        precio_final = None
elif plan == "premium":
    precio = 140000
    if modalidad == "presencial":
        precio_final = precio
    elif modalidad == "virtual":
        precio_final = precio * 0.9
    else:
        print("Modalidad inválida")
        precio_final = None
else:
    print("Plan inválido")
    precio_final = None

if precio_final:
    print(f"El precio final es: ${precio_final}")
