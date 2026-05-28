# semantic-critical-thinking-ecuador
Sistema de búsqueda semántica para Pensamiento Crítico contextualizado al Ecuador. Trabajo de titulación de la Maestría en Inteligencia Artificial Aplicada (UDLA).   Usa Sentence-Transformers + FAISS para recuperar ejemplos reales ecuatorianos de falacias y sesgos cognitivos desde consultas en lenguaje natural.
# Buscador Semántico de Pensamiento Crítico - Ecuador

**Herramienta de búsqueda semántica contextualizada al Ecuador** para la enseñanza de Pensamiento Crítico en la Universidad de Las Américas (UDLA).

Proyecto de titulación de la **Maestría en Inteligencia Artificial Aplicada**.

---

## 🎯 Descripción

Sistema que permite a estudiantes y docentes buscar ejemplos reales ecuatorianos de **falacias lógicas**, **sesgos cognitivos** y **heurísticas** mediante lenguaje natural. 

En lugar de depender de ejemplos genéricos o extranjeros, el sistema recupera casos contextualizados de la realidad política, mediática y social del Ecuador usando **búsqueda semántica**.

### Resultados clave
- **Recall@5**: 0.78 (vs 0.52 del baseline)
- **MRR@5**: 0.72 (vs 0.41 del baseline)
- Supera significativamente a enfoques léxicos y de lógica difusa

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **Sentence-Transformers** (`paraphrase-multilingual-MiniLM-L12-v2`)
- **FAISS** (Facebook AI Similarity Search)
- **Streamlit** (interfaz web)
- **pandas** + procesamiento de texto

---

## ✨ Características

- Búsqueda semántica en lenguaje natural (no requiere términos técnicos)
- Dataset curado de **100+ casos ecuatorianos**
- Respuestas con explicación pedagógica y fuente verificada
- Interfaz intuitiva diseñada para uso en el aula
- Arquitectura ligera y de costo cero

---

## 🚀 Cómo ejecutar localmente

```bash
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate    # En Windows: venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
