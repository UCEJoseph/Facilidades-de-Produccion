# Universidad Central del Ecuador
# Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental
# Carrera de Petróleos
# Integrantes: Allison Donoso, Joseph Pacheco, Karen Zhangallimbay
# Tema: Concentraciones

# Que volumen de demulsificante y biocida para un bache de 3 horas, se deben inyectar desde una plataforma que produce Qf (BFPD) 
# con el %BSW de agua y en que tiempo llegará un pig, el fluido es transportado por una tubería de (Diámetro) in, una longitud L en
# m, el fluido llega a una CPF.
# Concentación Biocida --> 500 ppm
# Cocentración Demulsificante --> 35 ppm

import pandas as pd

Cb = 500 # Concentración Biocida
Cd = 35 # Concentración Demulsificante

# Datos ingresados por el usuario
# Caudal del fluido Qf
Qf = float(input('Ingrese el valor del caudal del fluido (Qf) en BFPD: '))
# %BSW
BSW = float(input('Ingrese el valor %BSW en porcentaje: '))
# Longitud de la tubería
L = float(input('Ingrese el valor de la longitud de la tubería en metros (m): '))
# Diámetro de tubería
D = float(input('Ingrese el valor del diámetro de la tubería en pulgadas (in): '))

# Cálculos caudal
Qw = Qf * (BSW / 100)
Qo = Qf - Qw

# Volúmenes

# Biocida
Vb = Qw * (3 / 24)
x = ((Cb * Vb) / (1000000 - Cb)) * 42

# Demulsificante
Vd = ((Cd * Qo) / (1000000 - Cd)) * 42

# Tiempo
# Conversión de variables
L2 = L * 3.28  # Transformar a ft
Qf2 = Qf * 5.615  # Transformar a ft^3
D2 = D / 12  # Transformar a ft
t = ((3.1415 / 4) * (D2 ** 2) * L2) / Qf2

# Pasar a horas
t2 = t * 24

# Resultados
print(f'El volumen de Biocida es {x:0.2f} gal/3h')
print(f'El volumen de Demulsificante es {Vd:0.2f} gal/3h')
print(f'El tiempo de llegada al PIG es {t2:0.2f} horas')