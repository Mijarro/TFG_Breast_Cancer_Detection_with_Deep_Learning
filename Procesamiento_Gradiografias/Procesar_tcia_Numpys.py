import csv
import os
from tqdm import tqdm
import pandas as pd


pathcsv = "D:/Codigo/Datos/InfValidation/file-paths-validation.csv"
pathTCIA = 'D:/Codigo/Datos/InfValidation/BSC-DBT-Validation-manifest.tcia'
pathNumpys = "D:/Numpys/imagenesValCompletas/"

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
        view = row["View"]
        nombre = f"{view}-{index}.npy"
        if os.path.exists(os.path.join(f"{pathNumpys}/Normal", nombre)) or os.path.exists(os.path.join(f"{pathNumpys}/Actionable", nombre)) or os.path.exists(os.path.join(f"{pathNumpys}/Benign", nombre)) or os.path.exists(os.path.join(f"{pathNumpys}/Cancer", nombre)):
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
