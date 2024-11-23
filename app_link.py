import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

URL = "https://datos.gob.cl/uploads/recursos/temperatura2014-csv.csv"
df = pd.read_csv(URL, sep= ';')

# Crear un diccionario para renombrar las columnas
new_column_names = {
    df.columns[0]: 'locación',
    df.columns[1]: 'mes',
    df.columns[2]: 'dia',
    df.columns[3]: 'temp mas baja',
    df.columns[4]: 'temp mas alta'
}

# Renombrar las columnas del DataFrame
df = df.rename(columns=new_column_names)

# Título de la app en Streamlit
st.title('Análisis de Temperaturas por Locación')

# Descripción de la app
st.write("""
    Esta aplicación muestra el análisis de las temperaturas en varias locaciones de Chile durante el año 2014.
    Los gráficos muestran las locaciones con las temperaturas más bajas y altas, así como el promedio de temperatura 
    para cada locación, además de un análisis mensual de las temperaturas.
""")

# Gráfico 1: Top 10 Locaciones con la Temperatura Más Baja
st.header('1. Top 10 Locaciones con la Temperatura Más Baja')
top_10_bajas = df[['locación', 'temp mas baja']].drop_duplicates().sort_values(by='temp mas baja', ascending=True).head(10)
fig1, ax1 = plt.subplots()
ax1.bar(top_10_bajas['locación'], top_10_bajas['temp mas baja'], color='blue')
ax1.set_title('Top 10 Locaciones con la Temperatura Más Baja')
ax1.set_xlabel('Locación')
ax1.set_ylabel('Temperatura (°C)')
ax1.tick_params(axis='x', rotation=90)
st.pyplot(fig1)

# Gráfico 2: Top 10 Locaciones con la Temperatura Más Alta
st.header('2. Top 10 Locaciones con la Temperatura Más Alta')
top_10_altas = df[['locación', 'temp mas alta']].drop_duplicates().sort_values(by='temp mas alta', ascending=False).head(10)
fig2, ax2 = plt.subplots()
ax2.bar(top_10_altas['locación'], top_10_altas['temp mas alta'], color='red')
ax2.set_title('Top 10 Locaciones con la Temperatura Más Alta')
ax2.set_xlabel('Locación')
ax2.set_ylabel('Temperatura (°C)')
ax2.tick_params(axis='x', rotation=90)
st.pyplot(fig2)

# Gráfico 3: Promedio de Temperaturas (Baja + Alta) por Locación (Top 50)
st.header('3. Top 50 Promedio de Temperaturas por Locación')
df['promedio_temp'] = (df['temp mas baja'] + df['temp mas alta']) / 2
top_50_promedio = df[['locación', 'promedio_temp']].drop_duplicates().sort_values(by='promedio_temp', ascending=True).head(50)  # Top 50
fig3, ax3 = plt.subplots()
ax3.bar(top_50_promedio['locación'], top_50_promedio['promedio_temp'], color='green')
ax3.set_title('Top 50 Promedio de Temperaturas por Locación')
ax3.set_xlabel('Locación')
ax3.set_ylabel('Temperatura Promedio (°C)')
ax3.tick_params(axis='x', rotation=90)
st.pyplot(fig3)

# Gráfico 4: Temperatura más baja promedio por mes
st.header('4. Temperatura Más Baja Promedio por Mes')
avg_temp_baja_por_mes = df.groupby('mes')['temp mas baja'].mean()
fig4, ax4 = plt.subplots()
avg_temp_baja_por_mes.plot(kind='bar', color='blue', ax=ax4)
ax4.set_title('Temperatura Más Baja Promedio por Mes')
ax4.set_xlabel('Mes')
ax4.set_ylabel('Temperatura (°C)')
st.pyplot(fig4)

# Gráfico 5: Comparación de temperaturas más baja y más alta por mes
st.header('5. Comparación de Temperaturas Más Baja y Más Alta Promedio por Mes')
avg_temp_baja_y_alta_por_mes = df.groupby('mes')[['temp mas baja', 'temp mas alta']].mean()
fig5, ax5 = plt.subplots()
avg_temp_baja_y_alta_por_mes.plot(kind='bar', color=['blue', 'red'], ax=ax5)
ax5.set_title('Temperatura Baja y Alta Promedio por Mes')
ax5.set_xlabel('Mes')
ax5.set_ylabel('Temperatura (°C)')
st.pyplot(fig5)

# Agregar interactividad adicional (opcional)
st.sidebar.header('Filtros de Análisis')
selected_month = st.sidebar.selectbox('Selecciona un mes', df['mes'].unique())
filtered_data = df[df['mes'] == selected_month]

# Mostrar datos filtrados en la interfaz
st.sidebar.write(f"Mostrando datos para el mes {selected_month}")
st.sidebar.write(filtered_data)

# Cambiar color de fondo de la página usando CSS
st.markdown(
    """
    <style>
    body {
        background-color: #fcd0ed;
    }
    </style>
    """, unsafe_allow_html=True
    )