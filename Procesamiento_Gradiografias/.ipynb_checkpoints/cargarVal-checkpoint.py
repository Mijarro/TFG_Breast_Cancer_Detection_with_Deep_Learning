import os
import shutil


import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import numpy as np
import pydicom
import cv2

from tqdm import tqdm
from skimage.exposure import rescale_intensity
from PIL import Image
from duke_dbt_data import dcmread_image
from typing import AnyStr, BinaryIO, Dict, List, NamedTuple, Optional, Union

pathdf = "D:/TFG/Codigo/InfValidation/merged_dfValidation_serialized.pickle"
pathRadiografias = "D:/TFG/Radiografias Validacion/"
pathNumpys = "D:/TFG/imagenesValCompletas"

def npArrayNormalized(array,tamano_cuadrado):
    array_uint8 = array.astype(np.uint16)
    array_byte0 = (array_uint8 & 0xFF).astype(np.uint8)
    array_byte1 = ((array_uint8 >> 8) & 0xFF).astype(np.uint8)
    array_byte01 = []
    array_byte11 = []
    
    for i in range(array.shape[0]):  # Recorrer la dimensión 0 del array
        # Redimensionar y agregar los bytes a las listas
        array_byte01.append(cv2.resize(array_byte0[i], (tamano_cuadrado, tamano_cuadrado)))
        array_byte11.append(cv2.resize(array_byte1[i], (tamano_cuadrado, tamano_cuadrado)))
    
    # Convertir las listas de bytes a arrays de NumPy
    array_byte01 = np.array(array_byte01)
    array_byte11 = np.array(array_byte11)
    
    arrays = [array_byte01, array_byte11]
    
    arrays = np.transpose(np.array(arrays), (1, 2, 3, 0))
    return arrays
    
def resizeAndSave(npArrayImag, tamano_cuadrado, ruta):
    """
    Redimensiona cada imagen en un np.ndarray y las guarda en un archivo usando np.save.

    Args:
    - npArrayImag (np.ndarray): Un array de NumPy que contiene las imágenes.
    - tamano_cuadrado (int): El tamaño al que se redimensionarán las imágenes (ancho y alto).
    - ruta (str): La ruta donde se guardará el archivo con las imágenes redimensionadas.
    """
    # Crear un nuevo array para almacenar las imágenes redimensionadas
    imagenes_redimensionadas = np.zeros((5, tamano_cuadrado, tamano_cuadrado))

    # Redimensionar cada imagen y guardarla en el nuevo array
    for i in range(5):
        imagen_redimensionada = cv2.resize(npArrayImag[i], (tamano_cuadrado, tamano_cuadrado))
        imgu8 = convert(imagen_redimensionada, 0, 255, np.uint8)
        imagenes_redimensionadas[i] = imgu8

    # Guardar el array de imágenes redimensionadas en un archivo
    np.save(ruta, imagenes_redimensionadas)



# Cargar el DataFrame desde un archivo pickle serializado
merged_df = pd.read_pickle(pathdf)

# Tamaño cuadrado deseado para las imágenes (en píxeles)
tamano_cuadrado = 720

# Iterar sobre las filas del DataFrame merged_df
for index, row in tqdm(merged_df.iterrows(), total=merged_df.shape[0], desc="Cargando imagen"):
    ruta_imagen = os.path.join(pathRadiografias, row["descriptive_path"])
    # Reemplazar "NA" con otro valor
    ruta_imagen = ruta_imagen.replace("000000-", "000000-NA-")
    view = row["View"]
    nombre = f"{view}-{index}.npy"
    if os.path.exists(ruta_imagen):
        if not os.path.exists(os.path.join(f"{pathNumpys}/Normal", nombre)):
            if not os.path.exists(os.path.join(f"{pathNumpys}/Actionable", nombre)):
                if not os.path.exists(os.path.join(f"{pathNumpys}/Benign", nombre)):
                    if not os.path.exists(os.path.join(f"{pathNumpys}/Cancer", nombre)):
                        #print(ruta_imagen)
                        imagen = dcmread_image(fp=ruta_imagen, view=view)
                        arrayImagenes = npArrayNormalized(imagen,tamano_cuadrado)# Resize
                        
                        # Determinar a qué colección agregar la imagen según los valores de las columnas
                        if row["Normal"] == 1:
                            np.save(os.path.join(f"{pathNumpys}/Normal", nombre), arrayImagenes)
                            #print(os.path.join("imagenes/Normal", nombre))
                        if row["Actionable"] == 1:
                            np.save(os.path.join(f"{pathNumpys}/Actionable", nombre), arrayImagenes)
                            #print(os.path.join("imagenes/Actionable", nombre))
                        if row["Benign"] == 1:
                            np.save(os.path.join(f"{pathNumpys}/Benign", nombre), arrayImagenes)
                            #print(os.path.join("imagenes/Benign", nombre))
                        if row["Cancer"] == 1:
                            np.save(os.path.join(f"{pathNumpys}/Cancer", nombre), arrayImagenes)
                        #print(os.path.join("imagenes/Cancer", nombre))

