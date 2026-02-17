import streamlit as st
import requests
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Codex Intelligence System",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LÓGICA DEL CHATBOT CON IA (GEMINI API) ---
def call_gemini_api(messages):
    # La clave se maneja internamente en el entorno
    api_key = st.secrets.get("GEMINI_API_KEY", "")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={api_key}"
    
    system_prompt = """Eres el 'Codex Intelligence System'. Un asistente de IA de élite.
    Tu usuario es Diego Armando Cuenca Lavana.
    Especialidad absoluta: Normas del Codex Alimentarius, específicamente CXS 96-1981 (Jamón Curado Cocido).
    Responde en español de forma técnica, elegante y ejecutiva. 
    Si no hay una API Key configurada, informa al usuario que debe configurarla en los secretos de Streamlit."""

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

    # Exponential Backoff mejorado (1s, 2s, 4s, 8s, 16s)
    backoff_times = [1, 2, 4, 8, 16]
    for i in range(5):
        try:
            if not api_key:
                return "Configuración requerida: Por favor, agrega tu GEMINI_API_KEY en los 'Secrets' de Streamlit para activar la IA."
            
            response = requests.post(url, json=payload, timeout=20)
            if response.status_code == 200:
                result = response.json()
                return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Sin respuesta.")
            elif response.status_code == 429:
                time.sleep(backoff_times[i])
                continue
        except Exception:
            time.sleep(backoff_times[i])
    
    return "El sistema está experimentando una carga inusual. Por favor, intente en 30 segundos."

# --- SISTEMA DE DISEÑO AVANZADO (CSS ULTRA-LIMPIO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    .stApp { background-color: #020617; }
    
    /* --- ELIMINAR BASURA VISUAL Y BOTONES DE SISTEMA --- */
    /* Ocultar botón de cerrar/colapsar sidebar */
    [data-testid="stSidebarCollapseButton"], 
    button[title="Collapse sidebar"],
    button[title="Expand sidebar"],
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* Ocultar textos de accesibilidad tipo 'keyboard_double_arrow' */
    .st-emotion-cache-6qob1r, 
    .st-emotion-cache-1647ite,
    .st-emotion-cache-ch5vun,
    [data-testid="stHeader"]::before {
        display: none !important;
        content: "" !important;
    }

    /* Quitar padding extra del header que deja espacio en blanco */
    header[data-testid="stHeader"] {
        background: transparent !important;
        color: transparent !important;
    }

    /* Centrado Maestro de la Portada */
    .stApp:has(.splash-marker) [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
        text-align: center;
    }

    /* Tipografías */
    h1, h2, h3, .serif-text {
        font-family: 'Playfair Display', serif !important;
        color: #f8fafc;
        margin: 0 !important;
    }
    p, span, div, .sans-text {
        font-family: 'Inter', sans-serif !important;
        color: #94a3b8;
    }

    /* --- DISEÑO DEL CHATBOT (SIDEBAR PREMIUM) --- */
    [data-testid="stSidebar"] {
        background-color: #050a18 !important;
        border-right: 1px solid rgba(59, 130, 246, 0.1);
        width: 380px !important;
    }

    .chat-bubble-user {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.25), rgba(37, 99, 235, 0.1));
        border: 1px solid rgba(59, 130, 246, 0.4);
        padding: 20px;
        border-radius: 25px 25px 5px 25px;
        color: #f8fafc;
        margin-bottom: 25px;
        font-size: 0.9rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .chat-bubble-bot {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 25px 25px 25px 5px;
        color: #cbd5e1;
        margin-bottom: 25px;
        font-size: 0.9rem;
        line-height: 1.7;
    }

    .bot-tag {
        color: #3b82f6;
        font-weight: 800;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 12px;
        display: block;
    }

    /* --- PORTADA --- */
    .main-title {
        font-size: 7rem; font-weight: 800; letter-spacing: -7px; line-height: 0.8;
        background: linear-gradient(to bottom, #ffffff, #64748b);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .accent-title {
        font-size: 7rem; font-weight: 700; letter-spacing: -7px; line-height: 0.8;
        color: #3b82f6; font-style: italic;
    }
    .glow-icon {
        font-size: 5rem; margin-bottom: 40px;
        filter: drop-shadow(0 0 35px rgba(59, 130, 246, 0.7));
    }

    /* --- TARJETAS --- */
    .card-link { text-decoration: none !important; display: block; margin-bottom: 30px; }
    .custom-card {
        background: #ffffff;
        padding: 55px;
        border-radius: 50px;
        transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        text-align: left;
    }
    .custom-card:hover {
        transform: translateY(-25px) scale(1.03);
        box-shadow: 0 60px 120px rgba(0,0,0,0.5);
        border: 1px solid #3b82f6;
    }
    .doc-code {
        background: #eff6ff; color: #2563eb; font-weight: 800; font-size: 0.75rem;
        padding: 8px 18px; border-radius: 12px; letter-spacing: 3px;
        display: inline-block; margin-bottom: 25px;
    }
    .doc-title { color: #0f172a; font-size: 2.1rem; font-weight: 900; letter-spacing: -1.5px; }

    /* Botones */
    div.stButton > button {
        border-radius: 20px !important; background: #ffffff !important;
        color: #020617 !important; padding: 22px 80px !important;
        font-weight: 800 !important; border: none !important;
        letter-spacing: 7px; box-shadow: 0 40px 80px rgba(0,0,0,0.6) !important;
        margin-top: 60px !important;
    }
    div.stButton > button:hover {
        background: #3b82f6 !important; color: #ffffff !important; transform: scale(1.1) !important;
    }

    .cat-divider {
        margin: 120px 0 60px 0; padding: 25px 40px;
        border-left: 8px solid #3b82f6; letter-spacing: 15px;
        font-weight: 800; color: white; text-transform: uppercase;
        background: rgba(255,255,255,0.01);
    }
    </style>
    """, unsafe_allow_html=True)

# --- ASISTENTE IA INTEGRADO EN SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 class='serif-text' style='font-size: 2.8rem; margin-top: 30px !important;'>Codex AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; opacity: 0.3; letter-spacing: 2px;'>SYSTEM INTELLIGENCE</p>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    chat_display = st.container()
    with chat_display:
        for m in st.session_state.messages:
            if m["role"] == "user":
                st.markdown(f'<div class="chat-bubble-user">{m["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'''
                    <div class="chat-bubble-bot">
                        <span class="bot-tag">Intelligence System</span>
                        {m["content"]}
                    </div>
                ''', unsafe_allow_html=True)

    if prompt := st.chat_input("Consulte la normativa..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with st.spinner("Sincronizando protocolos..."):
            ans = call_gemini_api(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": ans})
            st.rerun()

# --- LÓGICA DE NAVEGACIÓN ---
if 'view' not in st.session_state:
    st.session_state.view = 'splash'

# --- 1. PORTADA ---
if st.session_state.view == 'splash':
    st.markdown('<div class="splash-marker"></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-container">
            <div class="glow-icon">📜</div>
            <h1 class="main-title">MANUAL DE</h1>
            <h1 class="accent-title">NORMATIVIDAD</h1>
            <p style='letter-spacing: 20px; margin-top: 50px; opacity: 0.3; color: white; font-size: 1.2rem; font-weight: 300;'>CODEX ALIMENTARIUS</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("INGRESAR"):
        st.session_state.view = 'selection'
        st.rerun()
    
    st.markdown("<br><br><br><p style='color: #1e293b; font-size: 0.75rem; letter-spacing: 15px; font-weight: 800;'>DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. SELECCIÓN ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 5.5rem; letter-spacing: -5px;'>Selección Técnica</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.5rem; margin-bottom: 100px; font-weight: 300;'>Identifique el protocolo internacional.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="custom-card" style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8fafc);">
                <div style="font-size: 8rem; margin-bottom: 50px;">🍖</div>
                <h3 style="font-size: 3.2rem; color: #0f172a; margin-bottom: 15px; font-weight: 900; letter-spacing: -2px;">JAMÓN CURADO COCIDO</h3>
                <div class="doc-code" style="font-size: 1.2rem; padding: 12px 30px;">CXS 96-1981</div>
                <p style="color: #64748b; font-size: 1.3rem; margin-top: 40px; font-style: italic; line-height: 1.8;">
                    Normativa integral de identidad y seguridad técnica para productos cárnicos curados procesados térmicamente.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ABRIR EXPEDIENTE"):
            st.session_state.view = 'manual'
            st.rerun()

# --- 3. MANUAL ---
elif st.session_state.view == 'manual':
    st.markdown("<style>.stApp { background-color: #fcfdfe; }</style>", unsafe_allow_html=True)
    
    col_back, _ = st.columns([1, 8])
    with col_back:
        if st.button("← VOLVER"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<h1 style='color: #0f172a; font-size: 5rem; letter-spacing: -5px; font-weight: 900;'>Documentación Oficial</h1>", unsafe_allow_html=True)
    
    manual_data = {
        "I. PRÁCTICAS (CXC)": [
            ("Higiene / Principios", "CXC 1-1969", "Protocolos básicos de higiene para la cadena de suministro alimentario.", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
            ("Higiene / Carne", "CXC 58-2005", "Directrices sanitarias rigurosas específicas para la manipulación de carne.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXC%B58-2005%252FCXC_058s.pdf"),
            ("Higiene / Pocos Ácidos", "CXC 23-1979", "Seguridad en procesos térmicos y envasado hermético de baja acidez.", "https://www.fao.org/3/y1579s/y1579s02.pdf"),
        ],
        "II. DIRECTRICES (CXG)": [
            ("Aditivos / Aromatizantes", "CXG 66-2008", "Control de sustancias saporíferas y condensados de humo en el producto.", "https://www.fao.org/input/download/standards/11020/cxg_066s.pdf"),
            ("Higiene / Microbiano", "CXG 21-1997", "Parámetros biológicos para garantizar la inocuidad y vida útil comercial.", "https://www.fao.org/4/y5307s/y5307s04.htm"),
        ],
        "III. GENERALES (CXS)": [
            ("Aditivos Alimentarios", "CXS 192-1995", "Regulación internacional sobre aditivos y sus límites máximos permitidos.", "https://www.fao.org/gsfaonline/docs/CXS_192s.pdf"),
            ("Contaminantes / Toxinas", "CXS 193-1995", "Vigilancia de metales pesados, radionucleidos y toxinas químicas.", "https://www.fao.org/fileadmin/user_upload/livestockgov/documents/CXS_193s.pdf"),
            ("Etiquetado / Envasados", "CXS 1-1985", "Transparencia informativa y declaración de ingredientes obligatoria.", "https://www.fao.org/4/y2770s/y2770s02.htm"),
            ("Análisis y Muestreo", "CXS 234-1999", "Metodologías de laboratorio para la verificación de cumplimiento técnico.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B234-1999%252FCXS_234s.pdf"),
        ]
    }

    for categoria, items in manual_data.items():
        st.markdown(f"<div class='cat-divider'>{categoria}</div>", unsafe_allow_html=True)
        cols = st.columns(2)
        for i, (nombre, codigo, desc, url) in enumerate(items):
            with cols[i % 2]:
                st.markdown(f"""
                    <a href="{url}" target="_blank" class="card-link">
                        <div class="custom-card" style="padding: 50px; border: 1px solid #f1f5f9; box-shadow: 0 15px 35px rgba(0,0,0,0.03);">
                            <div class="doc-code">{codigo}</div>
                            <div class="doc-title">{nombre}</div>
                            <p style="color: #64748b; font-size: 1.1rem; margin-top: 25px; font-style: italic; line-height: 1.7;">{desc}</p>
                        </div>
                    </a>
                """, unsafe_allow_html=True)

    st.markdown("<br><br><p style='text-align: center; color: #cbd5e1; font-size: 1.1rem; letter-spacing: 10px; font-weight: 800;'>CODEX ALIMENTARIUS • GASTRONOMÍA • 2026</p>", unsafe_allow_html=True)
