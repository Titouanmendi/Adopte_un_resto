import streamlit as st
import pandas as pd
from ast import literal_eval
import base64

import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from streamlit_card import card

from utils import convert_words_to_emojis, district_list, lieu_mapping

# -- Set page config
st.set_page_config(page_title="Adopte un resto", page_icon="🔥")

# -- Set page config
apptitle = "Adopte un resto"


# -- Default detector list
detectorlist = ["H1", "L1", "V1"]


# -- Sidebar

df = pd.read_csv("data/restaurants.csv")
df["food_type"] = df["food_type"].apply(literal_eval)


st.sidebar.markdown("## Filtres")

df_districts = pd.DataFrame({"districts": df["district"].explode().sort_values().unique()})

bakery = st.sidebar.toggle("Goûter", value=False)
if bakery:
    df = df[df['bakery']]

vegan_only = st.sidebar.toggle("Vegan uniquement", value=False)
if vegan_only:
    df = df[df['vegan_only']]

district = st.sidebar.multiselect("Arrondissement", options=df_districts, default=district_list)

price = st.sidebar.radio(
    "Prix",
    ("€", "€€", "€€€"),
    help="€ (0-10), €€ (10-20) et €€€ (20-plus)",
    index=1
)
price_mapping = {"€": 1, "€€": 2, "€€€": 3}
price_value = price_mapping[price]

lieu = st.sidebar.radio(
    "Lieu",
    ("Partout", "Proche de chez Jaz", "Proche du taff de Jaz"),
)

lieu_value = lieu_mapping[lieu]

filtered_df = df[df["price"] <= price_value]
filtered_df = filtered_df[filtered_df["district"].isin(district)]
if lieu_value != "Partout":
    filtered_df = filtered_df[filtered_df[lieu_value]]

print(filtered_df)


# -- Main page

tieqson = (48.8732918,2.3513939)

show_map = st.toggle("Liste / Carte", value=True)

# df = pd.read_csv("data/restaurants.csv")
if show_map:
    st.markdown("### Carte des restaurants")
    #lat_lon = filtered_df.apply(lambda row: (row["lat"], row["lon"]), axis=1).to_list()
    m = folium.Map(location=tieqson, tiles="Cartodb Positron", zoom_start=13)
    marker_cluster = MarkerCluster().add_to(m)
    for index, row in filtered_df.iterrows():
        popup_content = (
            f'<h3>{row["name"]}</h3>'
            f'<p><b>Food Type:</b> {", ".join([word.capitalize() for word in row["food_type"]])}</p>'
            f'<p><b>Price:</b> {row["price"]}</p>'
            f'<p><b>Note:</b> {row["review"]}</p>'
        )
        folium.Marker(
            [row["lat"], row["lon"]], popup=folium.Popup(popup_content, max_width=300),
        ).add_to(marker_cluster)

    folium_static(m, width=800, height=500)
else:
    st.markdown("### Liste des restaurants")

    filepath = "assets/logo.png"
    with open(filepath, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
        data = "data:image/png;base64," + encoded.decode("utf-8")

    filtered_df["price_emoji"] = filtered_df["price"].map({1: "€", 2: "€€", 3: "€€€"})

    for index, row in filtered_df.iterrows():
        res = card(
            title=row["name"],
            text=[
                f'Prix : {row["price_emoji"]}',
                f'Note: {row["review"]}',
                f'Type de nourriture : {convert_words_to_emojis(row["food_type"])}',
            ],
            image=data,
            url=row["gmaps_link"],
            styles={
                "card": {
                    "width": "100%",  # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                    "height": "300px",  # <- if you want to set the card height to 300px
                },
            },
        )
