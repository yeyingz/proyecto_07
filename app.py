
import pandas as pd
import plotly.express as px
import streamlit as st

ruta_vehicles = 'vehicles_us.csv'  # Ruta del archivo CSV
# Cargar el archivo CSV en un DataFrame de pandas
try:
    # Leer el archivo CSV: vehicls_us.csv
    car_data = pd.read_csv(ruta_vehicles)
except FileNotFoundError:
    print(f"Error: El archivo {ruta_vehicles} no se encuentra.")
    exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: El archivo {ruta_vehicles} está vacío.")
    exit(1)


st.header("Aálisis de datos de automóviles en US")  # Encabezado

# checkbok para construir histograma
build_histogram = st.checkbox('Construir histograma')

if build_histogram:
    # Escribir mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# checkbok para construir gráfico de dispersión
build_dispersion = st.checkbox('Construir gráfico de dispersión')

if build_dispersion:
    # Escribir mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
