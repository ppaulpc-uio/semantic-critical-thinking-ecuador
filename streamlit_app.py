import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Configuración de página
st.set_page_config(
    page_title="Buscador Semántico - Pensamiento Crítico Ecuador",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Buscador Semántico de Pensamiento Crítico")
st.markdown("**Ejemplos contextualizados al Ecuador** de falacias lógicas, sesgos cognitivos y heurísticas")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_excel("data/Pensamiento Crítico Ecuatoriano_100_Ejemplos.xlsx")
    df['Caso Texto (Contexto Ecuador)'] = df['Caso Texto (Contexto Ecuador)'].astype(str)
    return df

df = load_data()

# Cargar modelo e índice FAISS
@st.cache_resource
def load_model_and_index(df):
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    texts = df['Caso Texto (Contexto Ecuador)'].tolist()
    embeddings = model.encode(texts, show_progress_bar=False)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner Product (mejor con embeddings normalizados)
    faiss.normalize_L2(embeddings)
    index.add(embeddings.astype('float32'))
    
    return model, index

model, index = load_model_and_index(df)

# Interfaz
st.subheader("Realiza tu consulta")
query = st.text_input(
    "Describe la falacia, sesgo o situación (en lenguaje natural):",
    placeholder="Ejemplo: 'atacar a la persona en vez del argumento' o 'confirmar solo lo que me conviene'"
)

if st.button("🔍 Buscar casos relevantes", type="primary"):
    if query:
        with st.spinner("Buscando..."):
            # Generar embedding de la consulta
            query_embedding = model.encode([query])
            faiss.normalize_L2(query_embedding)
            
            # Buscar los más similares
            k = 5
            D, I = index.search(query_embedding.astype('float32'), k)
            
            st.subheader(f"Resultados para: **{query}**")
            
            for i, idx in enumerate(I[0]):
                if idx < len(df):
                    case = df.iloc[idx]
                    score = D[0][i]
                    
                    with st.expander(f"**{i+1}. {case.get('Subcategoría', 'N/A')}** - Similitud: {score:.3f}"):
                        st.markdown(f"**Descripción:** {case.get('Caso Texto (Contexto Ecuador)', 'N/A')}")
                        st.markdown(f"**Explicación lógica:** {case.get('Explicación Lógica', 'N/A')}")
                        st.markdown(f"**Fuente / Sector:** {case.get('Fuente / Sector', 'N/A')}")
    else:
        st.warning("Por favor ingresa una consulta.")

# Información del proyecto
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.info("**Dataset:** 100 casos curados de la realidad ecuatoriana")
with col2:
    st.info("**Tecnologías:** Sentence-Transformers + FAISS")

st.caption("Trabajo de Titulación - Maestría en Inteligencia Artificial Aplicada | UDLA 2026")