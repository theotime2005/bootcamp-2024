"""
BootCamp 2024
Jour 6
Partie 1
"""

import pandas as pd
from fastparquet import ParquetFile
from pyarrow import PythonFile

def  read_parquet(filename: str) -> pd.DataFrame:
    """
    Read a parquet file and return a DataFrame with the 10 first lines
    """
    pf = ParquetFile(filename)
    df = pf.to_pandas()
    return df.head(10)
print(read_parquet('/Users/theotime/epitech-projets/2024-2025/piscine-python/documents/Jour 6/flights.parquet'))

# -----------------------------------
def  read_parquet_columns(filename: str, columns: list) -> pd.DataFrame :
    """
    Read a parquet file and return a DataFrame with selected columns
    """
    pf = ParquetFile(filename)
    df = pf.to_pandas(columns=columns)
    return df

# -----------------------------------
def  	read_parquet_batch(filename: str, batch_size: list) -> pd.DataFrame:
    """
    Read a parquet file and return a DataFrame with selected batch size
    """
    # Ouvrir le fichier Parquet
    parquet_file = ParquetFile(file_path)

    # Liste pour stocker les DataFrames de chaque batch
    dfs = []

    # Itérer sur les batches
    for batch in parquet_file.iter_batches(batch_size=batch_size):
        # Convertir le batch en DataFrame Pandas
        df_batch = batch.to_pandas()

        # Prendre les deux premières lignes
        df_first_two_rows = df_batch.head(2)

        # Ajouter ce DataFrame à la liste
        dfs.append(df_first_two_rows)

    # Concaténer tous les DataFrames de la liste
    final_df = pd.concat(dfs, ignore_index=True)

    # Réinitialiser les index avant de retourner le DataFrame final
    final_df.reset_index(drop=True, inplace=True)

    return final_df
