import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters
from ast import literal_eval

# -- Set page config
apptitle = 'Adopte un resto'

st.set_page_config(page_title=apptitle, page_icon=":fork_knife_plate:")

# -- Default detector list
detectorlist = ['H1','L1', 'V1']


# -- Sidebar

df = pd.read_csv("data/restaurants.csv")
df['food_constraints']=df['food_constraints'].apply(literal_eval)
df['food_type']=df['food_type'].apply(literal_eval)

    
st.sidebar.markdown("## Filtres")

time_available = st.sidebar.slider('Distance (minutes)', 0, 30, 1)  

df_food_contraints = pd.DataFrame({
    'food_constraints': df['food_constraints'].explode().unique()
})
food_constraints = st.sidebar.multiselect(
    'Régime', options=df_food_contraints, default=[]
)

# df_food_type = pd.DataFrame({
#     'food_type': df['food_type'].explode().unique()
# })
# food_types = st.sidebar.multiselect(
#     'Pas envie', options=df_food_type, default=[]
# )

price = st.sidebar.radio(
    "Prix",
    ("€", "€€", "€€€"),
    help="(€ (0-10), €€ (10-20) et €€€ (20-plus)",
)

price_mapping = {"€":1, "€€":2, "€€€":3}
price_value = price_mapping[price]


filtered_df = df[df['dist_minutes']<=time_available].assign(**{
    'all_constraints_validated': lambda df: df['food_constraints'].apply(lambda c: set(food_constraints) <= set(c))
})
filtered_df = filtered_df[filtered_df['all_constraints_validated']]

filtered_df = filtered_df[filtered_df['price']<=price_value]
  

display_restaurants = st.sidebar.button("Manger !")


# Title the app
st.title('Liste de restaurants')

st.markdown("""
 * Choisissez un restaurant grâce aux filtres à gauche
""")



