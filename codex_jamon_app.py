import streamlit as st
import requests
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Codex Intelligence - Diego Cuenca",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- LÓGICA DEL CHATBOT CON IA (GEMINI API) ---
def call_gemini_api(messages):
    api_key = st.secrets.get("GEMINI_API_KEY", "")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={api_key}"
    
    system_prompt = """Eres el 'Codex Intelligence System'. Un asistente de IA de élite.
    Usuario: Diego Armando Cuenca Lavana.
    Especialidad: Normas del Codex Alimentarius, específicamente:
    1. CXS 96-1981 (Jamón Curado Cocido)
    2. CXS 12-1981 (Norma para la Miel)
    Responde en español de forma técnica, elegante y profesional. 
    Ayuda con dudas sobre procesos, higiene, etiquetado y normatividad cárnica y apícola."""

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
                return "⚠️ Configuración requerida: Agregue su API Key en los Secrets de Streamlit."
            response = requests.post(url, json=payload, timeout=20)
            if response.status_code == 200:
                result = response.json()
                return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Sin respuesta.")
            elif response.status_code == 429:
                time.sleep(backoff_times[i])
                continue
        except Exception:
            time.sleep(backoff_times[i])
    return "El sistema está saturado. Por favor, intente en un momento."

# --- SISTEMA DE DISEÑO ULTRA-PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Fondo base oscuro */
    .stApp { background-color: #020617; }

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

    /* --- DISEÑO DEL CHATBOT (SIDEBAR) --- */
    [data-testid="stSidebar"] {
        background-color: #050a18 !important;
        border-right: 1px solid rgba(59, 130, 246, 0.1);
    }

    .chat-bubble-user {
        background: rgba(37, 99, 235, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.3);
        padding: 15px; border-radius: 20px 20px 5px 20px;
        color: #f1f5f9; margin-bottom: 20px; font-size: 0.85rem;
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

    /* Tarjetas Clickables */
    .card-link { text-decoration: none !important; display: block; margin-bottom: 25px; }
    .custom-card {
        background: #ffffff; padding: 45px; border-radius: 45px;
        transition: all 0.5s ease; text-align: left; height: 100%;
    }
    .custom-card:hover { transform: translateY(-10px); box-shadow: 0 30px 60px rgba(0,0,0,0.3); border: 1px solid #3b82f6; }
    .doc-code { background: #eff6ff; color: #2563eb; font-weight: 800; font-size: 0.7rem; padding: 5px 12px; border-radius: 8px; margin-bottom: 15px; display: inline-block; }
    .doc-title { color: #0f172a; font-size: 1.8rem; font-weight: 900; letter-spacing: -1px; }

    /* Botones */
    div.stButton > button {
        border-radius: 20px !important; background: #ffffff !important; color: #020617 !important; padding: 20px 40px !important;
        font-weight: 800 !important; border: none !important; letter-spacing: 5px; box-shadow: 0 15px 30px rgba(0,0,0,0.4) !important;
        margin-top: 20px !important; width: 100%;
    }
    
    /* Divisores de Categoría */
    .cat-divider { margin: 80px 0 40px 0; padding: 15px 25px; border-left: 5px solid #3b82f6; letter-spacing: 10px; font-weight: 800; color: white; text-transform: uppercase; background: rgba(255,255,255,0.01); }
    </style>
    """, unsafe_allow_html=True)

# --- ASISTENTE IA EN SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 class='serif-text' style='font-size: 2.2rem; margin-top: 10px !important;'>Codex AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.75rem; opacity: 0.4; letter-spacing: 2px;'>SISTEMA INTELIGENTE</p>", unsafe_allow_html=True)
    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for m in st.session_state.messages:
        if m["role"] == "user":
            st.markdown(f'<div class="chat-bubble-user">{m["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-bot"><span style="color:#3b82f6;font-weight:800;font-size:0.6rem;display:block;margin-bottom:5px;letter-spacing:1px;">SISTEMA</span>{m["content"]}</div>', unsafe_allow_html=True)

    if prompt := st.chat_input("Consulta con la IA..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with st.spinner("Analizando protocolos..."):
            ans = call_gemini_api(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": ans})
            st.rerun()

# --- LÓGICA DE NAVEGACIÓN Y DATOS ---
if 'view' not in st.session_state:
    st.session_state.view = 'splash'
if 'product' not in st.session_state:
    st.session_state.product = None

# Base de datos de productos
productos = {
    "jamon": {
        "nombre": "JAMÓN CURADO COCIDO",
        "codigo": "CXS 96-1981",
        "emoji": "🍖",
        "desc": "Normativa de identidad y seguridad técnica para productos cárnicos curados procesados.",
        "url_base": "https://www.fao.org/gsfaonline/docs/CXS_096s.pdf",
        "manual": {
            "I. PRÁCTICAS (CXC)": [
                ("Higiene / Principios", "CXC 1-1969", "Protocolos básicos de higiene alimentaria.", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
                ("Higiene / Carne", "CXC 58-2005", "Directrices sanitarias para la carne.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXC%B58-2005%252FCXC_058s.pdf"),
                ("Higiene / Pocos Ácidos", "CXC 23-1979", "Seguridad en procesos térmicos.", "https://www.fao.org/3/y1579s/y1579s02.pdf"),
            ],
            "II. DIRECTRICES (CXG)": [
                ("Aditivos / Aromatizantes", "CXG 66-2008", "Control de aromatizantes y humos.", "https://www.fao.org/input/download/standards/11020/cxg_066s.pdf"),
                ("Higiene / Microbiano", "CXG 21-1997", "Parámetros biológicos de inocuidad.", "https://www.fao.org/4/y5307s/y5307s04.htm"),
            ],
            "III. GENERALES (CXS)": [
                ("Aditivos Alimentarios", "CXS 192-1995", "Regulación internacional sobre aditivos.", "https://www.fao.org/gsfaonline/docs/CXS_192s.pdf"),
                ("Etiquetado / Envasados", "CXS 1-1985", "Declaración de ingredientes obligatoria.", "https://www.fao.org/4/y2770s/y2770s02.htm"),
            ]
        }
    },
    "miel": {
        "nombre": "NORMA PARA LA MIEL",
        "codigo": "CXS 12-1981",
        "emoji": "🍯",
        "desc": "Estándar internacional sobre la identidad, calidad y pureza de la miel de abejas.",
        "url_base": "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%2B12-1981%252FCXS_012s.pdf",
        "manual": {
            "I. HIGIENE": [
                ("Principios de Higiene", "CXC 1-1969", "Principios generales de higiene de los alimentos.", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
                ("Criterios Microbiológicos", "CXG 21-1997", "Establecimiento y aplicación de criterios microbiológicos.", "https://www.fao.org/4/y5307s/y5307s04.htm"),
            ],
            "II. ETIQUETADO": [
                ("Etiquetado General", "CXS 1-1985", "Norma para el etiquetado de alimentos preenvasados.", "https://www.fao.org/4/y2770s/y2770s02.htm"),
            ]
        }
    }
}

# --- 1. VISTA: PORTADA ---
if st.session_state.view == 'splash':
    st.markdown('<div class="splash-marker"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-icon">📜</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">MANUAL DE</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="accent-title">NORMATIVIDAD</h1>', unsafe_allow_html=True)
    st.markdown('<p style="letter-spacing: 15px; margin-top: 30px; opacity: 0.3; color: white;">CODEX ALIMENTARIUS</p>', unsafe_allow_html=True)
    if st.button("INGRESAR"):
        st.session_state.view = 'selection'
        st.rerun()
    st.markdown("<br><br><p style='color: #1e293b; font-size: 0.75rem; letter-spacing: 10px; font-weight: 800;'>DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. VISTA: SELECCIÓN ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4.5rem; letter-spacing: -3px;'>Selección Técnica</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.2rem; margin-bottom: 50px;'>Elija el producto para consultar su base normativa.</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div class="custom-card" style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8fafc);">
                <div style="font-size: 5rem; margin-bottom: 20px;">{productos['jamon']['emoji']}</div>
                <h3 class="doc-title">{productos['jamon']['nombre']}</h3>
                <div class="doc-code">{productos['jamon']['codigo']}</div>
                <p style="color: #64748b; font-size: 1rem; font-style: italic;">{productos['jamon']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ABRIR MANUAL JAMÓN", key="btn_jamon"):
            st.session_state.product = 'jamon'
            st.session_state.view = 'manual'
            st.rerun()

    with col2:
        st.markdown(f"""
            <div class="custom-card" style="text-align: center; background: linear-gradient(135deg, #ffffff, #fffbeb);">
                <div style="font-size: 5rem; margin-bottom: 20px;">{productos['miel']['emoji']}</div>
                <h3 class="doc-title">{productos['miel']['nombre']}</h3>
                <div class="doc-code" style="background:#fef3c7; color:#b45309;">{productos['miel']['codigo']}</div>
                <p style="color: #64748b; font-size: 1rem; font-style: italic;">{productos['miel']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ABRIR MANUAL MIEL", key="btn_miel"):
            st.session_state.product = 'miel'
            st.session_state.view = 'manual'
            st.rerun()

# --- 3. VISTA: MANUAL ---
elif st.session_state.view == 'manual':
    p = productos[st.session_state.product]
    st.markdown("<style>.stApp { background-color: #fcfdfe; }</style>", unsafe_allow_html=True)
    if st.button("← VOLVER A SELECCIÓN"):
        st.session_state.view = 'selection'
        st.rerun()
    
    st.markdown(f"<h1 style='color: #0f172a; font-size: 3.5rem; font-weight: 900; letter-spacing: -3px;'>Manual: {p['nombre']}</h1>", unsafe_allow_html=True)
    
    # Botón para abrir el Codex Base del producto seleccionado
    st.markdown(f"""
        <a href="{p['url_base']}" target="_blank" class="card-link">
            <div class="custom-card" style="background:#f8fafc; border: 2px dashed #3b82f6; padding: 25px; text-align:center;">
                <span style="color:#3b82f6; font-weight:800; letter-spacing:2px;">ABRIR CODEX OFICIAL {p['codigo']}</span>
            </div>
        </a>
    """, unsafe_allow_html=True)

    for categoria, items in p['manual'].items():
        st.markdown(f"<div class='cat-divider'>{categoria}</div>", unsafe_allow_html=True)
        cols = st.columns(2)
        for i, (nombre, codigo, desc, url) in enumerate(items):
            with cols[i % 2]:
                st.markdown(f"""
                    <a href="{url}" target="_blank" class="card-link">
                        <div class="custom-card">
                            <div class="doc-code">{codigo}</div>
                            <div class="doc-title" style="font-size:1.3rem;">{nombre}</div>
                            <p style="color:#64748b;font-size:0.95rem;margin-top:10px;font-style:italic;">{desc}</p>
                        </div>
                    </a>
                """, unsafe_allow_html=True)

    st.markdown("<br><br><p style='text-align: center; color: #cbd5e1; font-size: 0.95rem; letter-spacing: 10px; font-weight: 800;'>CODEX ALIMENTARIUS • DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

