import csv
import os
from tqdm import tqdm
import pandas as pd

/*
    Este código se encarga de comprobar el numero de imágenes descargadas para un fichero de descarga .tcia dado.
*/

pathcsv = "/media/miguel/Granja azul/TFG/Codigo/InfTraining/file-paths-train.csv"
pathTCIA = '/media/miguel/Granja azul/TFG/Codigo/InfTraining/BSC-DBT-Train-manifest.tcia'
pathRadiografias = "/media/miguel/Granja azul/TFG/Radiografias Training/Prinicipal/manifest-1617905855234/"

borrados=0
numero_de_filas = 0
bandera = False

df = pd.read_csv(pathcsv)
# Leer y modificar el archivo BSC-DBT-Train-manifest.tcia
with open(pathTCIA, 'r') as manifest_file:
    lines = manifest_file.readlines()
    numero_de_filas = len(lines)
# Leer el archivo CSV
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Cargando imágen"):
        ruta_imagen = os.path.join(pathRadiografias, row["descriptive_path"])
        ruta_imagen = ruta_imagen.replace("000000-", "000000-NA-")
        if os.path.exists(ruta_imagen):
            classic_path = row['classic_path']
            parte_classic_path = classic_path.split("/")[-2]
            indice = 0
            #print(parte_classic_path)
            bandera = False
            for i, linea in enumerate(lines):
                if parte_classic_path in linea:
                    indice=i
                    bandera = True
                    break
            if bandera:
                del lines[indice]
                borrados += 1

with open(pathTCIA, 'w') as manifest_file:
    manifest_file.writelines(lines)
"data"
print(f"Proceso completado. Se han borrado {borrados} filas")
print(f"Fichero original con {numero_de_filas} filas.")
print(f"Fichero restante con {len(lines)} filas.")
