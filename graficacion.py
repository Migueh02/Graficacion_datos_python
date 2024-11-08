import pymongo
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ejercicio_graficacion"]
collection = db["datos"]

# Obtener datos de la colección y convertirlos en un DataFrame
data = list(collection.find({}))
df = pd.DataFrame(data)

# Verificar las columnas disponibles
print("Columnas en el DataFrame:", df.columns)

# Asegúrate de que los campos están presentes en el DataFrame
if not df.empty and 'FECHA HECHO' in df.columns and 'CANTIDAD' in df.columns:
    # Convertir la columna 'FECHA HECHO' a un formato de fecha
    df['FECHA HECHO'] = pd.to_datetime(df['FECHA HECHO'], errors='coerce')
    
    # Eliminar filas con fechas no válidas
    df.dropna(subset=['FECHA HECHO'], inplace=True)
    
    # Agrupar por fecha y sumar la cantidad
    df_grouped = df.groupby('FECHA HECHO')['CANTIDAD'].sum().reset_index()

    # Graficar los datos
    plt.figure(figsize=(10, 6))
    plt.plot(df_grouped['FECHA HECHO'], df_grouped['CANTIDAD'], marker='o')
    plt.title("Cantidad de eventos por fecha")
    plt.xlabel("Fecha")
    plt.ylabel("Cantidad")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Los campos no están presentes en los datos.")
