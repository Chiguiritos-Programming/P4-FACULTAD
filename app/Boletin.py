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


def facultadServicial(puestos):
    facultadName = ""
    servicePorcentaje = 0.0
    copy = puestos.copy()
    puestosAtiende = 0
    puestosEstudiantes = 0
    # Eliminar la diagonal
    df = copy.mask(np.triu(np.ones(copy.shape, dtype=bool), k=1))
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


print(matrizFacultades('data/estadisticas_facultades.csv'))
print(matrizPuestos('data/matriz_puestos.csv'))
print(matrizDobles('data/matriz_dobles.csv'))
print(puestosFacultad(matrizPuestos('data/matriz_puestos.csv'), 'Economia'))
print(puestosOcupados(matrizPuestos('data/matriz_puestos.csv'), 'Educacion'))
print(facultadServicial(matrizPuestos('data/matriz_puestos.csv')))
