import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Ejemplo 2: DEM
    - Datos descargados: https://www.ign.gob.ar/NuestrasActividades/Geodesia/ModeloDigitalElevaciones/Busqueda
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    import rasterio
    import numpy as np

    import plotly.graph_objects as go
    return go, mo, np, rasterio


@app.cell
def _(np, rasterio):

    # descarga DEM de https://www.ign.gob.ar/NuestrasActividades/Geodesia/ModeloDigitalElevaciones/Busqueda
    with rasterio.open("charla/data/3369-13.img") as src:
        dem = src.read(1)
        dem[dem == src.nodata] = np.nan
        bounds = src.bounds
        print("CRS (Sistema de coordenadas):", src.crs)
        print("Resolución:", src.res)
        print("Bounds (xmin, ymin, xmax, ymax):", bounds)
        print("Transform:", src.transform)
    return (dem,)


@app.cell
def _(dem, go, np):
    # Reduce resolución para acelerar la visualización
    factor = 4
    dem_sub = dem[::factor, ::factor]

    ny, nx = dem_sub.shape
    X = np.linspace(0, nx - 1, nx)
    Y = np.linspace(0, ny - 1, ny)
    X, Y = np.meshgrid(X, Y)

    fig = go.Figure(data=[go.Surface(z=dem_sub, x=X, y=Y, colorscale='viridis')])
    fig.update_layout(
        title="MDE-Ar (Plotly 3D Surface)",
        autosize=True,
        scene=dict(zaxis_title='Elevación (m)'),
        margin=dict(l=0, r=0, b=0, t=30)
    )
    fig.show()
    return


@app.cell
def _():
    import leafmap

    m = leafmap.Map(center=[-31.5, -60.7], zoom=7)  # ejemplo: Santa Fe, Argentina
    m.add_raster("charla/data/3369-13.img", cmap="terrain", opacity=0.7)
    m
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
