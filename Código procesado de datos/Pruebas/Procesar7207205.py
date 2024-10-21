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


def coger5Imagenes(arrayImagenes):
    # Cojemos 5 imagenes del total
    n = len(arrayImagenes)
    #print(arrayImagenes.shape)
    indices_seleccionados = [2, n // 4, n // 2, 3 * n // 4, n - 3]
    # Seleccionar las imágenes en las posiciones especificadas
    imagenes_seleccionadas = arrayImagenes[indices_seleccionados]
    #print(imagenes_seleccionadas.shape)
    return imagenes_seleccionadas


pathdf = "/media/miguel/Granja azul/TFG/Codigo/InfValidation/merged_dfValidation_serialized.pickle"
pathNumpys = "/media/miguel/Granja azul/TFG/imagenesValCompletas"
pathNumpySave = "/media/miguel/SYSTEM/TFG/ImagenesValidacion"

# Cargar el DataFrame desde un archivo pickle serializado
merged_df = pd.read_pickle(pathdf)

# Iterar sobre las filas del DataFrame merged_df
for index, row in tqdm(merged_df.iterrows(), total=merged_df.shape[0], desc="Cargando imagen"):
    view = row["View"]
    nombre = f"{view}-{index}.npy"
    if os.path.exists(os.path.join(f"{pathNumpys}/Normal", nombre)):
        arrayImagenes = np.load(os.path.join(f"{pathNumpys}/Normal", nombre))
        arrayImagenes = coger5Imagenes(arrayImagenes)
        np.save(os.path.join(f"{pathNumpySave}/Normal", nombre), arrayImagenes)
    if os.path.exists(os.path.join(f"{pathNumpys}/Actionable", nombre)):
        arrayImagenes = np.load(os.path.join(f"{pathNumpys}/Actionable", nombre))
        arrayImagenes = coger5Imagenes(arrayImagenes)
        np.save(os.path.join(f"{pathNumpySave}/Actionable", nombre), arrayImagenes)
    if os.path.exists(os.path.join(f"{pathNumpys}/Benign", nombre)):
        arrayImagenes = np.load(os.path.join(f"{pathNumpys}/Benign", nombre))
        arrayImagenes = coger5Imagenes(arrayImagenes)
        np.save(os.path.join(f"{pathNumpySave}/Benign", nombre), arrayImagenes)
    if os.path.exists(os.path.join(f"{pathNumpys}/Cancer", nombre)):
        arrayImagenes = np.load(os.path.join(f"{pathNumpys}/Cancer", nombre))
        arrayImagenes = coger5Imagenes(arrayImagenes)
        np.save(os.path.join(f"{pathNumpySave}/Cancer", nombre), arrayImagenes)
                    
    
