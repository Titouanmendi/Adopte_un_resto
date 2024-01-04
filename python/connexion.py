import streamlit as st


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Connecte-toi pour adopter ton restaurant! 😋")

def authentification_et_redirection():
    # Champ d'entrée pour l'identifiant
    id_utilisateur = st.text_input("Identifiant")

    # Champ d'entrée pour le mot de passe
    mdp_utilisateur = st.text_input("Mot de passe", type="password")

    # Bouton pour soumettre le formulaire et rediriger vers une autre page
    #bouton_connexion = st.button("VITE J'AI FAIM")
    
    st.link_button("VITE J'AI FAIM","http://localhost:8501/Adopte_un_resto")
        # # Redirection vers une autre page (remplacez l'URL ci-dessous par celle de votre page d'authentification)
        # #st.markdown("<script>window.location.href = 'http://localhost:8501/Adopte_un_resto';</script>", unsafe_allow_html=True)
        # st.markdown('<a href="http://localhost:8501/Adopte_un_resto" target="_blank">Rediriger</a>', unsafe_allow_html=True)


# Appeler la fonction d'authentification et redirection
authentification_et_redirection()

