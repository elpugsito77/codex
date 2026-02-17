import streamlit as st
import requests
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Codex Intelligence - Diego Cuenca",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded" # Forzamos que la IA esté abierta desde el inicio
)

# --- LÓGICA DEL CHATBOT CON IA (GEMINI API) ---
def call_gemini_api(messages):
    # Obtener clave de los secretos de Streamlit
    api_key = st.secrets.get("GEMINI_API_KEY", "")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={api_key}"
    
    system_prompt = """Eres el 'Codex Intelligence System'. Un asistente de IA de élite.
    Usuario: Diego Armando Cuenca Lavana.
    Especialidad: Norma CXS 96-1981 (Jamón Curado Cocido) y seguridad alimentaria.
    Responde en español de forma técnica y elegante.
    Tu objetivo es ayudar con dudas sobre procesos, ingredientes y normatividad cárnica."""

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

    backoff_times = [1, 2, 4, 8, 16]
    for i in range(5):
        try:
            if not api_key:
                return "⚠️ Configuración requerida: Por favor, agrega la GEMINI_API_KEY en los 'Secrets' de Streamlit para activar el asistente."
            
            response = requests.post(url, json=payload, timeout=20)
            if response.status_code == 200:
                result = response.json()
                return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Sin respuesta disponible.")
            elif response.status_code == 429:
                time.sleep(backoff_times[i])
                continue
        except Exception:
            time.sleep(backoff_times[i])
    
    return "El sistema inteligente está procesando muchas solicitudes. Intente en un momento."

# --- SISTEMA DE DISEÑO ULTRA-LIMPIO Y RESPONSIVO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Fondo base */
    .stApp { background-color: #020617; }

    /* --- LIMPIEZA DE INTERFAZ (OCULTAR TEXTOS DE SISTEMA Y BOTONES) --- */
    header, footer, [data-testid="stHeader"], [data-testid="stToolbar"], 
    [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"],
    button[title="Collapse sidebar"], button[title="Expand sidebar"],
    .st-emotion-cache-6qob1r, .st-emotion-cache-1647ite, .st-emotion-cache-ch5vun {
        display: none !important;
        visibility: hidden !important;
    }

    /* Quitar padding de Streamlit */
    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* --- RESPONSIVIDAD --- */
    @media (max-width: 768px) {
        .main-title, .accent-title { font-size: 3rem !important; }
        .custom-card { padding: 25px !important; }
        [data-testid="stSidebar"] { width: 100% !important; }
    }

    /* Centrado Portada */
    .stApp:has(.splash-marker) [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
        text-align: center;
    }

    /* Tipografías */
    h1, h2, h3, .serif-text { font-family: 'Playfair Display', serif !important; color: #f8fafc; margin: 0 !important; }
    p, span, div, .sans-text { font-family: 'Inter', sans-serif !important; color: #94a3b8; }

    /* --- DISEÑO CHATBOT (SIDEBAR FIX) --- */
    [data-testid="stSidebar"] {
        background-color: #050a18 !important;
        border-right: 1px solid rgba(59, 130, 246, 0.15);
    }

    .chat-bubble-user {
        background: rgba(37, 99, 235, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.3);
        padding: 15px; border-radius: 20px 20px 5px 20px;
        color: #f1f5f9; margin-bottom: 20px; font-size: 0.85rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .chat-bubble-bot {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 15px; border-radius: 20px 20px 20px 5px;
        color: #cbd5e1; margin-bottom: 20px; font-size: 0.85rem; line-height: 1.6;
    }

    /* Portada */
    .main-title { font-size: 6.5rem; font-weight: 800; letter-spacing: -6px; line-height: 0.8; background: linear-gradient(to bottom, #ffffff, #64748b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .accent-title { font-size: 6.5rem; font-weight: 700; letter-spacing: -6px; line-height: 0.8; color: #3b82f6; font-style: italic; }
    .glow-icon { font-size: 5rem; margin-bottom: 30px; filter: drop-shadow(0 0 30px rgba(59, 130, 246, 0.5)); }

    /* Tarjetas */
    .card-link { text-decoration: none !important; display: block; margin-bottom: 25px; }
    .custom-card {
        background: #ffffff; padding: 45px; border-radius: 45px;
        transition: all 0.5s ease; text-align: left;
    }
    .custom-card:hover { transform: translateY(-10px); box-shadow: 0 30px 60px rgba(0,0,0,0.3); border: 1px solid #3b82f6; }
    .doc-code { background: #eff6ff; color: #2563eb; font-weight: 800; font-size: 0.7rem; padding: 5px 12px; border-radius: 8px; margin-bottom: 12px; display: inline-block; }
    .doc-title { color: #0f172a; font-size: 1.8rem; font-weight: 900; }

    /* Botones */
    div.stButton > button {
        border-radius: 20px !important; background: #ffffff !important; color: #020617 !important; padding: 15px 50px !important;
        font-weight: 800 !important; border: none !important; letter-spacing: 4px; box-shadow: 0 15px 30px rgba(0,0,0,0.4) !important;
        margin-top: 30px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: ASISTENTE IA ---
with st.sidebar:
    st.markdown("<h2 class='serif-text' style='font-size: 2rem; margin-top: 10px !important;'>Codex AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.75rem; opacity: 0.4; letter-spacing: 2px;'>INTELIGENCIA NORMATIVA</p>", unsafe_allow_html=True)
    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar historial
    for m in st.session_state.messages:
        if m["role"] == "user":
            st.markdown(f'<div class="chat-bubble-user">{m["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-bot"><span style="color:#3b82f6;font-weight:800;font-size:0.6rem;display:block;margin-bottom:5px;letter-spacing:1px;">SISTEMA</span>{m["content"]}</div>', unsafe_allow_html=True)

    # Input
    if prompt := st.chat_input("Consulta la IA..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

    # Respuesta
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with st.spinner("Analizando protocolos..."):
            ans = call_gemini_api(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": ans})
            st.rerun()

# --- VISTAS ---
if 'view' not in st.session_state:
    st.session_state.view = 'splash'

if st.session_state.view == 'splash':
    st.markdown('<div class="splash-marker"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-icon">📜</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">MANUAL DE</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="accent-title">NORMATIVIDAD</h1>', unsafe_allow_html=True)
    st.markdown('<p style="letter-spacing: 15px; margin-top: 30px; opacity: 0.3; color: white;">CODEX ALIMENTARIUS</p>', unsafe_allow_html=True)
    if st.button("INGRESAR"):
        st.session_state.view = 'selection'
        st.rerun()

elif st.session_state.view == 'selection':
    st.markdown("<h1 style='text-align: center; font-size: 4rem; letter-spacing: -3px;'>Selección Técnica</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="custom-card" style="text-align: center;">
                <div style="font-size: 5rem; margin-bottom: 20px;">🍖</div>
                <h3 class="doc-title">JAMÓN CURADO COCIDO</h3>
                <div class="doc-code">CXS 96-1981</div>
                <p style="color: #64748b; font-size: 1rem; font-style: italic;">Estándar de identidad y seguridad técnica.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ABRIR EXPEDIENTE"):
            st.session_state.view = 'manual'
            st.rerun()

elif st.session_state.view == 'manual':
    st.markdown("<style>.stApp { background-color: #fcfdfe; }</style>", unsafe_allow_html=True)
    if st.button("← VOLVER"):
        st.session_state.view = 'selection'
        st.rerun()
    st.markdown("<h1 style='color: #0f172a; font-size: 3.5rem; font-weight: 900;'>Documentación Oficial</h1>", unsafe_allow_html=True)
    
    # Ejemplo de sección
    st.markdown("<div style='margin-top:40px; border-left: 5px solid #3b82f6; padding-left: 20px; font-weight: 800;'>I. PRÁCTICAS (CXC)</div>", unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        st.markdown('<a href="https://www.fao.org/4/a1552s/a1552s00.pdf" target="_blank" class="card-link"><div class="custom-card"><div class="doc-code">CXC 1-1969</div><div class="doc-title" style="font-size:1.3rem;">Higiene / Principios</div></div></a>', unsafe_allow_html=True)
    with cols[1]:
        st.markdown('<a href="https://www.fao.org/3/y1579s/y1579s02.pdf" target="_blank" class="card-link"><div class="custom-card"><div class="doc-code">CXC 23-1979</div><div class="doc-title" style="font-size:1.3rem;">Pocos Ácidos</div></div></a>', unsafe_allow_html=True)
