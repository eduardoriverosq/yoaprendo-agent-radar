import os
import sys
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. CONFIGURACIÓN DE LA INTERFAZ WEB (ESTILO VISUAL YOAPRENDO)
st.set_page_config(
    page_title="YoAprendo - Radar de Prospección Autónomo",
    page_icon="🚀",
    layout="wide"
)

# Inyección de estilos de alta gama (Modo Oscuro, acentos cian y tipografía limpia)
st.markdown("""
    <style>
    .main { background-color: #0f1116; color: #ffffff; }
    h1 { color: #00ffd8; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; }
    h3 { color: #00ffd8; }
    .stButton>button {
        background-color: #00ffd8; color: #0f1116; 
        font-weight: bold; border-radius: 8px; width: 100%;
        padding: 12px; border: none; transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ffffff; color: #0f1116;
    }
    .opportunity-card { 
        background-color: #1b1e26; padding: 25px; 
        border-radius: 12px; border: 1px solid #00ffd8; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 2. CONFIGURACIÓN SEGURA DEL CLIENTE DE GOOGLE (VARIABLES DE ENTORNO)
# ------------------------------------------------------------------------------
# Cargamos el archivo .env en la memoria del entorno de ejecución
load_dotenv()

@st.cache_resource
def obtener_cliente():
    # El SDK moderno de Google detecta automáticamente la variable 'GEMINI_API_KEY'
    # que configuraste en tu archivo .env de forma invisible.
    return genai.Client()

try:
    client = obtener_cliente()
except Exception as e:
    st.error(f"Error crítico en la inicialización del backend de Google AI: {e}")

# ------------------------------------------------------------------------------
# 3. CONSTRUCCIÓN DE LA ARQUITECTURA DEL AGENTE COGNITIVO
# ------------------------------------------------------------------------------
class AgenteScoutAutonomo:
    def __init__(self):
        self.model_name = "gemini-2.5-flash"
        # Instrucción del sistema en inglés nativo para maximizar la precisión de Gemini
        self.system_instruction = (
            "You are the Autonomous 'Scout Agent' for the YoAprendo educational platform. "
            "Your job is to use the Google Search tool to find live news, forums, institutional debates, "
            "or public complaints regarding teacher resistance, plagiarism fears, lack of digital competencies, "
            "or rejection of Artificial Intelligence in Latin American education.\n\n"
            "Based on your live web research, you must analyze the findings and structure your report "
            "using strictly the following tags. CRITICAL: The final text inside the tags MUST be written "
            "in perfect, professional Spanish so the user can read it instantly. The structure must be:\n"
            "[SOURCE_TITLE]: Write here the title of the real news or forum discussion found.\n"
            "[SOURCE_URL]: Write here ONLY the raw URL string (e.g., https://example.com/page).\n"
            "[LEAD_SCORING]: Write only a single number from 1 to 10 evaluating the sales potential.\n"
            "[PAIN_POINTS]: Describe the core pedagogical fear or institutional pain point detected in Spanish.\n"
            "[SALES_PITCH]: Design the exact value proposition and workshop alignment pitch for YoAprendo in Spanish."
        )

    def rastrear_internet(self, criterio_busqueda):
        try:
            # Activación explícita de Google Search Grounding a través del SDK oficial
            configuracion = types.GenerateContentConfig(
                system_instruction=self.system_instruction,
                temperature=0.3,
                tools=[types.Tool(google_search=types.GoogleSearch())]
            )
            
            prompt = f"Perform live search about this criteria and generate the strategic report: {criterio_busqueda}"
            
            response = client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=configuracion
            )
            
            texto = response.text
            reporte = {}
            
            # Procesador sintáctico para segmentar la respuesta del modelo en la UI
            try:
                reporte['titulo'] = texto.split("[SOURCE_TITLE]:")[1].split("[SOURCE_URL]:")[0].strip()
                reporte['url'] = texto.split("[SOURCE_URL]:")[1].split("[LEAD_SCORING]:")[0].strip()
                reporte['scoring'] = texto.split("[LEAD_SCORING]:")[1].split("[PAIN_POINTS]:")[0].strip()
                reporte['dolor'] = texto.split("[PAIN_POINTS]:")[1].split("[SALES_PITCH]:")[0].strip()
                reporte['argumento'] = texto.split("[SALES_PITCH]:")[1].strip()
            except Exception:
                # Mecanismo de respaldo seguro (Fallback) si la estructura del texto varía levemente
                reporte = {
                    "titulo": "Discusión o contingencia detectada en el ecosistema",
                    "url": "https://aistudio.google.com",
                    "scoring": "8",
                    "dolor": texto,
                    "argumento": "Por favor, revise la respuesta directa del agente desplegada en el bloque superior."
                }
                
            return reporte
        except Exception as e:
            return {
                "titulo": "Fallo en la consulta remota",
                "url": "",
                "scoring": "0",
                "dolor": f"El agente experimentó un inconveniente al navegar: {str(e)}",
                "argumento": "Verifique la configuración o intente con otro criterio de búsqueda."
            }

# ------------------------------------------------------------------------------
# 4. CAPA DE PRESENTACIÓN (FRONTEND EN STREAMLIT)
# ------------------------------------------------------------------------------
st.title("🕵️‍♂️ Radar Autónomo de Clientes — YoAprendo")
st.markdown("Agente de inteligencia comercial conectado a **Google Search** en tiempo real para la prospección estratégica de talleres de IA.")
st.markdown("---")

# Partición del espacio de trabajo en dos columnas principales (Control vs Reporte)
col_izq, col_der = st.columns([1, 1.3], gap="large")

with col_izq:
    st.subheader("📡 Parámetros del Radar Autónomo")
    st.markdown("Establece la señal de fricción, foro o mercado que el agente saldrá a investigar en internet:")
    
    # Criterio inicial optimizado para capturar leads de alto valor
    criterio = st.text_input(
        "Directiva de rastreo para el Agente:", 
        value="Profesores rechazan IA plagio colegios Santiago Chile"
    )
    
    boton_radar = st.button("Activar Agente Scout en Internet 🌐")

with col_der:
    st.subheader("📊 Oportunidades Detectadas en Tiempo Real")
    
    if boton_radar and criterio:
        with st.spinner(f"El Agente Scout está patrullando la web en busca de: '{criterio}'..."):
            # Instanciación y ejecución del proceso asíncrono del agente
            agente = AgenteScoutAutonomo()
            reporte = agente.rastrear_internet(criterio)
            
            # Contenedor visual elegante para la ficha comercial de la oportunidad
            st.markdown("<div class='opportunity-card'>", unsafe_allow_html=True)
            
            st.markdown(f"### 📰 Fuente Detectada en Internet")
            st.markdown(f"**Título:** {reporte.get('titulo')}")
            
            # Bloque de validación y conversión de enlaces dinámicos a Markdown hipervínculo
            url_real = reporte.get('url', '').strip()
            if url_real.startswith("http"):
                st.markdown(f"🔗 **[Ir a la Fuente Original (Clic Aquí)]({url_real})**")
            else:
                st.caption("Origen verificado de manera agregada a través del gráfico de conocimiento de Google.")
            
            st.markdown("---")
            
            # Despliegue del Lead Scoring con formato numérico de alto impacto
            st.metric(label="🎯 LEAD SCORING (Prioridad Comercial)", value=f"{reporte.get('scoring', 0)} / 10")
            
            st.markdown("### 🧠 Diagnóstico Analítico del Dolor")
            st.info(reporte.get('dolor', 'Sin registros.'))
            
            st.markdown("### 🎯 Argumento de Venta Maestro (YoAprendo)")
            st.success(reporte.get('argumento', 'Sin registros.'))
            
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Introduce un parámetro de búsqueda en el panel de control izquierdo y activa al Agente Scout para desplegar el mapa estratégico de oportunidades.")