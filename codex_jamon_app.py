import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Manual de Normatividad - Codex Jamón",
    page_icon="🍖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INYECCIÓN DE CSS AVANZADO PARA DISEÑO ULTRA-PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Variables de diseño */
    :root {
        --glass: rgba(255, 255, 255, 0.05);
        --glass-border: rgba(255, 255, 255, 0.1);
        --accent: #3b82f6;
    }

    .stApp {
        background-color: #020617;
    }

    /* Tipografías */
    h1, h2, h3, .serif-text {
        font-family: 'Playfair Display', serif !important;
        color: white;
    }

    p, span, div, .sans-text {
        font-family: 'Inter', sans-serif !important;
        color: #94a3b8;
    }

    /* --- PORTADA REDISEÑADA (GLOW EFFECT) --- */
    .splash-container {
        height: 80vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        background: radial-gradient(circle at center, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 50px;
        border-radius: 40px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }

    /* --- TARJETAS (CARDS) CON ANIMACIÓN --- */
    .custom-card {
        background-color: white;
        padding: 35px;
        border-radius: 35px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 20px;
    }

    .custom-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.12);
        border-color: #3b82f6;
    }

    .doc-title {
        color: #0f172a;
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 5px;
        letter-spacing: -0.5px;
    }

    .doc-code {
        color: #2563eb;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .doc-desc {
        color: #64748b;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-top: 15px;
        font-style: italic;
    }

    /* --- BOTONES PREMIUM --- */
    .stButton>button {
        border-radius: 20px !important;
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%) !important;
        color: white !important;
        padding: 15px 45px !important;
        font-weight: 700 !important;
        border: none !important;
        transition: all 0.4s ease !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .stButton>button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 0 30px rgba(37, 99, 235, 0.5) !important;
    }

    /* DIVISORES */
    .cat-divider {
        margin: 60px 0 30px 0;
        padding: 10px 20px;
        background: rgba(255,255,255,0.03);
        border-left: 4px solid #3b82f6;
        color: white;
        font-weight: 800;
        letter-spacing: 3px;
    }

    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- MANEJO DE ESTADO DE NAVEGACIÓN ---
if 'view' not in st.session_state:
    st.session_state.view = 'splash'

# --- 1. VISTA DE PORTADA (REDISEÑO PRO) ---
if st.session_state.view == 'splash':
    st.markdown('<div class="splash-container">', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-box">
            <div style="font-size: 3rem; margin-bottom: 20px;">📖</div>
            <h1 style="font-size: 4.5rem; line-height: 0.9; margin: 0; letter-spacing: -2px;">MANUAL DE</h1>
            <h1 style="font-size: 4.5rem; line-height: 0.9; margin: 0; letter-spacing: -2px; color: #3b82f6; font-style: italic;">NORMATIVIDAD</h1>
            <p style="letter-spacing: 8px; font-weight: 300; margin-top: 20px; opacity: 0.6;">CODEX ALIMENTARIUS</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INGRESAR AL SISTEMA"):
            st.session_state.view = 'selection'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: #475569; font-size: 0.7rem; letter-spacing: 5px; margin-top: 20px;'>AUTOR: DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. VISTA DE SELECCIÓN ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 4rem; letter-spacing: -1px;'>Seleccione un Producto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.2rem;'>Gestión normativa especializada para cárnicos.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Imagen del jamón en tabla
        st.markdown(f"""
            <div class="custom-card" style="text-align: center;">
                <img src="https://images.unsplash.com/photo-1544077960-604201fe74bc?auto=format&fit=crop&q=80&w=800" style="width: 100%; border-radius: 30px; margin-bottom: 25px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                <h3 style="font-size: 2.2rem; color: #0f172a; margin-bottom: 5px;">JAMÓN CURADO COCIDO</h3>
                <span style="background-color: #eff6ff; color: #2563eb; font-weight: 800; padding: 6px 20px; border-radius: 12px; font-size: 0.9rem;">CXS 96-1981</span>
                <p style="color: #64748b; font-size: 1rem; margin-top: 20px; font-weight: 500;">Normas técnicas de procesamiento, calidad y seguridad.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ABRIR MANUAL COMPLETO →"):
            st.session_state.view = 'manual'
            st.rerun()

# --- 3. VISTA DE MANUAL CON DESCRIPCIONES ---
elif st.session_state.view == 'manual':
    st.markdown("<style>.stApp { background-color: #f8fafc; }</style>", unsafe_allow_html=True)
    
    col_back, col_title = st.columns([1, 6])
    with col_back:
        if st.button("← VOLVER"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<h1 style='color: #0f172a; font-size: 3.5rem; margin-bottom: 10px;'>Normatividad Detallada</h1>", unsafe_allow_html=True)
    
    # Cabecera
    st.markdown("""
        <div style="background-color: white; border-radius: 30px; padding: 30px; display: flex; align-items: center; gap: 30px; margin-bottom: 50px; border: 1px solid #e2e8f0;">
            <img src="https://images.unsplash.com/photo-1544077960-604201fe74bc?auto=format&fit=crop&q=80&w=150" style="width: 100px; height: 100px; border-radius: 20px; object-fit: cover;">
            <div>
                <h3 style="color: #0f172a; margin: 0; font-size: 1.8rem;">JAMÓN CURADO COCIDO</h3>
                <p style="color: #3b82f6; font-weight: 700; margin: 0;">NORMATIVA TÉCNICA CXS 96-1981</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Datos con descripciones agregadas
    manual_data = {
        "I. PRÁCTICAS (CXC)": [
            ("Higiene / Principios", "CXC 1-1969", "Bases fundamentales para el control de higiene en toda la cadena alimentaria.", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
            ("Higiene / Carne", "CXC 58-2005", "Código específico para la manipulación sanitaria de productos cárnicos.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXC%B58-2005%252FCXC_058s.pdf"),
            ("Higiene / Pocos Ácidos", "CXC 23-1979", "Normas para alimentos procesados térmicamente y envasados herméticamente.", "https://www.fao.org/3/y1579s/y1579s02.pdf"),
        ],
        "II. DIRECTRICES (CXG)": [
            ("Aditivos / Aromatizantes", "CXG 66-2008", "Regula el uso de aromas y saborizantes, fundamental para el proceso de ahumado.", "https://www.fao.org/input/download/standards/11020/cxg_066s.pdf"),
            ("Higiene / Microbiano", "CXG 21-1997", "Directrices para establecer límites de bacterias y microorganismos seguros.", "https://www.fao.org/4/y5307s/y5307s04.htm"),
        ],
        "III. GENERALES (CXS)": [
            ("Aditivos Alimentarios", "CXS 192-1995", "Lista oficial de sustancias permitidas en el procesamiento de alimentos.", "https://www.fao.org/gsfaonline/docs/CXS_192s.pdf"),
            ("Contaminantes / Toxinas", "CXS 193-1995", "Límites máximos para metales pesados y contaminantes accidentales.", "https://www.fao.org/fileadmin/user_upload/livestockgov/documents/CXS_193s.pdf"),
            ("Etiquetado / Envasados", "CXS 1-1985", "Normas de etiquetado para informar correctamente al consumidor final.", "https://www.fao.org/4/y2770s/y2770s02.htm"),
            ("Etiquetado / No Minorista", "CXS 346-2021", "Requisitos de información para envases destinados a la industria y mayoreo.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B346-2021%252FCXS_346s.pdf"),
            ("Análisis y Muestreo", "CXS 234-1999", "Métodos técnicos de laboratorio para verificar el cumplimiento de normas.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B234-1999%252FCXS_234s.pdf"),
        ]
    }

    for categoria, items in manual_data.items():
        st.markdown(f"<div class='cat-divider'>{categoria}</div>", unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, (nombre, codigo, desc, url) in enumerate(items):
            with cols[i % 2]:
                st.markdown(f"""
                    <div class="custom-card">
                        <div class="doc-title">{nombre}</div>
                        <div class="doc-code">{codigo}</div>
                        <div class="doc-desc">{desc}</div>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"VER PDF OFICIAL", url, use_container_width=True)

    st.markdown("<br><br><p style='text-align: center; color: #94a3b8; font-size: 0.8rem; font-weight: bold;'>CODEX ALIMENTARIUS • GASTRONOMÍA • 2026</p>", unsafe_allow_html=True)
