import ast
from streamlit_card import card
import numpy as np
import pandas as pd

df = pd.read_csv("data/restaurants.csv")

df["constraints_list"] = df["food_constraints"].apply(
    lambda x: ast.literal_eval(x) if pd.notnull(x) else []
)

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
restaurant1 = card(
    title=random_restaurant_1,
    text=[
        "Un restaurant végétarien au hasard",
        f'Prix : {row_restaurant_1["price"]}',
        f'Note: {row_restaurant_1["review"]}',
        f'Temps de trajet : {row_restaurant_1["dist_minutes"]} min',
        f'Type de nourriture : {row_restaurant_1["food_type"]}',
        f'Régimes alimentaires : {row_restaurant_1["food_constraints"]}',
    ],
    image="assets/" + row_restaurant_1["img"],
    url=row_restaurant_1["gmaps_link"],
)

row_restaurant_2 = df[df["name"] == random_restaurant_2].iloc[0]
restaurant2 = card(
    title=random_restaurant_2,
    text=[
        "Un restaurant végétarien au hasard",
        f'Prix : {row_restaurant_2["price"]}',
        f'Note: {row_restaurant_2["review"]}',
        f'Temps de trajet : {row_restaurant_2["dist_minutes"]} min',
        f'Type de nourriture : {row_restaurant_2["food_type"]}',
        f'Régimes alimentaires : {row_restaurant_2["food_constraints"]}',
    ],
    image="assets/" + row_restaurant_2["img"],
    url=row_restaurant_2["gmaps_link"],
)

row_restaurant_3 = df[df["name"] == random_restaurant_3].iloc[0]
restaurant3 = card(
    title=random_restaurant_3,
    text=[
        "Un restaurant végétarien au hasard",
        f'Prix : {row_restaurant_3["price"]}',
        f'Note: {row_restaurant_3["review"]}',
        f'Temps de trajet : {row_restaurant_3["dist_minutes"]} min',
        f'Type de nourriture : {row_restaurant_3["food_type"]}',
        f'Régimes alimentaires : {row_restaurant_3["food_constraints"]}',
    ],
    image="assets/" + row_restaurant_3["img"],
    url=row_restaurant_3["gmaps_link"],
)
