import streamlit as st
import requests
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Codex AI - Manual de Normatividad",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LÓGICA DEL CHATBOT CON IA (GEMINI API) ---
def call_gemini_api(messages):
    api_key = ""  # El entorno proporciona la clave automáticamente
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={api_key}"
    
    # Sistema de Instrucción para que la IA sea experta en el Codex
    system_prompt = """Eres un Asistente Experto en el Codex Alimentarius, especializado en productos cárnicos y específicamente en Jamón Curado Cocido (Norma CXS 96-1981).
    Tu objetivo es ayudar a estudiantes y profesionales de gastronomía (como Diego Armando Cuenca Lavana) a entender las normas:
    - CXS 96-1981 (Jamón Curado Cocido)
    - CXC 1-1969 (Higiene General)
    - CXC 58-2005 (Higiene de la Carne)
    - CXG 66-2008 (Aditivos/Aromas)
    - CXS 192-1995 (Aditivos Alimentarios)
    Responde con tono profesional, técnico pero accesible, y da recomendaciones basadas en seguridad alimentaria, procesos de curado, control de patógenos y etiquetado."""

    # Formatear historial para la API
    contents = []
    for m in messages:
        contents.append({
            "role": "user" if m["role"] == "user" else "model",
            "parts": [{"text": m["content"]}]
        })

    payload = {
        "contents": contents,
        "systemInstruction": {"parts": [{"text": system_prompt}]}
    }

    # Implementación de Exponential Backoff (1s, 2s, 4s, 8s, 16s)
    backoff_times = [1, 2, 4, 8, 16]
    for i in range(5):
        try:
            response = requests.post(url, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No pude procesar la respuesta.")
        except Exception:
            pass
        time.sleep(backoff_times[i])
    
    return "Lo siento, el servicio de IA está experimentando alta demanda. Por favor, intenta de nuevo en unos segundos."

# --- SISTEMA DE DISEÑO Y CSS AVANZADO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Fondo base */
    .stApp { background-color: #020617; }
    
    /* Sidebar Chat Estética */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    h1, h2, h3, .serif-text {
        font-family: 'Playfair Display', serif !important;
        color: #f8fafc;
    }

    p, span, div, .sans-text {
        font-family: 'Inter', sans-serif !important;
        color: #94a3b8;
    }

    /* Centrado Portada */
    .stApp:has(.splash-marker) [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
    }

    .hero-box { text-align: center; padding: 40px; z-index: 10; }
    .hero-icon {
        font-size: 4rem;
        filter: drop-shadow(0 0 20px rgba(59, 130, 246, 0.6));
        animation: float 4s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }

    .main-title {
        font-size: 5.5rem; line-height: 0.8; letter-spacing: -4px;
        background: linear-gradient(to bottom, #ffffff 0%, #64748b 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    .accent-title {
        font-size: 5.5rem; line-height: 0.8; letter-spacing: -4px;
        color: #3b82f6; font-style: italic; font-weight: 700;
    }

    /* Tarjetas Minimalistas */
    .card-link { text-decoration: none !important; display: block; margin-bottom: 25px; }
    .custom-card {
        background-color: #ffffff; padding: 35px; border-radius: 35px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        transition: all 0.5s ease;
    }
    .custom-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 40px 80px -15px rgba(0, 0, 0, 0.2);
        border-color: #3b82f6;
    }
    .doc-title { color: #0f172a; font-size: 1.5rem; font-weight: 800; }
    .doc-code {
        color: #2563eb; font-weight: 700; font-size: 0.75rem;
        background: #eff6ff; padding: 4px 12px; border-radius: 8px;
    }

    /* Botones */
    div.stButton > button {
        border-radius: 25px !important; background: #ffffff !important;
        color: #020617 !important; padding: 18px 50px !important;
        font-weight: 800 !important; border: none !important;
        letter-spacing: 3px; box-shadow: 0 15px 35px rgba(0,0,0,0.4) !important;
    }
    div.stButton > button:hover {
        background: #3b82f6 !important; color: #ffffff !important; transform: scale(1.05) !important;
    }

    .cat-divider {
        margin: 60px 0 30px 0; padding: 12px 25px;
        background: rgba(255,255,255,0.03); border-left: 3px solid #3b82f6;
        color: #f8fafc; font-weight: 800; letter-spacing: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CHATBOT EN EL SIDEBAR (ESQUINA IZQUIERDA) ---
with st.sidebar:
    st.markdown("<h3 class='serif-text' style='color: white;'>Asistente Codex AI</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; opacity: 0.6;'>Resuelvo dudas sobre normas, higiene y procesos del Codex.</p>", unsafe_allow_html=True)
    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensajes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada de chat
    if prompt := st.chat_input("¿Qué deseas consultar?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Consultando normatividad..."):
                response = call_gemini_api(st.session_state.messages)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# --- ESTADO DE NAVEGACIÓN ---
if 'view' not in st.session_state:
    st.session_state.view = 'splash'

# --- 1. PORTADA ---
if st.session_state.view == 'splash':
    st.markdown('<div class="splash-marker"></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-box">
            <div class="hero-icon">📜</div>
            <h1 class="main-title">MANUAL DE</h1>
            <h1 class="accent-title">NORMATIVIDAD</h1>
            <p style='letter-spacing: 15px; font-weight: 300; margin-top: 40px; opacity: 0.6; color: white; text-transform: uppercase; font-size: 0.9rem;'>CODEX ALIMENTARIUS</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("INGRESAR"):
        st.session_state.view = 'selection'
        st.rerun()
    
    st.markdown("<br><br><br><p style='text-align: center; color: #475569; font-size: 0.75rem; letter-spacing: 8px; font-weight: 600;'>DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. SELECCIÓN ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4rem; letter-spacing: -3px; color: white;'>Selección de Producto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.2rem;'>Identifique el estándar técnico a inspeccionar.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
            <div class="custom-card" style="text-align: center; background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);">
                <div style="font-size: 5rem; margin-bottom: 20px;">🍖</div>
                <h3 style="font-size: 2.5rem; color: #0f172a; margin-bottom: 5px; letter-spacing: -1px; font-weight: 900;">JAMÓN CURADO COCIDO</h3>
                <div class="doc-code" style="font-size: 1rem;">CXS 96-1981</div>
                <p style="color: #64748b; font-size: 1.1rem; margin-top: 25px; line-height: 1.6; font-weight: 400; font-style: italic;">
                    Estándar internacional de identidad y seguridad alimentaria.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("VER MANUAL TÉCNICO →"):
            st.session_state.view = 'manual'
            st.rerun()

# --- 3. MANUAL (TARJETAS CLICKABLES) ---
elif st.session_state.view == 'manual':
    st.markdown("<style>.stApp { background-color: #fcfdfe; }</style>", unsafe_allow_html=True)
    
    col_back, col_title = st.columns([1, 6])
    with col_back:
        if st.button("← VOLVER"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<h1 style='color: #0f172a; font-size: 3.5rem; letter-spacing: -3px; font-weight: 900;'>Documentación Técnica</h1>", unsafe_allow_html=True)
    
    manual_data = {
        "I. PRÁCTICAS (CXC)": [
            ("Higiene / Principios", "CXC 1-1969", "Protocolos básicos de higiene para la cadena de suministro.", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
            ("Higiene / Carne", "CXC 58-2005", "Directrices sanitarias rigurosas para la manipulación de carne.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXC%B58-2005%252FCXC_058s.pdf"),
            ("Higiene / Pocos Ácidos", "CXC 23-1979", "Seguridad en procesos térmicos y envasado hermético.", "https://www.fao.org/3/y1579s/y1579s02.pdf"),
        ],
        "II. DIRECTRICES (CXG)": [
            ("Aditivos / Aromatizantes", "CXG 66-2008", "Control de sustancias y aromas de humo.", "https://www.fao.org/input/download/standards/11020/cxg_066s.pdf"),
            ("Higiene / Microbiano", "CXG 21-1997", "Parámetros biológicos de inocuidad.", "https://www.fao.org/4/y5307s/y5307s04.htm"),
        ],
        "III. GENERALES (CXS)": [
            ("Aditivos Alimentarios", "CXS 192-1995", "Regulación sobre aditivos y límites permitidos.", "https://www.fao.org/gsfaonline/docs/CXS_192s.pdf"),
            ("Contaminantes / Toxinas", "CXS 193-1995", "Vigilancia de metales pesados y toxinas.", "https://www.fao.org/fileadmin/user_upload/livestockgov/documents/CXS_193s.pdf"),
            ("Etiquetado / Envasados", "CXS 1-1985", "Transparencia informativa e ingredientes.", "https://www.fao.org/4/y2770s/y2770s02.htm"),
            ("Etiquetado / No Minorista", "CXS 346-2021", "Requisitos para distribución industrial.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B346-2021%252FCXS_346s.pdf"),
            ("Análisis y Muestreo", "CXS 234-1999", "Metodologías de laboratorio para verificación.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B234-1999%252FCXS_234s.pdf"),
        ]
    }

    for categoria, items in manual_data.items():
        st.markdown(f"<div class='cat-divider'>{categoria}</div>", unsafe_allow_html=True)
        cols = st.columns(2)
        for i, (nombre, codigo, desc, url) in enumerate(items):
            with cols[i % 2]:
                st.markdown(f"""
                    <a href="{url}" target="_blank" class="card-link">
                        <div class="custom-card">
                            <div class="doc-code">{codigo}</div>
                            <div class="doc-title">{nombre}</div>
                            <p class="doc-desc">{desc}</p>
                        </div>
                    </a>
                """, unsafe_allow_html=True)

    st.markdown("<br><br><p style='text-align: center; color: #94a3b8; font-size: 0.9rem; letter-spacing: 5px; font-weight: 700;'>CODEX ALIMENTARIUS • GASTRONOMÍA • 2026</p>", unsafe_allow_html=True)
