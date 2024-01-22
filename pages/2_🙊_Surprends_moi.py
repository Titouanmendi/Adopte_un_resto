import ast
from streamlit_card import card
import streamlit as st
import numpy as np
import pandas as pd
import base64

from utils import convert_words_to_emojis, district_list, lieu_mapping2



# -- Set page config
st.set_page_config(page_title="Adopte un resto", page_icon="🔥")

df = pd.read_csv("data/restaurants.csv")

df["price_emoji"] = df["price"].map({1: "€", 2: "€€", 3: "€€€"})

st.sidebar.markdown("## Filtres")

lieu = st.sidebar.radio(
    "Lieu",
    ("Partout", "Patisserie", "Proche de chez Jaz", "Proche du taff de Jaz"),
)
lieu_value = lieu_mapping2[lieu]
if lieu_value != "Partout":
    df = df[df[lieu_value]]

filepath = "assets/logo.png"
with open(filepath, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

random_restaurant_1 = np.random.choice(df["name"])

random_restaurant_2 = np.random.choice(df["name"])
while random_restaurant_2 == random_restaurant_1:
    random_restaurant_2 = np.random.choice(df["name"])

random_restaurant_3 = np.random.choice(df["name"])
while random_restaurant_3 == random_restaurant_2 or random_restaurant_3 == random_restaurant_1:
    random_restaurant_3 = np.random.choice(df["name"])

print(random_restaurant_1)
print(random_restaurant_2)
print(random_restaurant_3)

row_restaurant_1 = df[df["name"] == random_restaurant_1].iloc[0]
print(row_restaurant_1)
st.markdown("### 3 restaurants au hasard")
restaurant1 = card(
    title=random_restaurant_1,
    text=[
        f'Prix : {row_restaurant_1["price_emoji"]}',
        f'Note : {row_restaurant_1["review"]}',
        f'Type de nourriture : {convert_words_to_emojis(row_restaurant_1["food_type"])}',
        f'Arrondissement : {row_restaurant_1["district"]}',
    ],
    image=data,
    url=row_restaurant_1["gmaps_link"],
    styles={
        "card": {
            "width": "100%",  # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "300px",  # <- if you want to set the card height to 300px
        },
    },
)

row_restaurant_2 = df[df["name"] == random_restaurant_2].iloc[0]
restaurant2 = card(
    title=random_restaurant_2,
    text=[
        f'Prix : {row_restaurant_2["price_emoji"]}',
        f'Note : {row_restaurant_2["review"]}',
        f'Type de nourriture : {convert_words_to_emojis(row_restaurant_2["food_type"])}',
        f'Arrondissement : {row_restaurant_2["district"]}',
    ],
    image=data,
    url=row_restaurant_2["gmaps_link"],
    styles={
        "card": {
            "width": "100%",  # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "300px",  # <- if you want to set the card height to 300px
        },
    },
)

row_restaurant_3 = df[df["name"] == random_restaurant_3].iloc[0]
restaurant3 = card(
    title=random_restaurant_3,
    text=[
        f'Prix : {row_restaurant_3["price_emoji"]}',
        f'Note : {row_restaurant_3["review"]}',
        f'Type de nourriture : {convert_words_to_emojis(row_restaurant_3["food_type"])}',
        f'Arrondissement : {row_restaurant_3["district"]}',
    ],
    image=data,
    url=row_restaurant_3["gmaps_link"],
    styles={
        "card": {
            "width": "100%",  # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "300px",  # <- if you want to set the card height to 300px
        },
    },
)
