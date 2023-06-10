import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def matrizFacultades(archivo: str) -> pd.DataFrame:
    archivo = pd.read_csv(archivo, sep=',')
    return archivo


def matrizPuestos(archivo: str) -> pd.DataFrame:
    archivo = pd.read_csv(archivo, sep=',')
    return archivo


def matrizDobles(archivo: str) -> pd.DataFrame:
    archivo = pd.read_csv(archivo, sep=',')
    return archivo


def puestosFacultad(puestos: pd.DataFrame, facultad: str) -> int:
    fila_facultad = puestos.loc[puestos.iloc[0:11, 0] == facultad]
    lista_puestos = fila_facultad.values[:]
    suma_puestos = 0
    for lista in lista_puestos:
        for valor in range(1, len(lista)):
            suma_puestos += lista[valor]
    return suma_puestos


def puestosOcupados(puestos: pd.DataFrame, facultad: str) -> int:
    sumaOcupados = 0
    for faculty in puestos:
        if faculty == facultad:
            sumaOcupados = puestos[faculty].sum()
    return sumaOcupados


def facultadGenerosa(puestos: pd.DataFrame, facultad: str, porcentaje: int) -> tuple:
    ocupadosFacultad = puestosOcupados(puestos, facultad)
    porcentajeOcupados = (ocupadosFacultad*porcentaje)/100
    for columna in puestos.columns:
        if columna == facultad:
            valores = puestos[columna]
            for valor in valores:
                if valor > porcentajeOcupados:
                    print(valor)


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
