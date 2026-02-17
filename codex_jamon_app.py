import streamlit as st
import requests
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Codex AI - Sistema Normativo",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LÓGICA DEL CHATBOT CON IA (GEMINI API) ---
def call_gemini_api(messages):
    const_api_key = ""  # La clave se proporciona automáticamente
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={const_api_key}"
    
    system_prompt = """Eres un Asistente Experto en el Codex Alimentarius. Tu especialidad es la seguridad alimentaria y el Jamón Curado Cocido (CXS 96-1981).
    Diego Armando Cuenca Lavana es el usuario principal. Responde dudas sobre:
    - Procesos de curado y cocción.
    - Normas de higiene (CXC 1-1969, CXC 58-2005).
    - Aditivos y Etiquetado.
    Da respuestas técnicas pero directas y profesionales."""

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

    # Exponential Backoff
    backoff_times = [1, 2, 4, 8, 16]
    for i in range(5):
        try:
            response = requests.post(url, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Error procesando.")
        except Exception:
            pass
        time.sleep(backoff_times[i])
    return "Error de conexión con la IA."

# --- SISTEMA DE DISEÑO AVANZADO (CSS ULTRA-PREMIUM) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Variables de Estilo */
    :root {
        --bg: #020617;
        --accent: #3b82f6;
    }

    .stApp { background-color: var(--bg); }

    /* Centrado Maestro de la Portada */
    .stApp:has(.splash-marker) [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
        text-align: center;
    }

    /* Tipografía Premium */
    h1, h2, h3, .serif-text {
        font-family: 'Playfair Display', serif !important;
        color: #f8fafc;
        margin: 0 !important;
    }
    
    p, span, div, .sans-text {
        font-family: 'Inter', sans-serif !important;
        color: #94a3b8;
    }

    /* Estilo del Hero (Portada) */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
    }

    .main-title {
        font-size: 6.5rem;
        font-weight: 800;
        letter-spacing: -5px;
        line-height: 0.8;
        background: linear-gradient(to bottom, #ffffff, #64748b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .accent-title {
        font-size: 6.5rem;
        font-weight: 700;
        letter-spacing: -5px;
        line-height: 0.8;
        color: var(--accent);
        font-style: italic;
    }

    .glow-icon {
        font-size: 3rem;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 15px rgba(59, 130, 246, 0.4));
    }

    /* Tarjetas Interactivas (Sin Fotos) */
    .card-link { text-decoration: none !important; display: block; margin-bottom: 20px; }
    
    .custom-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 40px;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
        text-align: left;
    }

    .custom-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 40px 80px rgba(0,0,0,0.3);
        border-color: var(--accent);
    }

    .doc-code {
        background: #eff6ff;
        color: #2563eb;
        font-weight: 800;
        font-size: 0.75rem;
        padding: 6px 14px;
        border-radius: 12px;
        letter-spacing: 2px;
        display: inline-block;
        margin-bottom: 15px;
    }

    .doc-title {
        color: #0f172a;
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: -1px;
    }

    /* Botones Premium */
    div.stButton > button {
        border-radius: 20px !important;
        background: #ffffff !important;
        color: #020617 !important;
        padding: 18px 60px !important;
        font-weight: 800 !important;
        border: none !important;
        letter-spacing: 5px;
        font-size: 0.9rem !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4) !important;
        margin-top: 40px !important;
    }

    div.stButton > button:hover {
        background: var(--accent) !important;
        color: #ffffff !important;
        transform: translateY(-5px) !important;
    }

    /* Sidebar Chat */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    .stChatMessage {
        border-radius: 20px !important;
        background: rgba(255,255,255,0.03) !important;
    }

    .cat-divider {
        margin: 80px 0 40px 0;
        padding-left: 20px;
        border-left: 3px solid var(--accent);
        letter-spacing: 6px;
        font-weight: 800;
        color: white;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CHATBOT EN EL SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 class='serif-text'>Codex AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem;'>Asistente inteligente para normas alimentarias.</p>", unsafe_allow_html=True)
    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Pregunta sobre normatividad..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analizando Codex..."):
                response = call_gemini_api(st.session_state.messages)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# --- NAVEGACIÓN ---
if 'view' not in st.session_state:
    st.session_state.view = 'splash'

# --- 1. PORTADA CENTRADA ---
if st.session_state.view == 'splash':
    st.markdown('<div class="splash-marker"></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-container">
            <div class="glow-icon">📜</div>
            <h1 class="main-title">MANUAL DE</h1>
            <h1 class="accent-title">NORMATIVIDAD</h1>
            <p style='letter-spacing: 12px; margin-top: 30px; opacity: 0.5; color: white; font-size: 0.9rem;'>CODEX ALIMENTARIUS</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("INGRESAR AL SISTEMA"):
        st.session_state.view = 'selection'
        st.rerun()
    
    st.markdown("<br><br><p style='color: #475569; font-size: 0.7rem; letter-spacing: 8px;'>DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. SELECCIÓN ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4rem; letter-spacing: -3px;'>Selección de Producto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.2rem; margin-bottom: 60px;'>Escoja el estándar técnico que desea inspeccionar.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="custom-card" style="text-align: center; background: linear-gradient(135deg, #ffffff, #f1f5f9);">
                <div style="font-size: 5rem; margin-bottom: 20px;">🍖</div>
                <h3 style="font-size: 2.5rem; color: #0f172a; margin-bottom: 10px; font-weight: 900;">JAMÓN CURADO COCIDO</h3>
                <div class="doc-code">CXS 96-1981</div>
                <p style="color: #64748b; font-size: 1.1rem; margin-top: 20px; font-style: italic;">
                    Estándar internacional de identidad, calidad y seguridad alimentaria.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ABRIR DOCUMENTACIÓN"):
            st.session_state.view = 'manual'
            st.rerun()

# --- 3. MANUAL (TARJETAS CLICKABLES) ---
elif st.session_state.view == 'manual':
    st.markdown("<style>.stApp { background-color: #fcfdfe; }</style>", unsafe_allow_html=True)
    
    col_back, _ = st.columns([1, 8])
    with col_back:
        if st.button("← VOLVER"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<h1 style='color: #0f172a; font-size: 3.5rem; letter-spacing: -3px;'>Documentación Técnica</h1>", unsafe_allow_html=True)
    
    # Contenido del Manual
    manual_data = {
        "I. PRÁCTICAS (CXC)": [
            ("Higiene / Principios", "CXC 1-1969", "Protocolos básicos de higiene para la cadena de suministro.", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
            ("Higiene / Carne", "CXC 58-2005", "Directrices sanitarias rigurosas para la manipulación de carne.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXC%B58-2005%252FCXC_058s.pdf"),
            ("Higiene / Pocos Ácidos", "CXC 23-1979", "Seguridad en procesos térmicos y envasado hermético.", "https://www.fao.org/3/y1579s/y1579s02.pdf"),
        ],
        "II. DIRECTRICES (CXG)": [
            ("Aditivos / Aromatizantes", "CXG 66-2008", "Control de sustancias saporíferas y condensados de humo.", "https://www.fao.org/input/download/standards/11020/cxg_066s.pdf"),
            ("Higiene / Microbiano", "CXG 21-1997", "Parámetros biológicos para garantizar la inocuidad.", "https://www.fao.org/4/y5307s/y5307s04.htm"),
        ],
        "III. GENERALES (CXS)": [
            ("Aditivos Alimentarios", "CXS 192-1995", "Regulación internacional sobre aditivos y límites máximos.", "https://www.fao.org/gsfaonline/docs/CXS_192s.pdf"),
            ("Contaminantes / Toxinas", "CXS 193-1995", "Vigilancia de metales pesados, radionucleidos y toxinas.", "https://www.fao.org/fileadmin/user_upload/livestockgov/documents/CXS_193s.pdf"),
            ("Etiquetado / Envasados", "CXS 1-1985", "Transparencia informativa y declaración de ingredientes.", "https://www.fao.org/4/y2770s/y2770s02.htm"),
            ("Análisis y Muestreo", "CXS 234-1999", "Metodologías de laboratorio para verificación de cumplimiento.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B234-1999%252FCXS_234s.pdf"),
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
                            <p style="color: #64748b; font-size: 0.9rem; margin-top: 15px; font-style: italic;">{desc}</p>
                        </div>
                    </a>
                """, unsafe_allow_html=True)

    st.markdown("<br><br><p style='text-align: center; color: #cbd5e1; font-size: 0.8rem; letter-spacing: 5px; font-weight: 700;'>CODEX ALIMENTARIUS • GASTRONOMÍA • 2026</p>", unsafe_allow_html=True)
