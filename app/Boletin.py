import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def matrizFacultades(archivo: str):
    archivo = pd.read_csv(archivo, sep=',')
    return archivo


def matrizPuestos(archivo: str):
    archivo = pd.read_csv(archivo, sep=',')
    return archivo


def matrizDobles(archivo: str):
    archivo = pd.read_csv(archivo, sep=',')
    return archivo


def cargar_matriz_estadisticas(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de estadisticas 
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """
    archivo = open(ruta_archivo)
    linea = archivo.readline()
    facultades = 11
    elementos = 9
    estadisticas = []
    for i in range(0, facultades+1):
        estadisticas.append([0]*(elementos+1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, elementos+1):
            estadisticas[i][j] = datos[j].strip()
        i += 1
        linea = archivo.readline()
    archivo.close()

    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo1 = open(ruta_archivo)
    linea = archivo1.readline()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0, oferentes+1):
        puestos.append([0] * (ocupantes+1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, ocupantes+1):
            puestos[i][j] = datos[j].strip()
        i += 1
        linea = archivo1.readline()
    archivo1.close()

    return puestos


def ejecutar_cargar_matriz_dobles(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """

    archivo2 = open(ruta_archivo)
    linea = archivo2.readline()
    programas = []

    while len(linea) > 0:
        datos = linea.split(",")
        programas.append(datos)
        linea = archivo2.readline()
    archivo2.close()

    return programas


def puestosFacultad(puestos, facultad):
    fila_facultad = puestos.loc[puestos.iloc[:, 0] == facultad]
    lista_puestos = fila_facultad.values[:]
    suma_puestos = 0
    for lista in lista_puestos:
        for valor in range(1, len(lista)):
            suma_puestos += lista[valor]
    return suma_puestos


def puestosOcupados(puestos, facultad):
    sumaOcupados = 0
    for faculty in puestos:
        if faculty == facultad:
            sumaOcupados = puestos[faculty].sum()
    return sumaOcupados


"""
def facultadServicial(puestos):
    facultadName = ""
    servicePorcentaje = 0.0
    copy = puestos.copy()
    puestosAtiende = 0
    puestosEstudiantes = 0
    # Eliminar la diagonal
    df = copy.mask(np.triu(np.ones(copy.shape, dtype=bool),k=1))
    df = df.dropna()
    for faculty in puestos:
        puestosAtiende = puestosFacultad(puestos, faculty)
        for faculty in df:
            puestosEstudiantes = puestosOcupados(df, faculty)
            division = int(puestosAtiende)/int(puestosEstudiantes)
            if division > servicePorcentaje:
                servicePorcentaje = division
                facultadName = faculty
    return (facultadName, servicePorcentaje)
"""


def promedioPGA(estadisticas: pd.DataFrame) -> None:
    estadisticas.sort_values(by="PGA promedio", ascending=True, inplace=True)
    ploter = estadisticas.iloc[0:11, 6]
    listaFacultades = list(estadisticas.iloc[0:11, 0])
    plt.bar(listaFacultades, ploter)
    plt.xticks(rotation=90)
    plt.title("PGA promedio por facultad")
    plt.xlabel("Facultades")
    plt.ylabel("PGA promedio")
    plt.show()


def puestosUsados(estadisticas: pd.DataFrame) -> None:
    estadisticas.sort_values(by="Estudios Dirigidos",
                             ascending=True, inplace=True)
    ploter = estadisticas.iloc[0:11, 12]
    listaFacultades = list(estadisticas.iloc[0:11, 0])
    plt.pie(ploter, labels=listaFacultades, startangle=360)
    plt.title("Puestos usados por Estudios Dirigidos")
    plt.show()


# print(matrizFacultades('data/estadisticas_facultades.csv'))
# print(matrizPuestos('data/matriz_puestos.csv'))
# print(matrizDobles('data/matriz_dobles.csv'))
# print(cargar_matriz_estadisticas('data/estadisticas_facultades.csv'))
# print(cargar_matriz_puestos('data/matriz_puestos.csv'))
# print(ejecutar_cargar_matriz_dobles("data/matriz_dobles.csv"))
# print(puestosFacultad(matrizPuestos('data/matriz_puestos.csv'), 'Economia'))
# print(puestosOcupados(matrizPuestos('data/matriz_puestos.csv'), 'Educacion'))
# print(facultadServicial(matrizPuestos('data/matriz_puestos.csv')))
# print(promedioPGA(matrizFacultades('data/estadisticas_facultades.csv')))
# print(puestosUsados(matrizFacultades('data/matriz_puestos.csv')))
