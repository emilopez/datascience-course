import marimo

__generated_with = "0.15.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/datascience_presentation.slides.json",
)


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from datetime import datetime, timedelta
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # Configuración de estilo
    plt.style.use('default')
    np.random.seed(42)
    return go, make_subplots, mo, np, pd, px


@app.cell
def _(mo):
    # SLIDE 1: TÍTULO Y PRESENTACIÓN
    slide_1 = mo.md("""
    # 🐍 Data Science con Python
    ## Una ventana al mundo de los datos para ingenieros

    ### Aplicaciones en:
    - 🌊 **Ingeniería Hídrica**: Análisis de caudales, calidad del agua
    - 🌱 **Ingeniería Ambiental**: Monitoreo atmosférico, contaminación
    - 💻 **Ingeniería Informática**: Análisis de sistemas, optimización
    - 🤖 **Inteligencia Artificial**: Machine Learning, Deep Learning

    ---
    *Presentación interactiva con marimo*
    """)
    return (slide_1,)


@app.cell
def _(mo):
    # SLIDE 2: ¿QUÉ ES DATA SCIENCE?
    slide_2 = mo.md("""
    # 🔍 ¿Qué es Data Science?

    ## El proceso de extraer conocimiento de los datos

    ```
    📊 DATOS → 🔧 PROCESAMIENTO → 📈 ANÁLISIS → 🎯 INSIGHTS → 💡 DECISIONES
    ```

    ### Componentes clave:
    - **Recolección**: CSV, APIs, sensores, satélites
    - **Limpieza**: Manejo de valores faltantes, outliers
    - **Exploración**: Visualización, estadísticas descriptivas
    - **Modelado**: Machine Learning, predicciones
    - **Comunicación**: Dashboards, reportes, mapas interactivos

    ### ¿Por qué Python? 🐍
    - Sintaxis simple y legible
    - Amplio ecosistema de librerías
    - Comunidad activa
    - Integración con herramientas de visualización
    """)
    return (slide_2,)


@app.cell
def _(np, pd):
    # Generar datos simulados para la presentación
    fechas = pd.date_range('2023-01-01', periods=365, freq='D')
    caudal_data = pd.DataFrame({
        'fecha': fechas,
        'caudal_m3s': 50 + 30 * np.sin(2 * np.pi * np.arange(365) / 365) + np.random.normal(0, 5, 365),
        'precipitacion_mm': np.random.exponential(2, 365),
        'temperatura_c': 15 + 10 * np.sin(2 * np.pi * np.arange(365) / 365) + np.random.normal(0, 2, 365)
    })

    # Coordenadas aproximadas de Santa Fe
    lat_centro = -31.6333
    lon_centro = -60.7000

    # Datos ambientales simulados
    estaciones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    contaminantes_data = pd.DataFrame({
        'estacion': np.random.choice(estaciones, 100),
        'pm25': np.random.lognormal(2, 0.5, 100),
        'pm10': np.random.lognormal(2.5, 0.4, 100),
        'no2': np.random.gamma(2, 20, 100),
        'lat': lat_centro + np.random.uniform(-0.02, 0.02, 100),
        'lon': lon_centro + np.random.uniform(-0.02, 0.02, 100)
    })
    return caudal_data, contaminantes_data, fechas


@app.cell
def _(caudal_data, go, make_subplots, mo):
    # SLIDE 3: TIPOS DE DATOS - TEMPORALES
    slide_3_code = mo.md("""
    # 📊 Tipos de Datos en Ingeniería

    ## 1. Datos Temporales (Series de Tiempo)
    **Ejemplo: Monitoreo hidrológico**
    """)

    # Gráfico de series de tiempo
    fig_temporal = make_subplots(
        rows=3, cols=1, 
        subplot_titles=('Caudal (m³/s)', 'Precipitación (mm)', 'Temperatura (°C)'),
        vertical_spacing=0.08
    )

    fig_temporal.add_trace(
        go.Scatter(x=caudal_data['fecha'], y=caudal_data['caudal_m3s'], 
                  name='Caudal', line=dict(color='blue')),
        row=1, col=1
    )

    fig_temporal.add_trace(
        go.Bar(x=caudal_data['fecha'], y=caudal_data['precipitacion_mm'], 
               name='Precipitación', marker_color='blue'),
        row=2, col=1
    )

    fig_temporal.add_trace(
        go.Scatter(x=caudal_data['fecha'], y=caudal_data['temperatura_c'], 
                  name='Temperatura', line=dict(color='red')),
        row=3, col=1
    )

    fig_temporal.update_layout(height=600, showlegend=False, 
                              title_text="Datos Hidrológicos - Serie Temporal")

    plot_temporal = mo.ui.plotly(fig_temporal)
    return plot_temporal, slide_3_code


@app.cell
def _(contaminantes_data, mo, px):
    # SLIDE 3: TIPOS DE DATOS - ESPACIALES
    slide_3_spatial = mo.md("""
    ## 2. Datos Espaciales (Georreferenciados)
    **Ejemplo: Red de monitoreo de calidad del aire**
    """)

    # Mapa de contaminación
    fig_spatial = px.scatter_map(
        contaminantes_data, 
        lat="lat", 
        lon="lon", 
        color="pm25",
        size="pm10",
        hover_data=['estacion', 'no2'],
        color_continuous_scale="Viridis",
        title="Concentración de PM2.5 en la ciudad",
        #mapbox_style="open-street-map",
        zoom=11,
        height=500
    )
    fig_spatial.update_layout(mapbox_style="open-street-map")

    plot_spatial = mo.ui.plotly(fig_spatial)
    return plot_spatial, slide_3_spatial


@app.cell
def _(mo):
    # SLIDE 4: ECOSISTEMA DE LIBRERÍAS
    slide_4 = mo.md("""
    # 🛠️ Ecosistema Python para Data Science

    ## Manipulación y Análisis de Datos
    - **pandas** 🐼: DataFrames, CSV, Excel, bases de datos
    - **polars** 🐻‍❄: Dataframes ️¿El reemplazo de Pandas?
    - **numpy** 🔢: Operaciones numéricas, arrays multidimensionales
    - **scipy** 🧮: Estadística, optimización, procesamiento de señalesrs 

    ## Visualización
    - **matplotlib** 📊: Gráficos básicos, control total
    - **seaborn** 🎨: Visualizaciones estadísticas elegantes
    - **plotly** ⚡: Gráficos interactivos, dashboards
    - **leafmap** 🗺️: Mapas interactivos, datos geoespaciales

    ## Entornos y Desarrollo Interactivo
    - **jupyter lab** 📓: Notebooks interactivos para ciencia de datos
    - **marimo** 🪄: Notebooks modernos y reactivos (esta presentación)
    - **streamlit** 🌐: Creación rápida de apps web de ciencia de datos 
        - [Monitor Reserva Natural del Oeste (Santa Fe)](https://monitorreservasfe.streamlit.app/)

    ## Machine Learning
    - **scikit-learn** 🤖: Algoritmos clásicos de ML
    - **tensorflow/pytorch** 🧠: Deep Learning
    - **xgboost** 🚀: Gradient boosting

    ## Datos Geoespaciales
    - **geopandas** 🌍: Análisis geoespacial
    - **rasterio** 🛰️: Procesamiento de imágenes satelitales
    - **folium/leafmap** 🗺️: Mapas web interactivos
    """)
    return (slide_4,)


@app.cell
def _(caudal_data, mo, px):
    # SLIDE 5: CASO PRÁCTICO
    slide_5_intro = mo.md("""
    # 🌊 Caso Práctico: Análisis de Cuenca Hídrica

    ## Problema a resolver:
    Analizar el comportamiento hidrológico de una cuenca para:
    - Identificar patrones estacionales
    - Detectar eventos extremos
    - Correlacionar precipitación con caudal
    - Generar alertas tempranas
    """)

    # Análisis estadístico de los datos
    stats_hidro = caudal_data.describe()

    # Correlaciones
    correlation_matrix = caudal_data[['caudal_m3s', 'precipitacion_mm', 'temperatura_c']].corr()

    # Gráfico de correlación
    fig_corr = px.imshow(correlation_matrix, 
                        text_auto=True, 
                        aspect="auto",
                        title="Matriz de Correlación - Variables Hidrológicas",
                        color_continuous_scale="RdBu")

    plot_correlation = mo.ui.plotly(fig_corr)

    # Detección de eventos extremos
    percentil_95 = caudal_data['caudal_m3s'].quantile(0.95)
    eventos_extremos = caudal_data[caudal_data['caudal_m3s'] > percentil_95]

    slide_5_results = mo.md(f"""
    ## Resultados del Análisis:

    ### 📈 Estadísticas Descriptivas
    - **Caudal promedio**: {caudal_data['caudal_m3s'].mean():.2f} m³/s
    - **Caudal máximo**: {caudal_data['caudal_m3s'].max():.2f} m³/s
    - **Precipitación anual**: {caudal_data['precipitacion_mm'].sum():.0f} mm

    ### ⚠️ Eventos Extremos Detectados
    - **Número de eventos**: {len(eventos_extremos)} días
    - **Umbral**: > {percentil_95:.2f} m³/s (percentil 95)
    - **Evento más intenso**: {eventos_extremos['caudal_m3s'].max():.2f} m³/s

    ### 🔗 Correlaciones Principales
    - Caudal vs Precipitación: {correlation_matrix.loc['caudal_m3s', 'precipitacion_mm']:.3f}
    - Caudal vs Temperatura: {correlation_matrix.loc['caudal_m3s', 'temperatura_c']:.3f}
    """)
    return plot_correlation, slide_5_intro, slide_5_results


@app.cell
def _(mo):
    # SLIDE 6: LEAFMAP
    slide_6_leafmap = mo.md("""
    # 🗺️ Leafmap: Visualización Geoespacial Interactiva

    ## ¿Qué es Leafmap?
    - Librería Python para crear mapas web interactivos
    - Basada en ipyleaflet y folium
    - Especializada en datos geoespaciales
    - Ideal para análisis ambientales e hídricos

    ## Capacidades principales:
    - **Visualización de rasters**: Imágenes satelitales, DEM, datos climáticos
    - **Datos vectoriales**: Shapefiles, GeoJSON, cuencas, límites
    - **Análisis temporal**: Animaciones, comparaciones antes/después
    - **Interactividad**: Zoom, pan, capas superpuestas
    - **Exportación**: PNG, HTML, PDF

    ## Casos de uso en ingeniería:
    - Monitoreo de cambios en el uso del suelo
    - Análisis de inundaciones
    - Seguimiento de deforestación
    - Planificación urbana
    - Evaluación de impacto ambiental
    """)

    leafmap_code = mo.md("""
    ## Ejemplo de código con Leafmap:

    ```python
    import leafmap
    import geopandas as gpd

    # Crear mapa base
    m = leafmap.Map(center=[-31.4, -60.5], zoom=10)

    # Agregar capa de elevación
    dem_url = "https://elevation-tiles.s3.amazonaws.com/..."
    m.add_raster(dem_url, colormap="terrain", layer_name="Elevación")

    # Agregar datos de estaciones
    estaciones_gdf = gpd.GeoDataFrame(
        contaminantes_data, 
        geometry=gpd.points_from_xy(contaminantes_data.lon, contaminantes_data.lat)
    )
    m.add_gdf(estaciones_gdf, column="pm25", scheme="quantiles", 
             legend_title="PM2.5 (μg/m³)")

    # Agregar controles
    m.add_layer_control()
    m.add_draw_control()
    m.add_measure_control()

    # Mostrar mapa
    m
    ```
    """)
    return leafmap_code, slide_6_leafmap


@app.cell
def _(mo):
    # SLIDE 7: FLUJO DE TRABAJO
    slide_7 = mo.md("""
    # 🔄 Flujo de Trabajo en Data Science

    ## 1. 📥 Obtención de Datos
    ```python
    # CSV local
    df = pd.read_csv('datos_sensor.csv')

    # API pública
    import requests
    response = requests.get('https://api.datos.gob.ar/...')

    # Base de datos
    import sqlalchemy
    engine = sqlalchemy.create_engine('postgresql://...')
    df = pd.read_sql('SELECT * FROM mediciones', engine)
    ```

    ## 2. 🧹 Limpieza y Preparación
    ```python
    # Eliminar valores faltantes
    df.dropna()
    df.fillna(df.mean())

    # Detectar outliers
    Q1 = df['valor'].quantile(0.25)
    Q3 = df['valor'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df['valor'] < Q1-1.5*IQR) | (df['valor'] > Q3+1.5*IQR)]

    # Transformaciones
    df['log_valor'] = np.log(df['valor'])
    df['fecha'] = pd.to_datetime(df['fecha'])
    ```

    ## 3. 📊 Análisis Exploratorio
    ```python
    # Estadísticas descriptivas
    df.describe()

    # Visualizaciones
    plt.hist(df['valor'])
    sns.boxplot(data=df, x='categoria', y='valor')
    px.scatter(df, x='x', y='y', color='valor')
    ```

    ## 4. 🤖 Modelado (opcional)
    ```python
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    ```

    ## 5. 📋 Comunicación de Resultados
    - Dashboards interactivos
    - Reportes automatizados
    - Mapas web
    - Presentaciones (¡como esta!)
    """)
    return (slide_7,)


@app.cell
def _(mo):
    # SLIDE 8: CASOS DE USO
    slide_8 = mo.md("""
    # 🎯 Casos de Uso por Especialidad

    ## 🌊 Ingeniería Hídrica
    - **Gestión de recursos**: Optimización de embalses
    - **Modelado hidrológico**: Predicción de caudales
    - **Calidad del agua**: Monitoreo de parámetros físico-químicos
    - **Eventos extremos**: Sistemas de alerta temprana
    - **Infraestructura**: Análisis de vulnerabilidad de obras

    ## 🌱 Ingeniería Ambiental
    - **Monitoreo atmosférico**: Redes de calidad del aire
    - **Gestión de residuos**: Optimización de rutas de recolección
    - **Evaluación de impacto**: Modelado de dispersión de contaminantes
    - **Restauración**: Seguimiento de ecosistemas
    - **Cambio climático**: Análisis de tendencias y proyecciones

    ## 💻 Ingeniería Informática
    - **Análisis de performance**: Optimización de sistemas
    - **Seguridad**: Detección de anomalías y intrusiones
    - **IoT**: Procesamiento de datos de sensores
    - **Redes**: Análisis de tráfico y patrones de uso
    - **DevOps**: Métricas y monitoring de aplicaciones

    ## 🤖 Inteligencia Artificial
    - **Computer Vision**: Procesamiento de imágenes satelitales
    - **NLP**: Análisis de documentos técnicos y reportes
    - **Predicción**: Modelos de forecasting para diferentes dominios
    - **Optimización**: Algoritmos genéticos, búsqueda heurística
    - **Automatización**: Pipelines de ML y despliegue de modelos
    """)
    return (slide_8,)


@app.cell
def _(mo):
    # SLIDE 9: RECURSOS
    slide_9 = mo.md("""
    # 🚀 Recursos y Siguientes Pasos

    ## 📚 Recursos para Aprender
    ### Documentación Oficial
    - [Python.org](https://python.org) - Documentación oficial
    - [Pandas](https://pandas.pydata.org) - Análisis de datos
    - [Matplotlib](https://matplotlib.org) - Visualización básica
    - [Leafmap](https://leafmap.org) - Mapas interactivos

    ### Cursos y Tutoriales
    - [Real Python](https://realpython.com) - Tutoriales prácticos
    - [Kaggle Learn](https://kaggle.com/learn) - Cursos gratuitos
    - [DataCamp](https://datacamp.com) - Cursos especializados
    - [Coursera](https://coursera.org) - Especializaciones universitarias

    ## 🛠️ Herramientas de Desarrollo
    - **Jupyter Notebooks**: Prototipado y experimentación
    - **VS Code**: Editor con extensiones para Python
    - **Google Colab**: Notebooks en la nube, GPU gratis
    - **Marimo**: Notebooks reactivos (como esta presentación!)

    ## 🎯 Proyectos para Empezar
    1. **Análisis de datos CSV**: Importar y visualizar datos de tu área
    2. **Dashboard simple**: Crear gráficos interactivos con Plotly
    3. **Mapa básico**: Usar Leafmap para visualizar datos geoespaciales
    4. **Predicción simple**: Modelo de regresión con scikit-learn
    5. **Automatización**: Script para procesar datos periódicamente

    ## 🌟 Consejos Finales
    - **Empezar simple**: No tratar de hacer todo de una vez
    - **Practicar regularmente**: Constancia es clave
    - **Unirse a comunidades**: Stack Overflow, Reddit, Discord
    - **Participar en competencias**: Kaggle, DrivenData
    - **Contribuir a proyectos**: GitHub, open source
    """)
    return (slide_9,)


@app.cell
def _(caudal_data, fechas, mo, px):
    # SLIDE 10: DEMO INTERACTIVA
    slide_10_demo = mo.md("""
    # 🎮 Demo Interactiva

    ## Explora los datos tu mismo:
    Selecciona diferentes parámetros y observa cómo cambian las visualizaciones.
    """)

    # Controles interactivos para la demo
    variable_selector = mo.ui.dropdown(
        options=['caudal_m3s', 'precipitacion_mm', 'temperatura_c'],
        value='caudal_m3s',
        label="Variable a analizar:"
    )

    periodo_selector = mo.ui.date_range(
        start=fechas[0].date(),
        stop=fechas[-1].date(),
        value=[fechas[0].date(), fechas[-1].date()],
        label="Período de análisis:"
    )

    # Función para crear gráfico interactivo basado en selección
    def create_interactive_plot(variable, start_date, end_date):
        # Convertir fechas si es necesario
        if hasattr(start_date, 'date'):
            start_date = start_date.date()
        if hasattr(end_date, 'date'):
            end_date = end_date.date()

        filtered_data = caudal_data[
            (caudal_data['fecha'].dt.date >= start_date) & 
            (caudal_data['fecha'].dt.date <= end_date)
        ]

        fig = px.line(
            filtered_data, 
            x='fecha', 
            y=variable,
            title=f"Evolución de {variable.replace('_', ' ').title()}",
            labels={'fecha': 'Fecha', variable: variable.replace('_', ' ').title()}
        )

        # Agregar estadísticas
        if len(filtered_data) > 0:
            mean_val = filtered_data[variable].mean()
            fig.add_hline(y=mean_val, line_dash="dash", 
                          annotation_text=f"Media: {mean_val:.2f}")

        return fig
    return (
        create_interactive_plot,
        periodo_selector,
        slide_10_demo,
        variable_selector,
    )


@app.cell
def _(mo):
    # SLIDE 11: CIERRE
    slide_11 = mo.md("""
    # 🎯 ¡Gracias por tu Atención!

    ## 💡 Puntos Clave a Recordar
    - Python es una herramienta poderosa para cualquier ingeniero
    - Los datos están en todas partes esperando ser analizados
    - La visualización es clave para comunicar resultados
    - Leafmap y herramientas similares hacen accesible el análisis geoespacial
    - El ecosistema Python es rico y está en constante crecimiento

    ## 🤝 Conectemos
    - **GitHub/Lab**: emilopez
    - **LinkedIn**: emilianolopez
    - **Email**: emiliano.lopez@gmail.com

    ## ❓ ¿Preguntas?

    ---
    *"Los datos son el nuevo petróleo, pero como el petróleo, son inútiles sin refinamiento"* - Clive Humby
    """)
    return (slide_11,)


@app.cell
def _(
    create_interactive_plot,
    fechas,
    leafmap_code,
    mo,
    periodo_selector,
    plot_correlation,
    plot_spatial,
    plot_temporal,
    slide_1,
    slide_10_demo,
    slide_11,
    slide_2,
    slide_3_code,
    slide_3_spatial,
    slide_4,
    slide_5_intro,
    slide_5_results,
    slide_6_leafmap,
    slide_7,
    slide_8,
    slide_9,
    variable_selector,
):
    # LAYOUT PRINCIPAL DE LA PRESENTACIÓN
    presentation_tabs = mo.ui.tabs({
        "🏠 Inicio": slide_1,
        "🔍 Qué es DS": slide_2,
        "📊 Tipos de Datos": mo.vstack([
            slide_3_code, 
            plot_temporal,
            slide_3_spatial,
            plot_spatial
        ]),
        "🛠️ Librerías": slide_4,
        "🌊 Caso Práctico": mo.vstack([
            slide_5_intro,
            plot_correlation,
            slide_5_results
        ]),
        "🗺️ Leafmap": mo.vstack([
            slide_6_leafmap,
            leafmap_code
        ]),
        "🔄 Flujo Trabajo": slide_7,
        "🎯 Casos de Uso": slide_8,
        "🚀 Recursos": slide_9,
        "🎮 Demo": mo.vstack([
            slide_10_demo,
            mo.hstack([variable_selector, periodo_selector]),
            mo.ui.plotly(create_interactive_plot(
                variable_selector.value,
                periodo_selector.value[0] if periodo_selector.value else fechas[0].date(),
                periodo_selector.value[1] if periodo_selector.value else fechas[-1].date()
            ))
        ]),
        "🎯 Cierre": slide_11
    })

    # Mostrar la presentación
    presentation_tabs
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
