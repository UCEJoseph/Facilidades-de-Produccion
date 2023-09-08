# Universidad Central del Ecuador
# Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental
# Carrera de Petróleos
# Integrantes: Allison Donoso, Joseph Pacheco, Karen Zhangallimbay
# Tema: Precio del Petróleo

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Ruta Completa

ruta_del_archivo = "C:/Users/PERSONAL/Documents/Python/Data_Histórica_Petróleo_2013-2023.xlsx"
data_hpet = pd.read_excel(ruta_del_archivo)  # Cambio en la lectura del archivo

# Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(data_hpet['Fecha'], data_hpet['Último'], label='Último')
plt.plot(data_hpet['Fecha'], data_hpet['Máximo'], label='Máximo')
plt.plot(data_hpet['Fecha'], data_hpet['Mínimo'], label='Mínimo')
plt.title('Datos Históricos Petróleo [2013-2023]')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.legend()
plt.show()

# Seaborn
plt.figure(figsize=(10, 6))
sns.set(style="darkgrid")  # Estilo de Seaborn
sns.lineplot(data=data_hpet, x='Fecha', y='Último', label='Último')
sns.lineplot(data=data_hpet, x='Fecha', y='Máximo', label='Máximo')
sns.lineplot(data=data_hpet, x='Fecha', y='Mínimo', label='Mínimo') 
plt.title('Datos Históricos Petróleo [2013-2023]')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.legend()
plt.show()

# Plotly
fig2 = px.line(data_hpet, x='Fecha', y=['Último', 'Máximo', 'Mínimo'],
              title='Datos Históricos Petróleo [2013-2023]', labels={'Fecha': 'Fecha', 'value': 'Precio'})

fig2.update_layout(xaxis_title='Fecha', yaxis_title='Precio ($)')
fig2.show()


