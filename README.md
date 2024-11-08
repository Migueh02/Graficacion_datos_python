Aquí tienes una documentación completa y organizada para tu proyecto en GitHub. Incluye los pasos detallados desde la creación de la base de datos en MongoDB, la importación de un archivo CSV a través de **MongoDB Compass**, y cómo visualizar los datos usando Python.

---

# Proyecto: Visualización de Datos de Destrucción de Infraestructura de Producción de Drogas

Este proyecto tiene como objetivo **visualizar y analizar datos** sobre la **destrucción de infraestructura de producción de drogas en Colombia**. Los datos fueron obtenidos de la plataforma [datos.gov.co](https://www.datos.gov.co/dataset/DESTRUCCI-N-DE-INFRAESTRUCTURA-DE-PRODUCCI-N-DE-DR/s29y-2xjd/about_data).

## Tabla de Contenidos
1. [Requisitos](#requisitos)
2. [Preparación del Entorno](#preparación-del-entorno)
3. [Creación de la Base de Datos en MongoDB](#creación-de-la-base-de-datos-en-mongodb)
4. [Importación del CSV usando MongoDB Compass](#importación-del-csv-usando-mongodb-compass)
5. [Graficación de Datos con Python](#graficación-de-datos-con-python)
6. [Referencias](#referencias)

---

## Requisitos

- **MongoDB** (Servidor y Compass)
- **Python 3.x**
- Bibliotecas de Python:
  - `pymongo`
  - `pandas`
  - `matplotlib`

Instala las bibliotecas necesarias ejecutando:
```bash
pip install pymongo pandas matplotlib
```

---

## Preparación del Entorno

Antes de comenzar, asegúrate de tener **MongoDB Compass** y **Python** instalados en tu sistema.

---

## Creación de la Base de Datos en MongoDB

1. Abre **MongoDB Compass** e inicia sesión en tu servidor de MongoDB.
2. Crea una **nueva base de datos** con el nombre:
   ```
   destruccion_infraestructura
   ```
3. Dentro de esta base de datos, crea una **colección** llamada:
   ```
   datos
   ```

---

## Importación del CSV usando MongoDB Compass

1. Descarga el archivo CSV desde el siguiente enlace:  
   [DESTRUCCIÓN DE INFRAESTRUCTURA DE PRODUCCIÓN DE DROGAS](https://www.datos.gov.co/dataset/DESTRUCCI-N-DE-INFRAESTRUCTURA-DE-PRODUCCI-N-DE-DR/s29y-2xjd/about_data)

2. Abre **MongoDB Compass** y navega a la base de datos `destruccion_infraestructura` y la colección `datos`.

3. Haz clic en el botón **"Import Data"** y selecciona el archivo **`DESTRUCCI_N_DE_INFRAESTRUCTURA_DE_PRODUCCI_N_DE_DROGAS_IL_CITAS_20241108.csv`**.

4. Asegúrate de que el **formato sea CSV** y haz clic en **"Import"** para cargar los datos.

---

## Graficación de Datos con Python

Ahora que los datos están en MongoDB, utilizaremos Python para realizar una visualización.

### Explicación del Código
1. **Conexión:** a la base de datos `destruccion_infraestructura` y obtención de los datos de la colección `datos`.
2. Conversión de los datos en un **DataFrame de pandas**.
3. Transformación de la columna `'FECHA HECHO'` a un **formato de fecha**.
4. Agrupación y suma de la columna `CANTIDAD` por fecha.
5. Creación de un **gráfico de líneas** para visualizar los datos.

---

## Referencias

- Datos obtenidos de: [datos.gov.co](https://www.datos.gov.co/)
- [Documentación de MongoDB](https://docs.mongodb.com/)
- [Documentación de Matplotlib](https://matplotlib.org/stable/contents.html)
- [Documentación de Pandas](https://pandas.pydata.org/)

---

¡Ahora puedes usar esta documentación para tu repositorio de GitHub! Asegúrate de agregar el código en un archivo `README.md` para que sea accesible directamente en la página principal de tu repositorio.
