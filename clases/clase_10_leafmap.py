import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import leafmap.foliumap as leafmap

    return (leafmap,)


@app.cell
def _(leafmap):
    m = leafmap.Map(center=(40, -100), zoom=4)
    m
    return


@app.cell
def _(leafmap):

    m2 = leafmap.Map()
    in_csv = "https://raw.githubusercontent.com/opengeos/leafmap/master/examples/data/world_cities.csv"
    m2.add_heatmap(
        in_csv,
        latitude="latitude",
        longitude="longitude",
        value="pop_max",
        name="Heat map",
        radius=20,
    )
    return (m2,)


@app.cell
def _(m2):

    m2
    return


@app.cell
def _(m2):
    m2.to_html("heat_map1.html")

    return


@app.cell
def _():
    import geopandas as gpd
    gdf = gpd.read_file(
        "https://github.com/opengeos/leafmap/raw/master/examples/data/cable_geo.geojson"
    )
    return (gdf,)


@app.cell
def _(gdf):
    gdf
    return


@app.cell
def _(gdf, leafmap):
    m3 = leafmap.Map()
    m3.add_basemap("SATELLITE")
    m3.add_gdf(gdf, layer_name="Cable lines")
    m3
    return


@app.cell
def _(leafmap):
    m4 = leafmap.Map()
    cog_url = "https://huggingface.co/datasets/giswqs/geospatial/resolve/main/las_vegas_train_naip.tif"
    m4.add_geotiff(cog_url, name="NAIP", indexes=[1, 2, 3])
    m4.add_layer_control()
    m4.add_opacity_control()
    m4
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
