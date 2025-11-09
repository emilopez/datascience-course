import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")

with app.setup:
    # 1. Carga: En lugar de pd.read_csv(), usamos gpd.read_file()
    #lugares = gpd.read_file(RUTA_LUGARES)
    #lugares.head(1000)
    pass


@app.cell(hide_code=True)
def intro(mo):
    mo.md("""
    # 🚀 De Pandas a GeoPandas: Análisis de datos Espaciales

    **GeoPandas** es una extensión que añade la capacidad de
    manejar datos geográficos (coordenadas, formas, geometrías) para responder
    preguntas basadas en **ubicación**.

    Usaremos datos de OpenStreetMap (OSM) [de Argentina](https://download.geofabrik.de/south-america/argentina.html).
    """)
    return


@app.cell
def _():
    import pandas as pd
    import marimo as mo
    from pathlib import Path
    import geopandas as gpd

    return Path, gpd, mo


@app.cell
def _():
    CRS_ARG = "EPSG:5346"  # POSGAR 2007 / Argentina 4
    return (CRS_ARG,)


@app.cell
def _(Path):
    # directorio base shapefiles arg osm
    dir_osm =  Path.cwd().parent / "datos/" / "argentina_osm" / "argentina-251101-free"
 
    # archivos que vamos a procesar
    RUTA_LUGARES = dir_osm / "gis_osm_places_a_free_1.shp"
    RUTA_POIS = dir_osm / "gis_osm_pois_free_1.shp"
    RUTA_CAMINOS = dir_osm /  "gis_osm_roads_free_1.shp"
    return RUTA_CAMINOS, RUTA_LUGARES, RUTA_POIS


@app.cell
def _(RUTA_LUGARES):
    RUTA_LUGARES
    return


@app.cell
def _(RUTA_LUGARES, gpd):
    # 1. Carga: En lugar de pd.read_csv(), usamos gpd.read_file()
    lugares = gpd.read_file(RUTA_LUGARES)
    lugares.head(1000)
    return (lugares,)


@app.cell
def _(lugares):
    type(lugares["geometry"])
    return


@app.cell
def _(lugares):
    lugares.explore()
    return


@app.cell(hide_code=True)
def exploracion_pandas(mo):
    mo.md("""
    ## 1. De DataFrame a *Geo*DataFrame
    El GeoDataFrame se ve como un Pandas DataFrame, pero tiene una columna clave: **geometry**.
    """)
    return


@app.cell
def _(lugares):
    lugares.info()
    return


@app.cell
def exploracion_geopandas(lugares):
    # Creamos el mapa interactivo directamente.
    mapa_lugares_interactivo = lugares.explore(
        style_kwds={'fillColor': 'lightgray', 'color': 'black', 'weight': 1, 'fillOpacity': 0.7},
        tooltip=['name', 'fclass'], # Información que aparece al pasar el mouse
        name="Lugares (Polígonos OSM)"
    )

    # Mostrar la figura interactiva (Marimo la renderiza al ser la última expresión)
    mapa_lugares_interactivo
    return


@app.cell(hide_code=True)
def crs_info(CRS_ARG, lugares, mo):
    mo.md(f"""
    ## 2. El Pilar: Sistemas de Coordenadas (CRS)
    **CRS Actual:** `{lugares.crs}`. Este es **EPSG:4326** (WGS 84), que habla en **grados** (lat/lon).
    Es bueno para ubicar, pero no para medir distancias o áreas con precisión.

    Para medir, debemos reproyectar a un CRS en **metros**. Usaremos `{CRS_ARG}`.
    """)
    return


@app.cell
def reproyeccion(CRS_ARG, lugares):
    # Reproyectamos a coordenadas planas
    lugares_proy = lugares.to_crs(CRS_ARG)
    print(f"Nuevo CRS (proyectado): {lugares_proy.crs}")
    return (lugares_proy,)


@app.cell(hide_code=True)
def calculo_area(mo):
    mo.md("""
    ## 3. Nuevas Columnas partiendo de la Geometría

    Podemos crear nuevas columnas usando las propiedades de la geometría (`.area`, `.length`, `.centroid`).
    **¡Solo tiene sentido hacerlo con el GDF proyectado (en metros)!**

    Calcularemos el área en kilómetros cuadrados.
    """)
    return


@app.cell
def _(lugares_proy):
    # Crear una copia para añadir columnas
    lugares_calc = lugares_proy.copy()

    # .area (metros cuadrados) / 1,000,000 = kilómetros cuadrados
    lugares_calc['area_km2'] = lugares_calc.area / 1_000_000

    # Volvemos a Pandas para ordenar por la nueva columna
    return (lugares_calc,)


@app.cell
def _(lugares_calc):
    lugares_calc
    return


@app.cell(hide_code=True)
def calculo_centroid(mo):
    mo.md("""
    ### .centroid

    Podemos calcular el centroide (punto central) de cada polígono.
    """)
    return


@app.cell
def _(lugares_proy):
    lugares_calc_full = lugares_proy.copy()
    centroides = lugares_proy.centroid
    return (centroides,)


@app.cell
def _(centroides, lugares_proy, mo):
    mo.md("### .centroid: Visualización Interactiva")
    mo.md("Calculamos el punto central (centroide) de cada polígono y lo mostramos sobre el mapa.")

    # 1. Calcular el GeoDataFrame de Centroides
    # Nota: La propiedad .centroid devuelve un GeoSeries, lo convertimos a GDF para .explore()
    #centroides = lugares_proy.centroid.to_frame(name='geometry')

    # 2. Crear el mapa base con los polígonos (Lugares)
    mapa_lugares = lugares_proy[500:1100].explore(
        style_kwds={'fillColor': 'lightgray', 'color': 'black', 'weight': 1, 'fillOpacity': 0.3},
        tooltip=['name', 'fclass'],
        name="Lugares (Polígonos)"
    )

    # 3. Añadir la capa de puntos (Centroides) al mapa base
    # Usamos m=mapa_lugares para agregar una segunda capa
    mapa_final = centroides[500:1100].explore(
        m=mapa_lugares,
        color='red',
        marker_kwds={'radius': 5}, # Controla el tamaño del punto
        tooltip=False, # No necesitamos tooltip en el punto, ya lo tenemos en el polígono
        name="Centroides (Puntos)"
    )

    # 4. Mostrar el mapa interactivo
    mapa_final
    return


@app.cell(hide_code=True)
def ejercicio1_enunciado(CRS_ARG, RUTA_CAMINOS, mo):
    mo.md(f"""
    ### ✏️ Ejercicio 1: Longitud de Autopistas

    1. Carga el archivo de caminos (`{RUTA_CAMINOS}`).
    2. Reproyéctalo a `{CRS_ARG}`.
    3. Filtra (con Pandas) para quedarte solo con las autopistas (`fclass == 'motorway'`).
    4. Calcula la longitud total en kilómetros de estas autopistas.
    """)
    return


@app.cell
def ejercicio1_solucion(RUTA_CAMINOS, gpd):
    # lectura
    caminos = gpd.read_file(RUTA_CAMINOS)

    # ver crs
    print(caminos.crs)

    # proyeccion a crs planas
    caminos_proy = caminos.to_crs("EPSG:4326")
    return (caminos_proy,)


@app.cell
def _(caminos_proy):
    caminos_proy.head(1000)
    return


@app.cell
def _(caminos_proy):
    # que tipos de caminos hay?
    caminos_proy['fclass'].unique()
    return


@app.cell
def _(caminos_proy):
    # filtrado 
    idx_autopistas = caminos_proy['fclass'] == 'motorway'
    autopistas = caminos_proy[idx_autopistas].copy()

    # cálculo
    autopistas['longitud_km'] = autopistas.length / 1000
    total_km = autopistas['longitud_km'].sum()
    return autopistas, total_km


@app.cell
def _(autopistas):
    autopistas
    return


@app.cell
def _(autopistas):
    RNA001 = autopistas[autopistas["ref"] == "RNA001"]
    return (RNA001,)


@app.cell
def _(RNA001):
    RNA001["longitud_km"].sum()
    return


@app.cell
def _(total_km):
    print(f"Total de KM de autopista (motorway) en el dataset: {total_km:.2f} km")
    return


@app.cell
def ejercicio(mo):
    mo.md(r"""
    ### Problema: cuántos km de longitud tiene la ruta nacional 40 ?
    """)
    return


@app.cell(hide_code=True)
def spatial_join_intro(mo):
    mo.md("""
    ## 4. Spatial Join (`gpd.sjoin()`)

    Mientras que `pd.merge()` une por una clave (ej: `id`), `gpd.sjoin()` une por **ubicación**.

    **Pregunta:** ¿Cuántos restaurantes (Puntos de Interés) hay en cada ciudad/barrio?
    """)
    return


@app.cell
def carga_pois(RUTA_POIS, gpd):
    # 1. Cargar POIs (puntos de interés)
    pois = gpd.read_file(RUTA_POIS)
    return (pois,)


@app.cell
def _(pois):
    pois
    return


@app.cell
def _(lugares, pois):
    # filtramos usando boolean indexing de pandas
    restaurantes = pois[pois['fclass'] == 'restaurant']

    # Aseguramos el mismo CRS: OJO, siempre operar con el mismo sistema de referencia
    restaurantes = restaurantes.to_crs(lugares.crs)
    return (restaurantes,)


@app.cell
def sjoin(lugares, restaurantes):
    # 2. Spatial Join: https://geopandas.org/en/stable/docs/user_guide/mergingdata.html#

    # predicate='within': ¿Qué puntos están DENTRO de qué polígonos?
    restaurantes_con_lugar = restaurantes.sjoin(lugares, how="inner", predicate='within')

    restaurantes_con_lugar.head()
    return (restaurantes_con_lugar,)


@app.cell
def _():
    # https://geopandas.org/en/stable/docs/reference/api/geopandas.sjoin.html
    # predicados aplicables a lugares
    # lugares.sindex.valid_query_predicates
    return


@app.cell
def _(restaurantes_con_lugar):
    restaurantes_con_lugar
    return


@app.cell
def agrupacion_pandas(mo):
    mo.md("""
    3. ¡Volvemos a Pandas! Agrupamos por el nombre del lugar (`name_right`) y contamos.
    """)
    return


@app.cell
def _(restaurantes_con_lugar):
    conteo_restaurantes = (
        restaurantes_con_lugar.groupby('name_right')
        .size()
        .reset_index(name='conteo_pois')
    )
    conteo_restaurantes = conteo_restaurantes.sort_values(
        'conteo_pois', ascending=False
    )
    conteo_restaurantes
    return (conteo_restaurantes,)


@app.cell(hide_code=True)
def ejercicio2_enunciado(mo):
    mo.md("""
    ### ✏️ Ejercicio 2: Mapa de Calor

    Ya tenemos el conteo. Ahora, vamos a mapear ese conteo:
    1. Usa **`pd.merge()`** (normal) para unir el `conteo_restaurantes` al GDF `lugares`.
    2. Rellena los valores nulos (`NaN`) con `0`.
    3. Plotea el GDF resultante, usando la columna `'conteo_pois'` para el color.
    """)
    return


@app.cell
def ejercicio2_solucion(conteo_restaurantes, lugares):
    # 1. Merge de Pandas
    lugares_con_conteo = lugares.merge(
        conteo_restaurantes, left_on='name', right_on='name_right', how='left'
    )

    # 2. Rellenar NaN
    lugares_con_conteo['conteo_pois'] = lugares_con_conteo['conteo_pois'].fillna(0)

    # 3. Crear el Mapa Interactivo (Coroplético)
    # .explore() detecta automáticamente que es un GDF y usa la columna 'conteo_pois' para el color.
    mapa_coropletico = lugares_con_conteo.explore(
        column='conteo_pois',         # Columna que define el color (el conteo)
        cmap='viridis',               # Mapa de color (igual que Matplotlib)
        tooltip=['name', 'conteo_pois'], # Información que aparece al pasar el mouse
        popup=True,                   # Mostrar la información en un pop-up al hacer click
        legend=True,                  # Mostrar la leyenda de colores
        name="Conteo Restaurantes",
    )

    # Mostrar la figura interactiva
    mapa_coropletico
    return


@app.cell(hide_code=True)
def buffers(mo):
    mo.md("""
    ## 5. Geoprocesamiento: Áreas de Influencia (Buffers)

    Un **Buffer** es un polígono que crea un área de proximidad.
    Calcularemos un buffer de 500 metros alrededor de las autopistas.
    """)
    return


@app.cell
def _(autopistas):
    # Autopistas ya está proyectado (en metros)
    buffers_500m_gdf = autopistas[:1000].buffer(1000).to_frame(name='geometry')

    # Convertimos el GeoSeries de buffers a un GeoDataFrame.
    # Esto es necesario para usar .explore() sobre los buffers.
    buffers_500m_gdf['Area'] = '500m Buffer'

    # 1. Creamos el mapa base con los buffers
    mapa_buffers = buffers_500m_gdf.explore(
        #style_kwds={'fillColor': 'blue', 'color': 'darkblue'},
        tooltip=['Area'], 
        name="Buffers 500m",
        ##tiles='cartodbdarkmatter', # Un estilo de mapa diferente
        # No necesitamos guardar la salida, explore ya devuelve el objeto mapa
    )

    # 3. Mostrar la figura interactiva
    # Marimo detectará el objeto folium/explore y lo renderizará.
    mapa_buffers
    return


@app.cell
def _(autopistas):
    autopistas
    return


@app.cell(hide_code=True)
def widgets_intro(mo):
    mo.md("""
    ## 🎁 Bonus: El Poder Interactivo de Marimo (Widgets)

    Aquí vemos cómo Marimo extiende la reactividad con **widgets**.
    El valor del widget se conecta directamente a cualquier celda que lo use.
    """)
    return


@app.cell
def widget_slider(mo):
    # Creamos el slider y lo mostramos
    slider_buffer = mo.ui.slider(
        100, 2000, step=100, value=500, label="Distancia de Buffer (metros):"
    )
    return (slider_buffer,)


@app.cell
def _(autopistas, gpd, plt, slider_buffer):
    # La celda se re-ejecuta cada vez que slider_buffer.value cambia
    buffers = autopistas.buffer(slider_buffer.value)

    fig_react, ax_react = plt.subplots(figsize=(10, 10))
    gpd.GeoSeries(buffers).plot(ax=ax_react, color='purple', alpha=0.5)
    autopistas.plot(ax=ax_react, color='black', linewidth=0.5)
    ax_react.set_title(f"Buffers de {slider_buffer.value}m")

    minx, miny, maxx, maxy = autopistas.total_bounds
    ax_react.set_xlim(minx, minx + (maxx - minx) * 0.1)
    ax_react.set_ylim(miny, miny + (maxy - miny) * 0.1)
    return


@app.cell
def widget_dropdown(mo, pois):
    # Creamos el dropdown
    tipos_poi_unicos = sorted(pois['fclass'].unique().tolist())
    selector_poi = mo.ui.dropdown(
        options=tipos_poi_unicos,
        value='restaurant',
        label="Selecciona tipo de POI a plotear:"
    )
    return (selector_poi,)


@app.cell(hide_code=True)
def widget_plot_poi(mo, selector_poi):
    mo.md(f"""
    ### Ejemplo 2: Filtrado de POIs (Tipo actual: **{selector_poi.value}**)
    """)
    return


@app.cell
def _(lugares, pois, selector_poi):

    # 1. Filtrar POIs (Pandas)
    pois_filtrados = pois[pois['fclass'] == selector_poi.value]

    # 2. Crear el mapa base con los polígonos (Lugares)
    mapa_lugares2 = lugares[:1000].explore(
        style_kwds={'fillColor': 'lightgray', 'color': 'black', 'weight': 1, 'fillOpacity': 0.5},
        tooltip=['name'],
        name="Lugares (Base)",
        tiles='cartodbpositron' # Estilo más claro para resaltar los puntos
    )

    # 3. Añadir la capa de POIs filtrados (Puntos) al mapa base
    # Usamos m=mapa_lugares para añadir una segunda capa
    mapa_final2 = pois_filtrados[:1000].explore(
        #m=mapa_lugares2,
        color='red',
        marker_kwds={'radius': 5},
        tooltip=['name', 'fclass'],
        name=f"Puntos: {selector_poi.value}"
    )

    # 4. Mostrar el mapa interactivo (la celda se actualiza al cambiar el selector)
    mapa_final2
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
