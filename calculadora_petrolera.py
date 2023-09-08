# Universidad Central del Ecuador
# Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental
# Carrera de Petróleos
# Integrantes: Allison Donoso & Joseph Pacheco
# Tema: Calculadora Petrolera

def convertir_volumen(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "m3": 1,
        "ft3": 0.0283168,
        "gal": 0.00378541,
        "L": 0.001
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_tasa_de_flujo(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "m3/s": 1,
        "ft3/min": 4.719474432e-5,
        "L/s": 0.001
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_densidad(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "kg/m3": 1,
        "g/cm3": 1000
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_presion(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "Pa": 1,
        "bar": 1e5,
        "psi": 6894.76
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_temperatura(valor, desde_unidad, hacia_unidad):
    if desde_unidad == "C":
        if hacia_unidad == "F":
            return valor * 9/5 + 32
        elif hacia_unidad == "K":
            return valor + 273.15
    elif desde_unidad == "F":
        if hacia_unidad == "C":
            return (valor - 32) * 5/9
        elif hacia_unidad == "K":
            return (valor + 459.67) * 5/9
    elif desde_unidad == "K":
        if hacia_unidad == "C":
            return valor - 273.15
        elif hacia_unidad == "F":
            return valor * 9/5 - 459.67

def convertir_longitud(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "m": 1,
        "ft": 0.3048,
        "in": 0.0254,
        "cm": 0.01
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_area(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "m2": 1,
        "acres": 0.000247105,
        "ft2": 10.7639
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]


# Solicitar al usuario los datos de conversión
print("Bienvenido al convertidor de unidades")
print("Por favor, seleccione el tipo de conversión:")
print("1. Volumen")
print("2. Tasa de flujo")
print("3. Densidad")
print("4. Presión")
print("5. Temperatura")
print("6. Longitud")
print("7. Área (acres)")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    desde_unidad = input("Ingrese la unidad de volumen de origen (ejemplo: m3, gal, L, ft3): ")
    hacia_unidad = input("Ingrese la unidad de volumen de destino (ejemplo: m3, gal, L, ft3): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_volumen(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 2:
    desde_unidad = input("Ingrese la unidad de tasa de flujo de origen (ejemplo: m3/s, ft3/min, L/s): ")
    hacia_unidad = input("Ingrese la unidad de tasa de flujo de destino (ejemplo: m3/s, ft3/min, L/s): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_tasa_de_flujo(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 3:
    desde_unidad = input("Ingrese la unidad de densidad de origen (ejemplo: kg/m3, g/cm3): ")
    hacia_unidad = input("Ingrese la unidad de densidad de destino (ejemplo: kg/m3, g/cm3): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_densidad(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 4:
    desde_unidad = input("Ingrese la unidad de presión de origen (ejemplo: Pa, bar, psi): ")
    hacia_unidad = input("Ingrese la unidad de presión de destino (ejemplo: Pa, bar, psi): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_presion(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 5:
    desde_unidad = input("Ingrese la unidad de temperatura de origen (ejemplo: C, F, K): ")
    hacia_unidad = input("Ingrese la unidad de temperatura de destino (ejemplo: C, F, K): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_temperatura(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 6:
    desde_unidad = input("Ingrese la unidad de longitud de origen (ejemplo: m, ft, in, cm): ")
    hacia_unidad = input("Ingrese la unidad de longitud de destino (ejemplo: m, ft, in, cm): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_longitud(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 7:
    desde_unidad = input("Ingrese la unidad de área de origen (ejemplo: m2, acres, ft2): ")
    hacia_unidad = input("Ingrese la unidad de área de destino (ejemplo: m2, acres, ft2): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_area(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 7 para realizar una conversión.")










