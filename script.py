import pandas as pd

df = pd.read_csv('data/restaurants.csv')
breakpoint()
df = df[df["selection_tits"]]