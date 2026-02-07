# ============================================================================
# VGT Nexus - Landing Page de Ventas B2B para ISPs
# Design System: VGT Nexus Mobile App Style (Violeta/Clean/Soft UI)
# Desarrollado por Miguel Esteller
# ============================================================================

import streamlit as st

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================
st.set_page_config(
    page_title="VGT Nexus | Control Total de tu Infraestructura",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# ESTILOS CSS PERSONALIZADOS (DESIGN SYSTEM VGT NEXUS)
# ============================================================================
st.markdown("""
<style>
    /* 1. TIPOGRAFÍA (Poppins) */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #2D3142 !important; /* Text Main Force */
    }
    
    /* 2. FONDO GENERAL */
    .stApp {
        background-color: #F4F6F9; /* Background gris azulado claro */
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 3. CLASES DE UTILIDAD (TEXTO) */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2D3142 !important; /* Text Main */
        font-weight: 600; /* SemiBold */
    }
    
    p, li, .stMarkdown p, .stMarkdown li {
        color: #7E84A3 !important; /* Text Secondary */
        font-weight: 400; /* Regular */
        line-height: 1.6;
    }
    
    /* Hero Title */
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        color: #2D3142 !important;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #7E84A3;
        text-align: center;
        max-width: 700px;
        margin: 0 auto 2.5rem auto;
        font-weight: 400;
    }
    
    /* 4. BOTONES (Primary Action) */
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #6C63FF 0%, #5A4FCF 100%);
        color: white !important;
        padding: 1rem 3rem;
        font-size: 1.1rem;
        font-weight: 500; /* Medium */
        border-radius: 50px; /* Pill shape */
        text-decoration: none;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0px 8px 25px rgba(108, 99, 255, 0.25); /* Sombra suave violeta */
        border: none;
    }
    
    .cta-button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 12px 30px rgba(108, 99, 255, 0.35);
    }
    
    /* 5. TARJETAS (Cards & Surface) */
    /* Base Card Style */
    .card-base {
        background: #FFFFFF; /* Surface */
        border-radius: 16px; /* Rounded corners */
        padding: 2rem;
        box-shadow: 0px 4px 20px rgba(108, 99, 255, 0.08); /* Sombra difusa */
        height: 100%;
        transition: transform 0.3s ease;
        border: 1px solid rgba(108, 99, 255, 0.05); /* Borde sutil */
    }
    
    .card-base:hover {
        transform: translateY(-5px);
        box-shadow: 0px 8px 30px rgba(108, 99, 255, 0.12);
    }
    
    /* Problem Card Styles */
    .problem-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
        display: inline-block;
        padding: 12px;
        background: #ECEBFF; /* Success/Accent Background */
        border-radius: 12px;
        color: #6C63FF;
    }
    
    .problem-title {
        color: #2D3142;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Feature/Solution Card Styles */
    .feature-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0px 4px 20px rgba(108, 99, 255, 0.05);
        border: 1px solid rgba(108, 99, 255, 0.05);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        color: #6C63FF; 
    }
    
    /* Pricing Cards */
    .pricing-card {
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 4px 20px rgba(108, 99, 255, 0.08);
        border: 1px solid transparent;
        position: relative;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .pricing-card.featured {
        border: 2px solid #6C63FF;
        background: linear-gradient(180deg, #ECEBFF 0%, #FFFFFF 30%);
        transform: scale(1.02);
        box-shadow: 0px 10px 40px rgba(108, 99, 255, 0.15);
        z-index: 10;
    }
    
    .pricing-header {
        margin-bottom: 1.5rem;
    }
    
    .pricing-price {
        font-size: 2.5rem;
        font-weight: 700;
        color: #6C63FF;
        margin: 0.5rem 0;
    }
    
    .pricing-price span {
        font-size: 1rem;
        font-weight: 400;
        color: #7E84A3;
    }
    
    .pricing-features {
        list-style: none;
        padding: 0;
        margin: 1.5rem 0;
        text-align: left;
        flex-grow: 1;
    }
    
    .pricing-features li {
        padding: 0.6rem 0;
        border-bottom: 1px dashed #ECEBFF;
        display: flex;
        align-items: center;
        font-size: 0.95rem;
    }
    
    .pricing-features li::before {
        content: "✔";
        color: #6C63FF;
        font-weight: 700;
        margin-right: 10px;
        background: #ECEBFF;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        font-size: 0.7rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Section Headers */
    .section-header {
        text-align: center;
        margin: 4rem 0 3rem 0;
    }
    
    .section-header h2 {
        font-size: 2.2rem;
        color: #2D3142;
        margin-bottom: 0.5rem;
    }
    
    .section-header-pill {
        display: inline-block;
        background: #ECEBFF;
        color: #6C63FF;
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
    }
    
    /* Footer */
    .footer {
        background: #FFFFFF;
        padding: 4rem 2rem;
        text-align: center;
        border-top: 1px solid #ECEBFF;
        margin-top: 5rem;
    }
    
    /* Inputs Override (Streamlit) */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px !important;
        border: 1px solid #E0E0E0 !important;
        background-color: #FFFFFF !important;
        color: #2D3142 !important;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #6C63FF !important;
        box-shadow: 0 0 0 2px rgba(108, 99, 255, 0.2) !important;
    }
    
    /* Button Override (Streamlit Form Submit) */
    .stButton > button {
        background-color: #6C63FF !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.5rem 2rem !important;
        font-weight: 500 !important;
    }
    
    .stButton > button:hover {
        background-color: #5A4FCF !important;
        box-shadow: 0px 4px 15px rgba(108, 99, 255, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HERO SECTION
# ============================================================================

# Nav/Logo Placeholder
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
<div style="display: flex; align-items: center; justify-content: center; gap: 25px; margin-top: 2rem; margin-bottom: 2rem;">
    <!-- Logo SVG VGT NEXUS -->
    <svg width="100" height="100" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0px 4px 6px rgba(108, 99, 255, 0.2));">
        <path d="M1 6V22L8 18L16 22L23 18V2L16 6L8 2L1 6Z" stroke="#6C63FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M8 2V18" stroke="#6C63FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M16 6V22" stroke="#6C63FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <div style="text-align: left; line-height: 1;">
        <div style="font-size: 3.5rem; font-weight: 800; color: #6C63FF; letter-spacing: -2px; margin-bottom: -5px;">VGT</div>
        <div style="font-size: 3.5rem; font-weight: 800; color: #2D3142; letter-spacing: -1px;">NEXUS</div>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<h1 class="hero-title">
    ¿Cuánto dinero pierde tu ISP hoy por<br>
    <span style="color: #6C63FF;">no controlar tu infraestructura?</span>
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class="hero-subtitle">
    Evita cortes de fibra, multas innecesarias y tiempos muertos.<br>
    <strong>VGT Nexus</strong> pone el control de tu red en la palma de tu mano.
</p>
""", unsafe_allow_html=True)

# CTA Button


# ============================================================================
# PROBLEM SECTION
# ============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-header-pill">Problemáticas</span>
    <h2>El Desorden Cuesta Dólares</h2>
    <p style="color: #7E84A3;">Identifica si tu ISP sufre de estos síntomas comunes</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="card-base">
        <div class="problem-icon">✂️</div>
        <div class="problem-title">Cortes Imprevistos</div>
        <p>
            Cada corte es una emergencia. Pierdes horas buscando el punto de falla y clientes molestos cancelan el servicio.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-base">
        <div class="problem-icon">📄</div>
        <div class="problem-title">Multas Regulatorias</div>
        <p>
            Procedatos y Conatel exigen documentación al día. Una multa por falta de VGTs puede superar los <strong>$5,000</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card-base">
        <div class="problem-icon">🙈</div>
        <div class="problem-title">Inventario Ciego</div>
        <p>
            ¿Sabes exactamente cuántos postes usas? Sin datos precisos, estás pagando de más o perdiendo activos valiosos.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# SOLUTION SECTION
# ============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-header-pill">Solución</span>
    <h2>Tu Centro de Control Inteligente</h2>
    <p>Diseñado específicamente para la realidad de los ISPs venezolanos</p>
</div>
""", unsafe_allow_html=True)

# Feature Highlights Row
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⏱️</div>
        <h3>Auditoría Real-Time</h3>
        <p>Sincronización instantánea entre campo y oficina.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📍</div>
        <h3>Mapas de Precisión</h3>
        <p>Geolocalización exacta de postes y mufas.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">�</div>
        <h3>Control de Pagos</h3>
        <p>Administra y lleva el control de los pagos VGT realizados mes por mes.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# App Screenshots Section
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div style="background: white; border-radius: 20px; padding: 20px; box-shadow: 0px 10px 40px rgba(0,0,0,0.05); text-align: center;">
        <h4 style="color: #6C63FF; margin-bottom: 1rem;">App Móvil de Campo</h4>
        <div style="background: #F4F6F9; height: 350px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #7E84A3; border: 2px dashed #E0E0E0;">
            PLACEHOLDER APP MÓVIL
        </div>
    </div>
    """, unsafe_allow_html=True)
    # st.image("assets/app_mobile.png")

with col2:
    st.markdown("""
    <div style="background: white; border-radius: 20px; padding: 20px; box-shadow: 0px 10px 40px rgba(0,0,0,0.05); text-align: center;">
        <h4 style="color: #6C63FF; margin-bottom: 1rem;">Dashboard Web</h4>
        <div style="background: #F4F6F9; height: 350px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #7E84A3; border: 2px dashed #E0E0E0;">
            PLACEHOLDER MAPA WEB
        </div>
    </div>
    """, unsafe_allow_html=True)
    # st.image("assets/app_web.png")

# CTA Button (Moved from Hero)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; margin-bottom: 2rem;">
        <a href="#contacto" class="cta-button">Solicitar Demo Piloto</a>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PRICING SECTION
# ============================================================================
st.markdown("""
<div class="section-header">
    <span class="section-header-pill">Precios</span>
    <h2>Planes Flexibles</h2>
    <p>Escala según el tamaño de tu red. Sin contratos forzosos.</p>
</div>
""", unsafe_allow_html=True)

# Free Demo Banner
st.markdown("""
<div style="background: #ECEBFF; border: 1px solid #6C63FF; border-radius: 16px; padding: 1.5rem; text-align: center; max-width: 600px; margin: 0 auto 3rem auto; color: #5A4FCF;">
    <span style="font-size: 1.5rem; vertical-align: middle;">🎁</span> 
    <span style="font-weight: 600; font-size: 1.1rem; margin-left: 10px;">Prueba GRATIS por 1 Semana - Sin compromiso</span>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="pricing-card">
        <div class="pricing-header">
            <h3 style="margin: 0;">Arranque</h3>
            <p style="font-size: 0.9rem;">Pequeños ISPs</p>
        </div>
        <div class="pricing-price">$70<span>/mes</span></div>
        <ul class="pricing-features">
            <li>Hasta <strong>500 postes</strong></li>
            <li>Gestión básica</li>
            <li>App Móvil</li>
            <li>Mapa Web</li>
            <li>Soporte Email</li>
        </ul>
        <a href="#contacto" style="display: block; padding: 0.8rem; border-radius: 12px; border: 1px solid #6C63FF; color: #6C63FF; text-decoration: none; font-weight: 500; margin-top: auto;">Elegir Plan</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pricing-card featured">
        <div style="background: #6C63FF; color: white; padding: 4px 12px; border-radius: 50px; font-size: 0.75rem; font-weight: 600; position: absolute; top: -12px; left: 50%; transform: translateX(-50%); text-transform: uppercase;">Más Popular</div>
        <div class="pricing-header">
            <h3 style="color: #6C63FF; margin: 0;">Expansión</h3>
            <p style="font-size: 0.9rem;">Crecimiento acelerado</p>
        </div>
        <div class="pricing-price">$150<span>/mes</span></div>
        <ul class="pricing-features">
            <li>Hasta <strong>1,000 postes</strong></li>
            <li>Onboarding Asistido</li>
            <li>App Móvil Ilimitada</li>
            <li>Reportes PDF Avanzados</li>
            <li>Soporte Prioritario</li>
        </ul>
        <a href="#contacto" style="display: block; padding: 0.8rem; border-radius: 12px; background: #6C63FF; color: white; text-decoration: none; font-weight: 500; margin-top: auto; box-shadow: 0 4px 12px rgba(108, 99, 255, 0.3);">Elegir Plan</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="pricing-card" style="background: #2D3142; color: white;">
        <div class="pricing-header">
            <h3 style="color: white; margin: 0;">Enterprise</h3>
            <p style="color: #7E84A3; font-size: 0.9rem;">Grandes Redes</p>
        </div>
        <div class="pricing-price" style="color: white; font-size: 2rem;">A Medida</div>
        <ul class="pricing-features">
            <li style="border-color: #4a4a68; color: #E0E0E0;">Postes Ilimitados</li>
            <li style="border-color: #4a4a68; color: #E0E0E0;">Integración API</li>
            <li style="border-color: #4a4a68; color: #E0E0E0;">Auditoría Masiva</li>
            <li style="border-color: #4a4a68; color: #E0E0E0;">Gerente de Cuenta</li>
        </ul>
        <a href="#contacto" style="display: block; padding: 0.8rem; border-radius: 12px; background: #FFFFFF; color: #2D3142; text-decoration: none; font-weight: 500; margin-top: auto;">Contactar Ventas</a>
    </div>
    """, unsafe_allow_html=True)

# Addon Card
st.markdown("""
<div style="margin-top: 2rem; text-align: center;">
    <div style="display: inline-block; background: #FFF; padding: 1rem 2rem; border-radius: 16px; border: 1px dashed #6C63FF; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        <span style="font-weight: 600; color: #2D3142;">¿Necesitas más capacidad?</span>
        <span style="color: #7E84A3; margin: 0 10px;">|</span>
        <span style="color: #6C63FF; font-weight: 600;">+100 postes extra por $7.99/mes</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================================
# CONTACT FORM
# ============================================================================
st.markdown('<div id="contacto"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <span class="section-header-pill">Contacto</span>
    <h2>Solicita tu Demo</h2>
    <p>Déjanos tus datos y te contactaremos a la brevedad.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with st.container():
        st.markdown('<div class="card-base" style="padding: 2.5rem;">', unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            
            c1, c2 = st.columns(2)
            with c1:
                nombre = st.text_input("Nombre del ISP")
            with c2:
                telefono = st.text_input("WhatsApp")
                
            email = st.text_input("Correo Corporativo")
            
            postes = st.selectbox("Cantidad de Postes", ["< 200", "200 - 500", "500 - 1000", "1000+"])
            
            mensaje = st.text_area("Mensaje Adicional", height=100)
            
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("🚀 Enviar Solicitud", use_container_width=True)
            
            if submitted:
                st.success("¡Recibido! Nos pondremos en contacto contigo pronto.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
<div class="footer">
    <div style="display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 1.5rem;">
        <!-- Logo SVG VGT NEXUS (Footer Version) -->
        <svg width="70" height="70" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0px 4px 6px rgba(108, 99, 255, 0.2));">
            <path d="M1 6V22L8 18L16 22L23 18V2L16 6L8 2L1 6Z" stroke="#6C63FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M8 2V18" stroke="#6C63FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M16 6V22" stroke="#6C63FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <div style="text-align: left; line-height: 1;">
            <div style="font-size: 2.2rem; font-weight: 800; color: #6C63FF; letter-spacing: -1px; margin-bottom: -5px;">VGT</div>
            <div style="font-size: 2.2rem; font-weight: 800; color: #2D3142; letter-spacing: 0px;">NEXUS</div>
        </div>
    </div>
    <p style="font-size: 0.9rem;">Tecnología 100% Venezolana 🇻🇪</p>
    <div style="margin-top: 2rem; font-size: 0.85rem; color: #7E84A3;">
        © 2026 VGT Nexus. Todos los derechos reservados.<br>
        Desarrollado por Miguel Esteller
    </div>
</div>
""", unsafe_allow_html=True)
