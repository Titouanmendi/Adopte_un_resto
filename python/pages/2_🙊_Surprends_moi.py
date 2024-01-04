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
