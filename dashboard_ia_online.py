
import streamlit as st
import pandas as pd
import plotly.express as px

# Título del Dashboard
st.set_page_config(page_title="Plan de Acción: IA Online", layout="wide")
st.title("🚀 Dashboard Interactivo: Gana Dinero con IA Online")

# Plan de acción en tabla
data = {
    "Etapa": [
        "Perfil y Marca Personal",
        "Servicios Freelance",
        "Cursos y Mentorías",
        "Contenido y Marketing",
        "Proyecto Propio (SaaS)"
    ],
    "Acciones": [
        "Crear portfolio y optimizar LinkedIn",
        "Publicar gigs en Fiverr y Upwork",
        "Grabar clases y publicar en Udemy",
        "Crear canal de YouTube y redes sociales",
        "Desarrollar y lanzar app de chatbot con IA"
    ],
    "Progreso (%)": [40, 20, 10, 30, 15]
}
df = pd.DataFrame(data)

# Mostrar tabla
st.subheader("📋 Etapas y Acciones Clave")
st.dataframe(df, height=300)

# Visualización: gráfico de progreso
fig = px.bar(df, x="Etapa", y="Progreso (%)", color="Etapa",
             text="Progreso (%)", title="📊 Progreso por Etapa",
             labels={"Progreso (%)": "Completado %"})
fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)

# Checklist interactiva
st.subheader("✅ Checklist Interactiva de Acciones")
with st.expander("Perfil y Marca Personal"):
    st.checkbox("Crear portfolio con tu chatbot IA")
    st.checkbox("Mejorar LinkedIn con IA y Quantum")

with st.expander("Servicios Freelance"):
    st.checkbox("Crear cuenta en Fiverr/Upwork")
    st.checkbox("Publicar gig de chatbot personalizado")
    st.checkbox("Publicar gig de automatización con IA")

with st.expander("Cursos y Mentorías"):
    st.checkbox("Grabar clases introductorias")
    st.checkbox("Publicar curso en Udemy/Gumroad")
    st.checkbox("Abrir perfil en Superprof")

with st.expander("Contenido y Marketing"):
    st.checkbox("Crear canal de YouTube sobre IA")
    st.checkbox("Subir video semanal educativo")
    st.checkbox("Crear reels en TikTok/Instagram")

with st.expander("Proyecto Propio (SaaS)"):
    st.checkbox("Convertir chatbot en app web")
    st.checkbox("Publicar MVP con suscripción")
    st.checkbox("Promocionar en foros o redes")

# Footer
st.markdown("---")
st.markdown("Creado por Jorge Guillem | Powered by Streamlit")
