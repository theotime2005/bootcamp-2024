# %% [markdown]
# # Markdown
# This is a markdown text

# %%
"Hello world"

# %%
from random import randint

my_list=[]

count = randint(0,100)

for i in range(count):
    my_list.append(randint(0,1000))
print(my_list)

# %% [markdown]
# ## On affiche les éléments suivants:
# - Somme,
# - Moyenne avec 1 chiffre après la virgule,
# - Minimum,
# - Maximum

# %%
informations = (sum(my_list), round(sum(my_list)/len(my_list), 1), sorted(my_list)[0], sorted(my_list)[-1])
print(informations)

# %%
import pandas as pd
from fastparquet import ParquetFile

def import_parquet(file):
    pf = ParquetFile(file)
    df = pf.to_pandas()
    return df

import_parquet('flights.parquet')

# %%
import ipywidgets as widgets
from IPython.display import display

# Création d'un slider
slider = widgets.IntSlider(
    value=50,  # Valeur initiale
    min=0,     # Valeur minimale
    max=100,   # Valeur maximale
    step=1,    # Incrément
    description='Slider:',
    style={'description_width': 'initial'}
)

# Affichage du slider
display(slider)

# %%
def show_new_value(value):
    print(f"La nouvelle valeur est: {value}")

slider.observe(show_new_value, names='value')

# %%
button = widgets.Button(description="Voici un bouton")

display(button)

# %%
def is_clicked(b):
    print("Bouton cliqué!!!!")

button.on_click(is_clicked)


