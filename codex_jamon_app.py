import streamlit as st
import webbrowser

# Configuración de la página
st.set_page_config(
    page_title="Manual de Normatividad - Codex",
    page_icon="🍖",
    layout="centered"
)

# Estilos personalizados para emular el diseño minimalista
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #2563eb;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    .title-text {
        font-family: 'Serif';
        font-weight: bold;
        text-align: center;
        color: #0f172a;
        text-transform: uppercase;
    }
    .category-header {
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 10px;
        margin-top: 30px;
        color: #1e293b;
        font-weight: bold;
        text-transform: uppercase;
    }
    .doc-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicialización del estado de la aplicación
if 'view' not in st.session_state:
    st.session_state.view = 'splash'

# --- VISTA: PORTADA (SPLASH) ---
if st.session_state.view == 'splash':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 class='title-text'>Manual de<br><span style='color: #3b82f6;'>Normatividad</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-style: italic;'>Codex Alimentarius</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("INGRESAR"):
            st.session_state.view = 'selection'
            st.rerun()
    
    st.markdown("<br><br><br><p style='text-align: center; font-size: 10px; color: #94a3b8; letter-spacing: 2px;'>DESARROLLADO POR<br><b>DIEGO ARMANDO CUENCA LAVANA</b></p>", unsafe_allow_html=True)

# --- VISTA: SELECCIÓN ---
elif st.session_state.view == 'selection':
    st.markdown("<h2 class='title-text'>Seleccione un Producto</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Consulte la normativa detallada para cada categoría.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("""
        <div style='background-color: white; padding: 30px; border-radius: 30px; border: 1px solid #e2e8f0; text-align: center; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);'>
            <h3 style='color: #1e293b; margin-bottom: 5px;'>JAMÓN CURADO COCIDO</h3>
            <p style='color: #3b82f6; font-weight: bold; font-size: 12px;'>CXS 96-1981</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ver Normatividad Detallada"):
            st.session_state.view = 'manual'
            st.rerun()

# --- VISTA: MANUAL DETALLADO ---
elif st.session_state.view == 'manual':
    if st.button("← Volver", key="back"):
        st.session_state.view = 'selection'
        st.rerun()
        
    st.markdown("<h1 class='title-text'>Normatividad Detallada</h1>", unsafe_allow_html=True)
    
    # Datos del manual
    categorias = {
        "I. PRÁCTICAS (CXC)": [
            ("Higiene / Principios", "CXC 1-1969", "Bases fundamentales para el control de higiene en toda la cadena alimentaria.", "https://www.fao.org/4/a1552s/a1552s00.pdf"),
            ("Higiene / Carne", "CXC 58-2005", "Código específico para la manipulación sanitaria de productos cárnicos.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXC%2B58-2005%252FCXC_058s.pdf"),
            ("Higiene / Pocos Ácidos", "CXC 23-1979", "Normas para alimentos procesados térmicamente y envasados herméticamente.", "https://www.fao.org/3/y1579s/y1579s02.pdf")
        ],
        "II. DIRECTRICES (CXG)": [
            ("Aditivos / Aromatizantes", "CXG 66-2008", "Regula el uso de aromas y saborizantes, fundamental para el proceso de ahumado.", "https://www.fao.org/input/download/standards/11020/cxg_066s.pdf"),
            ("Higiene / Microbiano", "CXG 21-1997", "Directrices para establecer límites de bacterias y microorganismos seguros.", "https://www.fao.org/4/y5307s/y5307s04.htm")
        ],
        "III. GENERALES (CXS)": [
            ("Aditivos Alimentarios", "CXS 192-1995", "Lista oficial de sustancias permitidas en el procesamiento de alimentos.", "https://www.fao.org/gsfaonline/docs/CXS_192s.pdf"),
            ("Contaminantes / Toxinas", "CXS 193-1995", "Límites máximos para metales pesados y contaminantes accidentales.", "https://www.fao.org/fileadmin/user_upload/livestockgov/documents/CXS_193s.pdf"),
            ("Etiquetado / Envasados", "CXS 1-1985", "Normas de etiquetado para informar correctamente al consumidor final.", "https://www.fao.org/4/y2770s/y2770s02.htm"),
            ("Análisis y Muestreo", "CXS 234-1999", "Métodos técnicos de laboratorio para verificar el cumplimiento de normas.", "https://www.fao.org/fao-who-codexalimentarius/sh-proxy/en/?lnk=1&url=https%253A%252F%252Fworkspace.fao.org%252Fsites%252Fcodex%252FStandards%252FCXS%2B234-1999%252FCXS_234s.pdf")
        ]
    }

    for cat_nombre, items in categorias.items():
        st.markdown(f"<h3 class='category-header'>{cat_nombre}</h3>", unsafe_allow_html=True)
        for nombre, codigo, intro, url in items:
            with st.container():
                st.markdown(f"""
                <div class='doc-card'>
                    <h4 style='margin:0; color: #1e293b;'>{nombre}</h4>
                    <span style='color: #3b82f6; font-size: 11px; font-weight: bold;'>{codigo}</span>
                    <p style='font-size: 13px; color: #64748b; font-style: italic; margin-top: 10px;'>{intro}</p>
                </div>
                """, unsafe_allow_html=True)
                st.link_button(f"Abrir {codigo}", url)

    st.markdown("<br><hr><p style='text-align: center; color: #94a3b8; font-size: 12px;'>Diego Armando Cuenca Lavana • Gastronomía</p>", unsafe_allow_html=True)