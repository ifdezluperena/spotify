import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Configuración inicial
st.set_page_config(page_title="Portfolio Iván", page_icon="📊", layout="wide")

df_tracks = pd.read_csv("../portfolio/data/music/raw/tracks.csv")

# Sidebar
menu = st.sidebar.radio("Navegación", ["Inicio", "Música", "Energía", "Extra"])

# Página de Inicio
if menu == "Inicio":
    st.title("👋 Bienvenido a mi Portfolio de Data Analyst")
    st.write("""
    Soy Iván, ingeniero en Energías Renovables y formado en Data Science.  
    Aquí muestro proyectos de análisis y visualización de datos sobre distintos temas que me interesan.  
    """)
    st.markdown("**Tecnologías:** Python, SQL, Power BI, Streamlit, Azure")
    st.markdown("[🔗 LinkedIn](https://linkedin.com) | [💻 GitHub](https://github.com) | [📄 CV en PDF](#)")

# Proyecto 1: Música
elif menu == "Música":
    st.header("🎵 Análisis de mi música favorita (Spotify)")
    st.write("Exploración de mis hábitos musicales con datos de Spotify API.")

     # --- gráfico: canciones más populares ---
    top_tracks = df_tracks.nlargest(10, "popularity")
    fig, ax = plt.subplots()
    ax.barh(top_tracks["track_name"], top_tracks["popularity"], color="skyblue")
    ax.set_xlabel("Popularidad")
    ax.set_ylabel("Canción")
    ax.invert_yaxis()
    st.pyplot(fig)
   
# Proyecto 2: Energía
elif menu == "Energía":
    st.header("🌱 Análisis de Energía Renovable en Europa")
    st.write("Estudio de la evolución de la producción de energías limpias en diferentes países.")
    # Placeholder
    st.bar_chart({"España": [30], "Alemania": [45], "Francia": [25]})

# Proyecto Extra
elif menu == "Extra":
    st.header("📊 Proyecto Extra")
    st.write("Aquí iría otro análisis de datos sobre deportes, películas o datos personales.")

