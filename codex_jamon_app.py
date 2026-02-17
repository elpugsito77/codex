import streamlit as st

# Configuración de página para eliminar márgenes innecesarios
st.set_page_config(
    page_title="Manual de Normatividad - Codex Jamón",
    page_icon="🍖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INYECCIÓN DE CSS AVANZADO PARA DISEÑO PREMIUM Y ANIMACIONES ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:wght@700&display=swap');

    /* Estilos Globales */
    .stApp {
        background-color: #f8fafc;
    }

    h1, h2, h3, .serif-text {
        font-family: 'Playfair Display', serif !important;
        color: #0f172a;
    }

    p, span, div, .sans-text {
        font-family: 'Inter', sans-serif !important;
    }

    /* --- PORTADA (SPLASH SCREEN) --- */
    .splash-bg {
        background-color: #0d162a;
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100vh;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        z-index: 1000;
        color: white;
        text-align: center;
    }

    /* --- TARJETAS (CARDS) CON ANIMACIÓN HOVER --- */
    .custom-card {
        background-color: white;
        padding: 30px;
        border-radius: 30px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        text-align: center;
        margin-bottom: 20px;
    }

    .custom-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
        border-color: #3b82f6;
    }

    /* --- BOTONES PREMIUM --- */
    .stButton>button {
        border-radius: 50px !important;
        background-color: #2563eb !important;
        color: white !important;
        padding: 12px 35px !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3) !important;
    }

    .stButton>button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.4) !important;
        background-color: #3b82f6 !important;
    }

    /* --- DIVISORES DE CATEGORÍA --- */
    .cat-divider {
        display: flex;
        align-items: center;
        text-align: center;
        margin: 40px 0;
        color: #94a3b8;
        font-size: 0.8rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: 700;
    }
    .cat-divider::before, .cat-divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid #e2e8f0;
    }
    .cat-divider:not(:empty)::before { margin-right: 1.5em; }
    .cat-divider:not(:empty)::after { margin-left: 1.5em; }

    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- MANEJO DE ESTADO DE NAVEGACIÓN ---
if 'view' not in st.session_state:
    st.session_state.view = 'splash'

# --- 1. VISTA DE PORTADA (ESTILO OSCURO) ---
if st.session_state.view == 'splash':
    st.markdown("""
        <div style="background-color: #0d162a; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 20px;">
            <div style="border: 2px solid #3b82f6; border-radius: 15px; padding: 15px; margin-bottom: 25px;">
                <span style="font-size: 2rem;">📖</span>
            </div>
            <h1 style="color: white; font-size: 3.5rem; line-height: 1; margin: 0;">MANUAL DE</h1>
            <h1 style="color: #60a5fa; font-size: 3.5rem; line-height: 1; margin: 0;">NORMATIVIDAD</h1>
            <p style="color: #94a3b8; font-style: italic; font-size: 1.2rem; margin-top: 15px;">Codex Alimentarius</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INGRESAR"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<p style='text-align: center; color: #475569; font-size: 0.7rem; letter-spacing: 3px; margin-top: 50px;'>DESARROLLADO POR DIEGO ARMANDO CUENCA LAVANA</p>", unsafe_allow_html=True)

# --- 2. VISTA DE SELECCIÓN DE PRODUCTO (ESTILO LIMPIO) ---
elif st.session_state.view == 'selection':
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>Seleccione un Producto</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Consulte la normativa detallada para cada categoría de producto.</p>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Aquí usamos la imagen del jamón en tabla que pediste
        st.markdown(f"""
            <div class="custom-card">
                <img src="https://images.unsplash.com/photo-1544077960-604201fe74bc?auto=format&fit=crop&q=80&w=600" style="width: 100%; border-radius: 20px; margin-bottom: 20px;">
                <h3 style="font-size: 1.8rem; margin-bottom: 5px;">JAMÓN CURADO COCIDO</h3>
                <span style="background-color: #eff6ff; color: #2563eb; font-weight: 700; padding: 5px 15px; border-radius: 10px; font-size: 0.8rem;">CXS 96-1981</span>
                <p style="color: #64748b; font-size: 0.9rem; margin-top: 15px;">Normatividad técnica para procesamiento de jamón.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ver Normatividad →"):
            st.session_state.view = 'manual'
            st.rerun()

# --- 3. VISTA DE MANUAL DETALLADO (ESTILO CARTAS INTERACTIVAS) ---
elif st.session_state.view == 'manual':
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("← Volver"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<h1 style='font-size: 2.5rem; margin-bottom: 30px;'>Normatividad Detallada</h1>", unsafe_allow_html=True)
    
    # Encabezado con imagen
    st.markdown("""
        <div style="background-color: white; border: 1px solid #e2e8f0; border-radius: 25px; padding: 25px; display: flex; align-items: center; gap: 20px; margin-bottom: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
            <img src="https://images.unsplash.com/photo-1544077960-604201fe74bc?auto=format&fit=crop&q=80&w=150" style="width: 80px; height: 80px; border-radius: 15px; object-fit: cover;">
            <div>
                <h3 style="margin: 0;">JAMÓN CURADO COCIDO</h3>
                <p style="color: #3b82f6; font-weight: 600; margin: 0;">CXS 96-1981 • Normatividad para Jamón Curado Cocido</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Estructura del Manual según la imagen proporcionada
    manual_data = {
        "I. PRÁCTICAS (CXC)": [
            ("Higiene / Principios", "CXC 1-1969", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
            ("Higiene / Carne", "CXC 58-2004", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXC%B58-2005%252FCXC_058s.pdf"),
            ("Higiene / Pocos Ácidos", "CXC 23-1979", "https://www.fao.org/3/y1579s/y1579s02.pdf"),
        ],
        "II. DIRECTRICES (CXG)": [
            ("Aditivos / Aromatizantes", "CXG 66-2008", "https://www.fao.org/input/download/standards/11020/cxg_066s.pdf"),
            ("Higiene / Microbiano", "CXG 21-1997", "https://www.fao.org/4/y5307s/y5307s04.htm"),
        ],
        "III. GENERALES (CXS)": [
            ("Aditivos Alimentarios", "CXS 192-1995", "https://www.fao.org/gsfaonline/docs/CXS_192s.pdf"),
            ("Contaminantes / Toxinas", "CXS 193-1995", "https://www.fao.org/fileadmin/user_upload/livestockgov/documents/CXS_193s.pdf"),
            ("Etiquetado / Envasados", "CXS 1-1985", "https://www.fao.org/4/y2770s/y2770s02.htm"),
            ("Etiquetado / No Minorista", "CXS 346-2021", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B346-2021%252FCXS_346s.pdf"),
            ("Análisis y Muestreo", "CXS 234-1999", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%B234-1999%252FCXS_234s.pdf"),
        ]
    }

    for categoria, items in manual_data.items():
        st.markdown(f"<div class='cat-divider'>{categoria}</div>", unsafe_allow_html=True)
        
        # Grid de 2 columnas para las tarjetas de documentos
        cols = st.columns(2)
        for i, (nombre, codigo, url) in enumerate(items):
            with cols[i % 2]:
                st.markdown(f"""
                    <div class="custom-card" style="padding: 20px; text-align: left; min-height: 120px; display: flex; flex-direction: column; justify-content: center;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <div>
                                <h4 style="margin: 0; font-size: 1.1rem; color: #1e293b;">{nombre}</h4>
                                <p style="color: #64748b; font-size: 0.8rem; font-weight: 600; margin: 5px 0;">{codigo}</p>
                            </div>
                            <span style="font-size: 1.2rem; opacity: 0.3;">📄</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button("Abrir Documento", url, use_container_width=True)

    st.markdown("<br><br><p style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>CODEX ALIMENTARIUS • GASTRONOMÍA • 2026</p>", unsafe_allow_html=True)
