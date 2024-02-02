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


# -- Sidebar

df = pd.read_csv("data/restaurants.csv")
df = df[df['new']]
df["food_type"] = df["food_type"].apply(literal_eval)


# -- Main page

tieqson = (48.8732918,2.3513939)

show_map = st.toggle("Liste / Carte", value=True)

# df = pd.read_csv("data/restaurants.csv")
if show_map:
    st.markdown("### Carte des restaurants")
    #lat_lon = filtered_df.apply(lambda row: (row["lat"], row["lon"]), axis=1).to_list()
    m = folium.Map(location=tieqson, tiles="Cartodb Positron", zoom_start=13)
    marker_cluster = MarkerCluster().add_to(m)
    for index, row in df.iterrows():
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

    df["price_emoji"] = df["price"].map({1: "€", 2: "€€", 3: "€€€"})

    for index, row in df.iterrows():
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
