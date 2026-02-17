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

    /* --- PORTADA REDISEÑADA (ESTILO BOUTIQUE) --- */
    .splash-container {
        height: 85vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        background: 
            radial-gradient(circle at 20% 30%, rgba(37, 99, 235, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(30, 64, 175, 0.08) 0%, transparent 40%);
    }

    .hero-box {
        position: relative;
        padding: 60px;
        border-radius: 40px;
        transition: all 0.5s ease;
    }

    .hero-icon {
        font-size: 3.5rem;
        margin-bottom: 25px;
        filter: drop-shadow(0 0 15px rgba(59, 130, 246, 0.5));
        animation: float 4s ease-in-out infinite;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }

    .main-title {
        font-size: 5.5rem;
        line-height: 0.85;
        margin: 0;
        letter-spacing: -3px;
        background: linear-gradient(to bottom, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .accent-title {
        font-size: 5.5rem;
        line-height: 0.85;
        margin: 0;
        letter-spacing: -3px;
        color: #3b82f6;
        font-style: italic;
    }

    /* --- TARJETAS (CARDS) SIN FOTOS --- */
    .custom-card {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 35px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 20px;
    }

    .selection-card {
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
        border: 1px solid rgba(59, 130, 246, 0.1);
        padding: 60px;
        text-align: center;
    }

    .custom-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.15);
        border-color: #3b82f6;
    }

    .doc-title {
        color: #0f172a;
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }

    .doc-code {
        color: #2563eb;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        background: #eff6ff;
        padding: 4px 12px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 15px;
    }

    .doc-desc {
        color: #64748b;
        font-size: 0.95rem;
        line-height: 1.6;
        font-style: italic;
    }

    /* --- BOTONES --- */
    .stButton>button {
        border-radius: 18px !important;
        background: #ffffff !important;
        color: #0f172a !important;
        padding: 18px 50px !important;
        font-weight: 800 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2) !important;
    }

    .stButton>button:hover {
        background: #3b82f6 !important;
        color: #ffffff !important;
        transform: scale(1.05) !important;
    }

    .cat-divider {
        margin: 70px 0 35px 0;
        padding: 12px 25px;
        background: rgba(255,255,255,0.03);
        border-left: 2px solid #3b82f6;
        color: #f8fafc;
        font-weight: 800;
        letter-spacing: 5px;
        font-size: 0.9rem;
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

# --- 1. PORTADA (DISEÑO TIPOGRÁFICO) ---
if st.session_state.view == 'splash':
    st.markdown('<div class="splash-container">', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-box">
            <div class="hero-icon">📜</div>
            <h1 class="main-title">MANUAL DE</h1>
            <h1 class="accent-title">NORMATIVIDAD</h1>
            <p style="letter-spacing: 12px; font-weight: 300; margin-top: 30px; opacity: 0.5; color: white;">CODEX ALIMENTARIUS</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INICIAR CONSULTA"):
            st.session_state.view = 'selection'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: #475569; font-size: 0.7rem; letter-spacing: 6px; margin-top: 0px;'>DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. SELECCIÓN (ESTILO MINIMALISTA) ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4rem; letter-spacing: -2px;'>Selección de Producto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.2rem; font-weight: 300;'>Identifique el estándar técnico a inspeccionar.</p>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
            <div class="custom-card selection-card">
                <div style="font-size: 4rem; margin-bottom: 20px;">🍖</div>
                <h3 style="font-size: 2.5rem; color: #0f172a; margin-bottom: 10px; letter-spacing: -1px;">JAMÓN CURADO COCIDO</h3>
                <div class="doc-code" style="font-size: 1rem; padding: 6px 20px;">CXS 96-1981</div>
                <p style="color: #64748b; font-size: 1.1rem; margin-top: 25px; line-height: 1.6; font-weight: 400;">
                    Estándar internacional de identidad, calidad y seguridad alimentaria para productos cárnicos curados.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("VER MANUAL TÉCNICO →"):
            st.session_state.view = 'manual'
            st.rerun()

# --- 3. MANUAL (ESTILO DE DOCUMENTACIÓN LIMPIA) ---
elif st.session_state.view == 'manual':
    st.markdown("<style>.stApp { background-color: #fcfdfe; }</style>", unsafe_allow_html=True)
    
    col_back, col_title = st.columns([1, 6])
    with col_back:
        if st.button("← VOLVER"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<h1 style='color: #0f172a; font-size: 3.5rem; margin-bottom: 10px; letter-spacing: -2px;'>Documentación Técnica</h1>", unsafe_allow_html=True)
    
    # Header minimalista
    st.markdown("""
        <div style="background-color: #f8fafc; border-radius: 25px; padding: 40px; margin-bottom: 50px; border: 1px solid #e2e8f0;">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="font-size: 2.5rem;">📁</div>
                <div>
                    <h3 style="color: #0f172a; margin: 0; font-size: 1.8rem; letter-spacing: -1px;">JAMÓN CURADO COCIDO</h3>
                    <p style="color: #3b82f6; font-weight: 800; margin: 0; letter-spacing: 2px; font-size: 0.8rem;">NORMATIVA CONSOLIDADA CXS 96-1981</p>
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

    st.markdown("<br><br><p style='text-align: center; color: #cbd5e1; font-size: 0.8rem; letter-spacing: 4px;'>CODEX ALIMENTARIUS • GASTRONOMÍA • 2026</p>", unsafe_allow_html=True)
