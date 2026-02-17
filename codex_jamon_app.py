import streamlit as st
import requests
import time

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="Codex AI - Sistema Inteligente",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LÓGICA DO CHATBOT CON IA (GEMINI API) ---
def call_gemini_api(messages):
    const_api_key = ""  # A chave é fornecida automaticamente pelo ambiente
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={const_api_key}"
    
    system_prompt = """Eres el 'Codex Intelligence System'. Un asistente de IA de nivel élite especializado en el Codex Alimentarius.
    Tu usuario es Diego Armando Cuenca Lavana.
    Tu conocimiento se centra en la Norma CXS 96-1981 y todas las directrices de higiene y aditivos relacionadas.
    Responde de forma técnica, elegante y sumamente profesional. 
    Si te preguntan por recomendaciones de procesos para el jamón, básate estrictamente en las normas del Codex."""

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

    # Exponential Backoff para robustez (1s, 2s, 4s, 8s, 16s)
    backoff_times = [1, 2, 4, 8, 16]
    for i in range(5):
        try:
            response = requests.post(url, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Error en el procesamiento de datos.")
        except Exception:
            pass
        time.sleep(backoff_times[i])
    return "El sistema está saturado. Por favor, intente de nuevo."

# --- SISTEMA DE DISEÑO AVANZADO (CSS CUSTOMIZADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Configuração Global */
    .stApp { background-color: #020617; }
    
    /* REMOVER BOTÕES DE MINIMIZAR E TEXTOS DO SISTEMA (keyboard_double, etc) */
    [data-testid="collapsedControl"], 
    button[title="Collapse sidebar"], 
    .st-emotion-cache-6qob1r,
    .st-emotion-cache-1647ite {
        display: none !important;
    }
    
    /* Centrado da Portada */
    .stApp:has(.splash-marker) [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
        text-align: center;
    }

    /* Tipografia */
    h1, h2, h3, .serif-text {
        font-family: 'Playfair Display', serif !important;
        color: #f8fafc;
        margin: 0 !important;
    }
    p, span, div, .sans-text {
        font-family: 'Inter', sans-serif !important;
        color: #94a3b8;
    }

    /* --- DISEÑO DEL CHATBOT (SIDEBAR) --- */
    [data-testid="stSidebar"] {
        background-color: #0b1120 !important;
        border-right: 1px solid rgba(59, 130, 246, 0.2);
    }
    
    /* Burbujas de Chat Personalizadas */
    .chat-bubble-user {
        background: rgba(59, 130, 246, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.3);
        padding: 15px;
        border-radius: 20px 20px 0px 20px;
        color: #e2e8f0;
        margin-bottom: 20px;
        font-size: 0.9rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .chat-bubble-bot {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 20px 20px 20px 0px;
        color: #cbd5e1;
        margin-bottom: 20px;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    .bot-name {
        color: #3b82f6;
        font-weight: 800;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 8px;
        display: block;
    }

    /* --- PORTADA ULTRA-PREMIUM --- */
    .main-title {
        font-size: 6.5rem; font-weight: 800; letter-spacing: -5px; line-height: 0.8;
        background: linear-gradient(to bottom, #ffffff, #64748b);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .accent-title {
        font-size: 6.5rem; font-weight: 700; letter-spacing: -5px; line-height: 0.8;
        color: #3b82f6; font-style: italic;
    }
    .glow-icon {
        font-size: 4.5rem; margin-bottom: 30px;
        filter: drop-shadow(0 0 25px rgba(59, 130, 246, 0.7));
    }

    /* --- TARJETAS TÉCNICAS (CLICKABLES) --- */
    .card-link { text-decoration: none !important; display: block; margin-bottom: 20px; }
    
    .custom-card {
        background: #ffffff;
        padding: 45px;
        border-radius: 40px;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
        text-align: left;
    }
    .custom-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 40px 80px rgba(0,0,0,0.4);
        border-color: #3b82f6;
    }
    .doc-code {
        background: #eff6ff; color: #2563eb; font-weight: 800; font-size: 0.75rem;
        padding: 6px 14px; border-radius: 12px; letter-spacing: 2px;
        display: inline-block; margin-bottom: 15px;
    }
    .doc-title { color: #0f172a; font-size: 1.8rem; font-weight: 900; letter-spacing: -1px; }

    /* Botões Customizados */
    div.stButton > button {
        border-radius: 20px !important; background: #ffffff !important;
        color: #020617 !important; padding: 20px 60px !important;
        font-weight: 800 !important; border: none !important;
        letter-spacing: 5px; box-shadow: 0 20px 40px rgba(0,0,0,0.4) !important;
        margin-top: 40px !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        background: #3b82f6 !important; color: #ffffff !important; transform: translateY(-5px) scale(1.05) !important;
    }

    .cat-divider {
        margin: 80px 0 40px 0; padding-left: 25px;
        border-left: 5px solid #3b82f6; letter-spacing: 10px;
        font-weight: 800; color: white; text-transform: uppercase;
        background: rgba(255,255,255,0.02); padding: 15px 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CHATBOT INTEGRADO NO SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 class='serif-text' style='font-size: 2.2rem;'>Codex AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.85rem; opacity: 0.5;'>Sistema de Inteligência Normativa</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibição de mensagens com estilo boutique
    chat_placeholder = st.container()
    with chat_placeholder:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""<div class="chat-bubble-user">{message["content"]}</div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="chat-bubble-bot">
                        <span class="bot-name">Codex Intelligence</span>
                        {message["content"]}
                    </div>
                """, unsafe_allow_html=True)

    # Input sem botões de minimizar por perto
    if prompt := st.chat_input("Consulte con la IA..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

    # Resposta da IA
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with st.spinner("Sincronizando con base de datos..."):
            response = call_gemini_api(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# --- LÓGICA DE NAVEGAÇÃO ---
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
            <p style='letter-spacing: 12px; margin-top: 40px; opacity: 0.4; color: white; font-size: 1.1rem; font-weight: 300;'>CODEX ALIMENTARIUS</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("INGRESAR AL SISTEMA"):
        st.session_state.view = 'selection'
        st.rerun()
    
    st.markdown("<br><br><p style='color: #475569; font-size: 0.8rem; letter-spacing: 10px; font-weight: 600;'>DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. SELECCIÓN ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4.5rem; letter-spacing: -3px;'>Selección de Producto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.3rem; margin-bottom: 70px;'>Escoja el estándar técnico que desea inspeccionar.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="custom-card" style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8fafc);">
                <div style="font-size: 6rem; margin-bottom: 30px;">🍖</div>
                <h3 style="font-size: 3rem; color: #0f172a; margin-bottom: 10px; font-weight: 900; letter-spacing: -2px;">JAMÓN CURADO COCIDO</h3>
                <div class="doc-code" style="font-size: 1rem; padding: 8px 20px;">CXS 96-1981</div>
                <p style="color: #64748b; font-size: 1.2rem; margin-top: 30px; font-style: italic; font-weight: 400; line-height: 1.8;">
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
    
    st.markdown("<h1 style='color: #0f172a; font-size: 4rem; letter-spacing: -3px; font-weight: 900;'>Documentación Técnica</h1>", unsafe_allow_html=True)
    
    manual_data = {
        "I. PRÁCTICAS (CXC)": [
            ("Higiene / Principios", "CXC 1-1969", "Protocolos básicos de higiene para toda la cadena de suministro alimentario.", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
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
            ("Etiquetado / No Minorista", "CXS 346-2021", "Requisitos informativos para distribución industrial y comercio b2b.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B346-2021%252FCXS_346s.pdf"),
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
                        <div class="custom-card">
                            <div class="doc-code">{codigo}</div>
                            <div class="doc-title">{nombre}</div>
                            <p style="color: #64748b; font-size: 1rem; margin-top: 15px; font-style: italic; line-height: 1.6;">{desc}</p>
                        </div>
                    </a>
                """, unsafe_allow_html=True)

    st.markdown("<br><br><p style='text-align: center; color: #cbd5e1; font-size: 0.9rem; letter-spacing: 6px; font-weight: 700;'>CODEX ALIMENTARIUS • GASTRONOMÍA • 2026</p>", unsafe_allow_html=True)
