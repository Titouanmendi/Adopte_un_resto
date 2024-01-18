import ast
from streamlit_card import card
import streamlit as st
import numpy as np
import pandas as pd
import base64


# -- Set page config
st.set_page_config(page_title="Adopte un resto", page_icon="🔥")

from utils import convert_words_to_emojis

df = pd.read_csv("data/restaurants.csv")

df["constraints_list"] = df["food_constraints"].apply(
    lambda x: ast.literal_eval(x) if pd.notnull(x) else []
)

df["price_emoji"] = df["price"].map({1: "€", 2: "€€", 3: "€€€"})

filepath = "assets/logo.png"
with open(filepath, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

random_restaurant_1 = np.random.choice(df["name"])

vegetarian_restaurants = df[df["constraints_list"].apply(lambda x: "VEGE" in x)]
random_restaurant_2 = np.random.choice(vegetarian_restaurants["name"])
while random_restaurant_2 == random_restaurant_1:
    random_restaurant_2 = np.random.choice(vegetarian_restaurants["name"])

halal_restaurants = df[df["constraints_list"].apply(lambda x: "VEGE" in x)]
random_restaurant_3 = np.random.choice(halal_restaurants["name"])
while random_restaurant_3 == random_restaurant_2 or random_restaurant_3 == random_restaurant_1:
    random_restaurant_3 = np.random.choice(halal_restaurants["name"])

print(random_restaurant_1)
print(random_restaurant_2)
print(random_restaurant_3)

row_restaurant_1 = df[df["name"] == random_restaurant_1].iloc[0]
print(row_restaurant_1)
st.markdown("### Un restaurant au hasard")
restaurant1 = card(
    title=random_restaurant_1,
    text=[
        f'Prix : {row_restaurant_1["price_emoji"]}',
        f'Note: {row_restaurant_1["review"]}',
        f'Type de nourriture : {convert_words_to_emojis(row_restaurant_1["food_type"])}',
        f'Régimes alimentaires : {convert_words_to_emojis(row_restaurant_1["food_constraints"])}',
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
st.markdown("### Un restaurant végétarien au hasard")
restaurant2 = card(
    title=random_restaurant_2,
    text=[
        f'Prix : {row_restaurant_2["price_emoji"]}',
        f'Note: {row_restaurant_2["review"]}',
        f'Type de nourriture : {convert_words_to_emojis(row_restaurant_2["food_type"])}',
        f'Régimes alimentaires : {convert_words_to_emojis(row_restaurant_2["food_constraints"])}',
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
st.markdown("### Un restaurant halal au hasard")
restaurant3 = card(
    title=random_restaurant_3,
    text=[
        f'Prix : {row_restaurant_3["price_emoji"]}',
        f'Note: {row_restaurant_3["review"]}',
        f'Type de nourriture : {convert_words_to_emojis(row_restaurant_3["food_type"])}',
        f'Régimes alimentaires : {convert_words_to_emojis(row_restaurant_3["food_constraints"])}',
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
