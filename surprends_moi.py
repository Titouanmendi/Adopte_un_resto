import pandas as pd
import numpy as np

# df = pd.read_csv("data/scraping.csv")

df = pd.DataFrame(
    {
        "name": ["Restaurant1", "Restaurant2", "Restaurant3", "Restaurant4", "Restaurant5"],
        "vegetarian": [True, False, True, False, True],
        "halal": [False, True, True, False, False],
    }
)

random_restaurant_1 = np.random.choice(df["name"])

vegetarian_restaurants = df[df["vegetarian"] == True]
random_restaurant_2 = np.random.choice(vegetarian_restaurants["name"])

halal_restaurants = df[df["halal"] == True]
random_restaurant_3 = np.random.choice(halal_restaurants["name"])
