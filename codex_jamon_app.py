import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Codex Alimentarius - Jamón Curado",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- SISTEMA DE DISEÑO Y CSS AVANZADO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Fondo base */
    .stApp {
        background-color: #020617;
    }

    /* Tipografías */
    h1, h2, h3, .serif-text {
        font-family: 'Playfair Display', serif !important;
        color: #f8fafc;
    }

    p, span, div, .sans-text {
        font-family: 'Inter', sans-serif !important;
        color: #94a3b8;
    }

    /* --- CENTRADO TOTAL DE LA PORTADA --- */
    /* Forzamos que el contenedor de la app sea un flexbox cuando estamos en la portada */
    .stApp:has(.splash-marker) [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
    }

    .hero-box {
        text-align: center;
        padding: 40px;
        z-index: 10;
    }

    .hero-icon {
        font-size: 4rem;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 20px rgba(59, 130, 246, 0.6));
        animation: float 4s ease-in-out infinite;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }

    .main-title {
        font-size: 6rem;
        line-height: 0.8;
        margin: 0;
        letter-spacing: -4px;
        background: linear-gradient(to bottom, #ffffff 0%, #64748b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    .accent-title {
        font-size: 6rem;
        line-height: 0.8;
        margin: 0;
        letter-spacing: -4px;
        color: #3b82f6;
        font-style: italic;
        font-weight: 700;
    }

    .subtitle {
        letter-spacing: 15px;
        font-weight: 300;
        margin-top: 40px !important;
        opacity: 0.6;
        color: white;
        text-transform: uppercase;
        font-size: 0.9rem;
    }

    /* --- TARJETAS (CARDS) --- */
    .custom-card {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 40px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 25px;
    }

    .selection-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid rgba(59, 130, 246, 0.1);
        padding: 60px;
        text-align: center;
    }

    .custom-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 40px 80px -15px rgba(0, 0, 0, 0.2);
        border-color: #3b82f6;
    }

    .doc-title {
        color: #0f172a;
        font-size: 1.6rem;
        font-weight: 800;
        margin-bottom: 10px;
        letter-spacing: -0.8px;
    }

    .doc-code {
        color: #2563eb;
        font-weight: 700;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        background: #eff6ff;
        padding: 6px 14px;
        border-radius: 10px;
        display: inline-block;
        margin-bottom: 20px;
    }

    .doc-desc {
        color: #64748b;
        font-size: 1rem;
        line-height: 1.7;
        font-style: italic;
    }

    /* --- BOTÓN PREMIUM --- */
    div.stButton > button {
        border-radius: 25px !important;
        background: #ffffff !important;
        color: #020617 !important;
        padding: 20px 60px !important;
        font-weight: 800 !important;
        border: none !important;
        transition: all 0.4s ease !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        font-size: 1rem !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4) !important;
        margin-top: 40px !important;
    }

    div.stButton > button:hover {
        background: #3b82f6 !important;
        color: #ffffff !important;
        transform: scale(1.1) !important;
        box-shadow: 0 20px 45px rgba(59, 130, 246, 0.5) !important;
    }

    .cat-divider {
        margin: 80px 0 40px 0;
        padding: 15px 30px;
        background: rgba(255,255,255,0.03);
        border-left: 3px solid #3b82f6;
        color: #f8fafc;
        font-weight: 800;
        letter-spacing: 6px;
        font-size: 1rem;
        text-transform: uppercase;
    }

    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO DE NAVEGACIÓN ---
if 'view' not in st.session_state:
    st.session_state.view = 'splash'

# --- 1. PORTADA (DISEÑO CENTRADO) ---
if st.session_state.view == 'splash':
    # Marcador invisible para activar el CSS de centrado
    st.markdown('<div class="splash-marker"></div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="hero-box">
            <div class="hero-icon">📜</div>
            <h1 class="main-title">MANUAL DE</h1>
            <h1 class="accent-title">NORMATIVIDAD</h1>
            <p class="subtitle">CODEX ALIMENTARIUS</p>
        </div>
    """, unsafe_allow_html=True)
    
    # El botón ahora aparecerá justo debajo del texto y centrado
    if st.button("INGRESAR"):
        st.session_state.view = 'selection'
        st.rerun()
    
    st.markdown("<br><br><br><p style='text-align: center; color: #475569; font-size: 0.75rem; letter-spacing: 8px; font-weight: 600;'>DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. SELECCIÓN (ESTILO MINIMALISTA) ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4.5rem; letter-spacing: -3px; color: white;'>Selección de Producto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.3rem; font-weight: 300;'>Identifique el estándar técnico a inspeccionar.</p>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
            <div class="custom-card selection-card">
                <div style="font-size: 5rem; margin-bottom: 25px;">🍖</div>
                <h3 style="font-size: 2.8rem; color: #0f172a; margin-bottom: 10px; letter-spacing: -1.5px; font-weight: 900;">JAMÓN CURADO COCIDO</h3>
                <div class="doc-code" style="font-size: 1.1rem; padding: 8px 25px;">CXS 96-1981</div>
                <p style="color: #64748b; font-size: 1.2rem; margin-top: 30px; line-height: 1.8; font-weight: 400; font-style: italic;">
                    Estándar internacional de identidad, calidad y seguridad alimentaria para productos cárnicos curados.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("VER MANUAL TÉCNICO →"):
            st.session_state.view = 'manual'
            st.rerun()

# --- 3. MANUAL (ESTILO DE DOCUMENTACIÓN TÉCNICA) ---
elif st.session_state.view == 'manual':
    st.markdown("<style>.stApp { background-color: #fcfdfe; }</style>", unsafe_allow_html=True)
    
    col_back, col_title = st.columns([1, 6])
    with col_back:
        if st.button("← VOLVER"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<h1 style='color: #0f172a; font-size: 4rem; margin-bottom: 10px; letter-spacing: -3px; font-weight: 900;'>Documentación Técnica</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background-color: #f8fafc; border-radius: 30px; padding: 45px; margin-bottom: 60px; border: 1px solid #e2e8f0; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <div style="display: flex; align-items: center; gap: 25px;">
                <div style="font-size: 3rem;">📁</div>
                <div>
                    <h3 style="color: #0f172a; margin: 0; font-size: 2rem; letter-spacing: -1px; font-weight: 800;">JAMÓN CURADO COCIDO</h3>
                    <p style="color: #3b82f6; font-weight: 900; margin: 0; letter-spacing: 3px; font-size: 0.9rem; text-transform: uppercase;">NORMATIVA CONSOLIDADA CXS 96-1981</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

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
                    <div class="custom-card">
                        <div class="doc-code">{codigo}</div>
                        <div class="doc-title">{nombre}</div>
                        <p class="doc-desc">{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"CONSULTAR PDF", url, use_container_width=True)

    st.markdown("<br><br><p style='text-align: center; color: #94a3b8; font-size: 0.9rem; letter-spacing: 5px; font-weight: 700;'>CODEX ALIMENTARIUS • GASTRONOMÍA • 2026</p>", unsafe_allow_html=True)
