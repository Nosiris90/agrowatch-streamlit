import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AgroWatch Dashboard", page_icon="🌱")

st.title("🌱 AgroWatch - Monitoring du sol")

st.write("Prototype du dashboard AgroWatch pour le cours GNG1503.")

data = pd.DataFrame({
    "Temps (min)": [0, 5, 10, 15, 20],
    "Humidité (%)": [40, 42, 47, 50, 55],
    "Température (°C)": [18, 19, 20, 21, 22],
})

tab1, tab2 = st.tabs(["Humidité", "Température"])

with tab1:
    fig_h = px.line(data, x="Temps (min)", y="Humidité (%)",
                    title="Évolution de l’humidité du sol")
    st.plotly_chart(fig_h, use_container_width=True)

with tab2:
    fig_t = px.line(data, x="Temps (min)", y="Température (°C)",
                    title="Évolution de la température")
    st.plotly_chart(fig_t, use_container_width=True)
