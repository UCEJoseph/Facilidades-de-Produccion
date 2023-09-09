# Universidad Central del Ecuador
# Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental
# Carrera de Petróleos
# Integrantes: Joseph Pacheco
# Tema: Ley de Stokes

import math

# Entradas del usuario
bfpd = float(input("Ingrese el caudal del fluido (en BFPD): "))
bwpd = float(input("Ingrese el caudal de agua (en BWPD): "))
gravedad_api = float(input("Ingrese la gravedad API del petróleo: "))
pae = float(input("Ingrese el porcentaje de agua emulsionada (en %): "))
viscosidad_petroleo = float(input("Ingrese la viscosidad del petróleo (en cP): "))
va = float(input("Ingrese la velocidad de asentamiento de la gota (en ft/min): "))
# Cálculos

# Caudal del petróleo
bopd=bfpd-bwpd
# Emulsión
emulsion=(bopd*100)/(100-pae)
# Agua Emulsionada
AE=emulsion-bopd
# Agua Libre
AL=bwpd-AE

# Densidad del agua (g/cm^3)
da=1

# Densidad del petróleo (g/cm^3)
# Densidad relativa
drp=141.5/(131.5+gravedad_api)
dp=drp*da

# Velocidad de asentamiento de la gota de agua
# Diámetro de la gota de agua
d = math.sqrt((va * viscosidad_petroleo) / ((1.072 * 10**-4) * (da - dp)))

# Mostrar resultados
print(f"El caudal del petróleo es {bopd:0.2f} BOPD.")
print(f"La emulsión es {emulsion:0.2f} bbl.")
print(f"Agua Emulsionada {AE:0.2f} bbl.")
print(f"Agua Libre {AL:0.2f} bbl.")
print(f"El diámetro de la gota de agua en la emulsión es aproximadamente {d:0.2f} µm.")
