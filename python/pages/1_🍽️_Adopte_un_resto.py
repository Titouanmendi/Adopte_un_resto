import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters
from ast import literal_eval

# -- Set page config
apptitle = 'Adopte un resto'

st.set_page_config(page_title=apptitle, page_icon=":fork_knife_plate:")

df = pd.read_csv("data/restaurants.csv")

# -- Default detector list
detectorlist = ['H1','L1', 'V1']

# Title the app
st.title('Liste de restaurants')

st.markdown("""
 * Choisissez un restaurant grâce aux filtres à gauche
""")

    
st.sidebar.markdown("## Filtres")
time_available = st.sidebar.slider('Distance (minutes)', 1, 30, 1)  # min, max, default



# literal_eval

# df[''].eexplode()





# dfRegime = pd.DataFrame({
#     'Regime': donnees_regime
# })

# dfPlats = pd.DataFrame({
#     'platsBof': donnee_platsPasEnvie
# })


# dynamic_filters = DynamicFilters(dfRegime , filters=['food_types'])
# dynamic_filters.display_filters(location='sidebar')
# df_filtered = dynamic_filters.filter_df()


# dynamic_filters_1 = DynamicFilters(dfPlats , filters=['platsBof'])
# dynamic_filters_1.display_filters(location='sidebar')
# df_filtered = dynamic_filters_1.filter_df()



check1 = st.sidebar.button("Manger !")





