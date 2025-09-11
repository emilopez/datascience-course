import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium", layout_file="layouts/charla_ds.slides.json")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Python sin fronteras

    - Emiliano López | emiliano.lopez@gmail.com | 9 sept 2025 | FICH UNL
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # ¿Qué es la ciencia de datos?

    Es la disciplina que utiliza métodos estadísticos, matemáticos, programación e inteligencia artificial para **analizar datos** y obtener *conocimiento* que apoye la toma de decisiones.

    - Objetivo: obtener *conocimiento* a partir de los datos ➡️ que guíen la toma de decisiones.
    - Combina matemáticas, estadística, programación, analítica avanzada, IA y machine learning.  
    - Requiere conocimiento del dominio específico.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Decisiones basadas en datos
    <center><img src="public/information_data_based.png" width="500" /></center>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Importancia actual
    - Crecimiento acelerado por el aumento del volumen y diversidad de datos.  
    - Una de las disciplinas de mayor expansión en todas las industrias.  
    - Las organizaciones requieren cada vez más de DS para mejorar resultados de negocio.
    - **En el ámbito científico es tarea de todos los días:**
        - Estudio de fenómenos ambientales
        - Datos provenientes de fuentes heterogéneas
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # En resumen

    El proceso de extraer conocimiento de los datos

    📊 DATOS → 🔧 PROCESAMIENTO → 📈 ANÁLISIS → 🎯 CONOCIMIENTO/ENTENDIMIENTO → 💡 DECISIONES



    **Componentes clave:**

    - **Recolección:** CSV, APIs, sensores, satélites
    - **Limpieza:** Manejo de valores faltantes, outliers
    - **Exploración:** Visualización, estadísticas descriptivas

    ETL = Extracción, Transformación y Carga

    ---
    - **Modelado:** Machine Learning, predicciones
    - **Comunicación:** Dashboards, reportes, mapas interactivos
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Machine learning

    - Clasificación
    - Regresión

    <center><img src="public/mlearning.png" width="700" /></center>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Python como herramienta

    - 🐍 Python ➕ ⚗️ ecosistema científico 🧪

    <center><img src="public/python_tiobe.png" width="700" /></center>

    ## Por dónde empezar? 
    - Distribución de Python que facilita instalación y gestión de librerías y entornos virtuales
    - Anaconda: https://www.anaconda.com/download/success
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Ecosistema científico de python

    <center><img src="public/scientific_ecosystem.png" width=700></center>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Ejemplos
    - Ej 1: 🖥️ Intro a Jupyter Lab / Marimo
    - Ej 2: ⛰️ Modelo digital de elevación (DEM) Mendoza
    - Ej 3: 🌎 Ciudades / Mapas
    - Ej 4: 🌱 Cultivos / LiDAR
        - [Crecimiento y rendimiento de alfalfa - Sensores ultrasónicos](https://py.cafe/app/emilopez/pyalfalfadynamics)
        - Escaner 3D LiDAR (jupyter)
    - Ej 5: 🦟 [Monitor Aedes aegypti - Santo Tomé](https://monitor-f6f2ac.gitlab.io/)
    - Ej 6: 🌊 Monitor Reserva Natural Urbana del Oeste - Santa Fe (https://monitorreservasfe.streamlit.app/)
        - Dashboard de esta charla
    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
