import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def gpd():
    from pathlib import Path
    import geopandas as gpd
    import marimo as mo
    import pandas as pd
    return Path, gpd, mo


@app.cell
def _(mo):
    # Contenido para la celda del Widget
    mo.md("""
    # 🔍 Filtro de Puntos de Interés (POIs) 🗺️

    Seleccioná el tipo de POI que querés visualizar:
    """)
    return


@app.cell
def selector_capa(Path, gpd, mo):
    # Variables de configuración y rutas (asume que los archivos .shp están cerca)

    # directorio base shapefiles arg osm
    dir_osm =  Path.cwd().parent / "datos" / "argentina_osm" / "argentina-251101-free"

    # archivos que vamos a procesar
    POIS_PATH = dir_osm / "gis_osm_pois_free_1.shp"

    # Cargar los datos
    pois = gpd.read_file(POIS_PATH)

    # armamos una lista de los tipos unicos de fclass
    tipos = sorted(pois["fclass"].unique().tolist())

    opciones_pois = {
            t.replace('_', ' ').title(): t
            for t in tipos
    }

    # 🔑 CORRECCIÓN: El valor inicial debe ser la CLAVE (label), no el valor
    # Buscar la clave que corresponde a "restaurant"
    valor_inicial = "Restaurant"  # La versión "title case" de "restaurant"

    # Si no existe, usar la primera opción disponible
    if valor_inicial not in opciones_pois:
        valor_inicial = list(opciones_pois.keys())[0]

    selector_poi = mo.ui.dropdown(
        options=opciones_pois,
        value=valor_inicial,  # "Restaurant" (la clave)
        label="Tipo de POI:"
    )

    # Selector de tipo de mapa
    opciones_mapas = {
        "OpenStreetMap (Estándar)": "OpenStreetMap",
        "CartoDB Positron (Claro)": "CartoDB positron",
        "CartoDB Dark Matter (Oscuro)": "CartoDB dark_matter", # conda install -c conda-forge xyzservices
        "OpenTopoMap (Topográfico)": "OpenTopoMap",
        "Esri WorldImagery (Satélite)": "Esri WorldImagery",
        "Esri WorldStreetMap": "Esri WorldStreetMap",
    }

    selector_mapa = mo.ui.dropdown(
        options=opciones_mapas,
        value="CartoDB Positron (Claro)",
        label="Estilo de mapa:"
    )

    # Mostrar ambos selectores uno al lado del otro
    mo.hstack([selector_poi, selector_mapa], gap=1)


    #selector_poi
    return pois, selector_mapa, selector_poi


@app.cell
def mapa_reactivo(mo, pois, selector_mapa, selector_poi):
    filtro_valor = selector_poi.value
    tile_seleccionado = selector_mapa.value

    mo.md(f"""
    ### Mostrando: {filtro_valor.replace('_', ' ').title()}
    **Mapa:** {tile_seleccionado}
    """)

    # Filtrar POIs
    pois_filtrados = pois[pois['fclass'] == filtro_valor]

    # Crear el mapa con el tile seleccionado
    mapa_final = pois_filtrados.explore(
        color='blue',
        marker_kwds={'radius': 5},
        tooltip=['name', 'fclass'],
        tiles=tile_seleccionado,  # Usar el tile del selector
        name=f"Puntos: {filtro_valor}"
    )

    mapa_final

    return


@app.cell
def _():
    import xyzservices.providers as xyz
    print(xyz.keys())
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
