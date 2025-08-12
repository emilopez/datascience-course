import marimo

__generated_with = "0.14.16"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Matrices y pandas

    - Fecha: 20-10-2022
    - Unidad 2: ecosistema científico básico
    - Temas:
        - Numpy.
        - Pandas.

    - Referencias:
        - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html
        - https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html



    ## Matrices: numpy ndarray
    """
    )
    return


@app.cell
def _():
    import numpy as np
    import plotly.graph_objects as go


    from PIL import Image
    #from matplotlib import pyplot as plt
    return Image, go, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Cargamos una imagen

    - Veamos su estructura
    """
    )
    return


@app.cell
def _(Image, np):
    # leemos la imagen
    i = Image.open('datos/pics/lapacho2.jpg')

    # la convertimos a un array numpy
    im = np.array(i)

    # vemos info del archivo
    print(type(im))   # tipo de contenedor
    print(im.dtype)   # tipo de dato dentro del contenedor
    print(im.ndim)    # dimensiones
    print(im.shape)   # elementos en cada dimension
    return (im,)


@app.cell
def _(im):
    im_1 = im[0:400, 0:300, :]
    return (im_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Visualizamos la imagen
    - Ahora con plotly
    """
    )
    return


@app.cell
def _(go, im_1):
    fig = go.Figure()
    fig.add_trace(go.Image(z=im_1))
    fig.update_layout(autosize=False, height=600)
    fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Visualizamos el valor de los pixeles

    Analicemos como se muestra en valor de los pixeles de una submatriz usando slices
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Veamos el valor de un pixel específico**
    - elegir un pixel interactivamente y corroborar sus valores mediante el código
    """
    )
    return


@app.cell
def _(im_1):
    colu = 239
    fila = 98
    banda_rojo = float(im_1[fila, colu, 0])
    banda_verde = float(im_1[fila, colu, 1])
    banda_azul = float(im_1[fila, colu, 2])
    print(type(banda_azul))
    print('rojo: ', banda_rojo)
    print('verde: ', banda_verde)
    print('azul: ', banda_azul)
    promedio = (banda_azul + banda_rojo + banda_verde) / 3
    print(promedio)
    return colu, fila


@app.cell
def _(colu, fila, im_1):
    im_1[fila, colu, :].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Ejercitación 8.1: creando el lapacho rojo

    - Recorrer la imagen usando dos ciclos for anidados y cambiar el color de las flores amarillas por rojas. Ayuda: utilice el promedio
    """
    )
    return


@app.cell
def _(go, im_1):
    filas, columnas, bandas = im_1.shape
    for f in range(filas):
        for c in range(columnas):
            prom = im_1[f, c, :].mean()
            if 90 <= prom <= 150:
                im_1[f, c, 0] = 255
                im_1[f, c, 1] = 0
                im_1[f, c, 2] = 0
    fig_1 = go.Figure()
    fig_1.add_trace(go.Image(z=im_1))
    fig_1.update_layout(autosize=False, height=600)
    fig_1.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Intro a Pandas

    - Documentación oficial:
        - https://pandas.pydata.org/
        - https://pandas.pydata.org/pandas-docs/stable/
    - Veremos:
        - conceptos generales: 
            - dataframe
            - series/columnas

    ### Importar pandas
    """
    )
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Dataframes a partir de un diccionario

    - Creamos un dataframe a partir del diccionario previo
    """
    )
    return


@app.cell
def _():
    mi_rio = {"dia":    [1, 2, 3, 4, 5, 6, 7], 
              "altura": [7, 7.1, 7.2, 7.1, 7.0, 6.9, 7]}
    return (mi_rio,)


@app.cell
def _(mi_rio):
    mi_rio
    return


@app.cell
def _(mi_rio, pd):
    rio_dataf = pd.DataFrame(mi_rio)
    rio_dataf
    return (rio_dataf,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""- Vemos su contenido usando los métodos .head() y .tail()""")
    return


@app.cell
def _(rio_dataf):
    rio_dataf.head(3)
    return


@app.cell
def _(rio_dataf):
    rio_dataf.tail(3)
    return


@app.cell
def _(rio_dataf):
    rio_dataf.info()
    return


@app.cell
def _(rio_dataf):
    rio_dataf.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Otro ejemplo con un diccionario: con numpy ndarray**""")
    return


@app.cell
def _(np, pd):
    t = np.linspace(-1, 1, 1000)
    sin_t = np.sin(2*np.pi*t)
    cos_t = np.cos(2*np.pi*t)
    data_trigo = pd.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})
    data_trigo.head()
    return (data_trigo,)


@app.cell
def _(data_trigo, go):
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=data_trigo["t"], y=data_trigo["sin"], name="sin"))
    fig3.add_trace(go.Scatter(x=data_trigo["t"], y=data_trigo["cos"], name="cos"))

    fig3.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Ejercitación 8.2
    - Grafique por separado los dataframes previos usando plotly
    """
    )
    return


@app.cell
def _(go, rio_dataf):
    fig4 = go.Figure()

    fig4.add_trace(go.Scattergl(x=rio_dataf["dia"], y=rio_dataf["altura"]))
    fig4.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Lectura desde un archivo""")
    return


@app.cell
def _(pd):
    datos_eph2019 = pd.read_csv("datos/eph_pobreza2019.csv", sep=";")
    return (datos_eph2019,)


@app.cell
def _(datos_eph2019):
    datos_eph2019.tail()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""- Analizamos su tipo y contenido: **help**, parámetros importantes: sep, decimal, skiprows, names...""")
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019.info()
    return


@app.cell
def _():
    #pd.read_csv?
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019.tail()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""- **Métodos útiles:** .head(), .tail(), info(). describe() .rename()""")
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019["PromePobreza"] = (datos_eph2019["PobrezaHogares"] + datos_eph2019["PobrezaPersonas"])/2
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019.head()
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Ejercitación 8.3

    - Grafique el dataframe previamente cargado desde el archivo usando el método .plot
    - Intente replicar el gráfico con plotly
    """
    )
    return


app._unparsable_cell(
    r"""
    datos_eph2019.plot?
    """,
    name="_"
)


@app.cell
def _():
    # series apiladas
    #datos_eph2019.plot()
    #plt.xlabel("Subregiones")
    #plt.ylabel("Porcentaje [%]")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Selección de datos y filtrado

    **Por columnas**

    Tenemos dos formas de seleccionar columnas:

    - **Como un diccionario:** ``data["NombreColumna"]`` <- sugerida pq es mejor!
    - Como un método: ``data.NombreColumna``

    Atención: revisar antes los nombres de las columnas por si tenemos espacios antes o después: ``data2.columns``
    """
    )
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019.columns
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019["Regiones"].head()
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019.Regiones.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""- **Podemos seleccionar columnas usando un índice numérico** ``.iloc[:,3]`` separando por comas las filas de las columnas.""")
    return


@app.cell
def _(datos_eph2019):
    # una única columna
    datos_eph2019.iloc[:,3]
    return


@app.cell
def _(datos_eph2019):
    # o varias columnas
    datos_eph2019.iloc[:,[0,3,1]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Por filas**

    - Usando slices: ``data[1:5]``
    """
    )
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019[5:10]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""- Selección de una única fila determinada""")
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019.iloc[2] # en versiones viejas se llamaba .ix[]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Crear nuevas columnas

    - Es posible agregar nuevas columnas al dataframe usando una práctica similar a los diccionarios:
    """
    )
    return


@app.cell
def _(datos_eph2019):
    datos_eph2019["PobrezaPromedio"] = (datos_eph2019["PobrezaHogares"] + datos_eph2019["PobrezaPersonas"])/2
    return


@app.cell
def _(data2):
    data2.head()
    return


@app.cell
def _(datos_eph2019):
    # boolean masking / boolean indexing
    indices1 = datos_eph2019["Regiones"] == "Cuyo"
    return (indices1,)


@app.cell
def _(datos_eph2019, indices1):
    datos_eph2019[indices1].mean()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
