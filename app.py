# ============================================================================
# VGT Nexus - Landing Page de Ventas B2B para ISPs
# Design System: VGT Nexus Mobile App Style (Violeta/Clean/Soft UI)
# Desarrollado por Miguel Esteller
# ============================================================================

import streamlit as st
import os
import base64
import streamlit.components.v1 as components

# ============================================================================
# FUNCIÓN PARA CARGAR TU IMAGEN LOCAL (SIN ERRORES)
# ============================================================================
def get_local_img_as_base64(file_path):
    """
    Intenta cargar una imagen local y convertirla a código para que se vea en el HTML.
    Si no encuentra el archivo, devuelve una imagen de internet por defecto.
    """
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        # Detectar extensión simple
        ext = "png" if file_path.endswith(".png") else "jpeg"
        return f"data:image/{ext};base64,{b64}"
    except FileNotFoundError:
        # Si no encuentra el archivo, devuelve esta imagen de ejemplo de internet
        return "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop"

# 1. IMAGEN HERO (SLIDE 1): La composición de dispositivos original
img_hero = get_local_img_as_base64("static/images/device_composition_hero.png")

# 2. IMAGEN TRAZABILIDAD (SLIDE 1): Imagen del mapa isométrico
img_trazabilidad = get_local_img_as_base64("trazabilidad_hero.png")

# 3. IMAGEN VGT NEXUS (SLIDE 3): Imagen del chip con postes
img_vgt_nexus = get_local_img_as_base64("vgt_nexus_hero.png")

# 4. IMAGEN PROYECTOS: Dashboard de proyectos VGT
img_proyectos = get_local_img_as_base64("proyectos_dashboard.png")

# 5. IMAGEN VENTAJAS: Features de la solución
img_ventajas = get_local_img_as_base64("ventajas_features.png")

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
# ESTILOS CSS
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1E293B;
        scroll-behavior: smooth;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif;
        color: #1E293B;
    }
    
    .stApp {
        background-color: #F8FAFC;
        background-image: radial-gradient(circle at 100% 0%, #EFF6FF 0%, #F8FAFC 50%);
        background-attachment: fixed;
    }
    
    .main .block-container {
        padding-top: 5rem !important;
        padding-bottom: 0rem !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* NAV BAR */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #1E293B;
        z-index: 9999;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.8rem 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }

    .nav-logo {
        display: flex;
        align-items: center;
        gap: 12px;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 1.5rem;
        color: #F8FAFC !important;
        text-decoration: none;
        letter-spacing: -0.5px;
    }
    
    .nav-logo svg { width: 32px; height: 32px; }
    
    .nav-links {
        display: flex;
        gap: 2.5rem;
        align-items: center;
        margin-left: auto;
        margin-right: 2rem;
    }
    
    .nav-link {
        color: #CBD5E1 !important;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.2s;
    }
    
    .nav-link:hover { color: #FFFFFF !important; }
    
    .nav-cta {
        background: #FFFFFF;
        color: #1E293B !important;
        padding: 0.5rem 1.8rem;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 700;
        font-size: 0.9rem;
        transition: transform 0.2s, box-shadow 0.2s;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .nav-cta:hover {
        background: #F1F5F9;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    /* CARD STYLES */
    .pricing-card, .problem-card, .feature-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        border: 1px solid #E2E8F0;
        transition: transform 0.3s, box-shadow 0.3s;
        height: 100%;
        min-height: 220px;
        display: flex;
        flex-direction: column;
    }
    
    .pricing-card:hover, .problem-card:hover, .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
        border-color: #CBD5E1;
    }

    .pricing-header h3 { font-size: 1.5rem; font-weight: 700; }
    .pricing-price { font-size: 2.5rem; font-weight: 800; color: #1E293B; margin: 1rem 0; }
    .pricing-price span { font-size: 1rem; font-weight: 500; color: #64748B; }
    
    .pricing-features { list-style: none; padding: 0; margin: 0 0 2rem 0; flex-grow: 1; }
    .pricing-features li {
        padding: 0.8rem 0;
        border-bottom: 1px solid #F1F5F9;
        color: #475569;
        font-size: 0.95rem;
        display: flex;
        align-items: center;
    }
    .pricing-features li:before {
        content: "✓";
        color: #6366F1;
        font-weight: 800;
        margin-right: 10px;
    }
    
    .cta-button {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
        color: white !important;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.4);
        display: inline-block;
        transition: transform 0.2s;
    }
    .cta-button:hover { transform: translateY(-3px); }

    /* Icon Wrappers */
    .problem-icon-wrapper, .feature-icon-wrapper {
        width: 56px; height: 56px; border-radius: 12px;
        display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;
    }
    .icon-red { background: #FEF2F2; color: #EF4444; }
    .icon-blue { background: #EFF6FF; color: #3B82F6; }
    .icon-orange { background: #FFF7ED; color: #F97316; }
    .bg-purple-light { background: #EEF2FF; }
    .bg-pink-light { background: #FDF2F8; }
    .bg-blue-light { background: #EFF6FF; }

    .problem-title, .feature-title { font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem; color: #1E293B; }
    .problem-description, .feature-text { font-size: 0.95rem; color: #64748B; line-height: 1.6; }
    
    .section-header { text-align: center; margin-bottom: 4rem; max-width: 700px; margin-left: auto; margin-right: auto; }
    .section-header h2 { font-size: 2.5rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -0.5px; }
    .section-header p { font-size: 1.1rem; color: #64748B; }
    .section-header-pill {
        background: #EEF2FF; color: #6366F1; padding: 0.5rem 1rem; border-radius: 50px;
        font-weight: 600; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;
        margin-bottom: 1rem; display: inline-block;
    }

</style>
""", unsafe_allow_html=True)

# ============================================================================
# NAVIGATION BAR
# ============================================================================
st.markdown("""
<div class="nav-container">
    <a href="#" class="nav-logo">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 6V22L8 18L16 22L23 18V2L16 6L8 2L1 6Z" stroke="#6366F1" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M8 2V18" stroke="#6366F1" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M16 6V22" stroke="#6366F1" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>VGT NEXUS</span>
    </a>
    <div class="nav-links">
        <a href="#problematicas" class="nav-link">Problemáticas</a>
        <a href="#solucion" class="nav-link">Solución</a>
        <a href="#precios" class="nav-link">Precios</a>
        <a href="#contacto" class="nav-cta">Solicitar Demo</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================================
# CARRUSEL CON IMÁGENES INYECTADAS (SLIDE 1 Y 2)
# ============================================================================
carousel_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Inter', sans-serif; background-color: transparent; overflow: hidden; }}
        .carousel-container {{ position: relative; width: 100%; height: 600px; overflow: hidden; }}
        
        .slide {{
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            opacity: 0; transition: opacity 1s ease-in-out;
            display: flex; align-items: center; justify-content: center;
            padding: 0 2rem; box-sizing: border-box; pointer-events: none;
        }}
        .slide.active {{ opacity: 1; pointer-events: auto; z-index: 2; }}
        
        .slide-content {{
            display: flex; align-items: center; justify-content: space-between;
            width: 100%; max-width: 1200px; margin: 0 auto; gap: 2rem;
        }}
        
        .slide-text {{ flex: 1; padding-right: 2rem; text-align: left; }}
        
        .slide-image {{ flex: 1.4; display: flex; justify-content: center; align-items: center; }}
        .slide-image img {{
            max-width: 120%; max-height: 600px; height: auto;
            object-fit: contain; filter: drop-shadow(0 10px 20px rgba(0,0,0,0.15));
        }}
        
        .hero-tag {{ display: inline-block; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px; color: #6366F1; margin-bottom: 1rem; text-transform: uppercase; }}
        .hero-title {{ font-family: 'Poppins', sans-serif; font-size: 3.5rem; font-weight: 700; line-height: 1.1; color: #1E293B; margin: 0 0 1.5rem 0; letter-spacing: -1px; }}
        .hero-subtitle {{ font-size: 1.1rem; color: #64748B; line-height: 1.6; margin-bottom: 2rem; max-width: 90%; }}
        
        .btn-hero {{
            display: inline-block; background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
            color: white; padding: 1rem 2.5rem; border-radius: 50px;
            text-decoration: none; font-weight: 600; font-size: 1.1rem;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.4);
        }}
        .btn-hero:hover {{ transform: translateY(-2px); box-shadow: 0 15px 30px -5px rgba(99, 102, 241, 0.5); }}
        
        .carousel-dots {{ position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); display: flex; gap: 12px; z-index: 10; }}
        .dot {{ width: 12px; height: 12px; border-radius: 50%; background-color: #CBD5E1; cursor: pointer; transition: all 0.3s ease; }}
        .dot.active {{ background-color: #6366F1; transform: scale(1.2); width: 24px; border-radius: 10px; }}
        
        @media (max-width: 768px) {{
            .slide-content {{ flex-direction: column-reverse; text-align: center; gap: 1rem; }}
            .slide-text {{ padding-right: 0; text-align: center; }}
            .hero-title {{ font-size: 2.5rem; }}
            .slide-image img {{ max-height: 300px; }}
        }}
    </style>
</head>
<body>

<div class="carousel-container">
    <div class="slide active" id="slide-0">
        <div class="slide-content">
            <div class="slide-text">
                <span class="hero-tag">TRAZABILIDAD TOTAL</span>
                <h1 class="hero-title">Logra la trazabilidad<br>de cada poste<br>que utilizas</h1>
                <p class="hero-subtitle">Maneja datos reales, evita multas. Control total sobre tus activos en campo.</p>
                <div style="margin-top: 2rem;">
                    <a href="#contacto" class="btn-hero" onclick="parent.location.hash='contacto'">Optimiza tu red ahora</a>
                </div>
            </div>
            <div class="slide-image">
                <img src="{img_trazabilidad}" alt="Mapa de Trazabilidad">
            </div>
        </div>
    </div>

    <div class="slide" id="slide-1">
        <div class="slide-content">
            <div class="slide-text">
                <span class="hero-tag">DOBLE HERRAMIENTA</span>
                <h1 class="hero-title">Recopila<br>y Gestiona</h1>
                <p class="hero-subtitle">Con el app móvil recopila y clasifica.<br>Con el app web gestiona tu data.</p>
                <div style="margin-top: 2rem;">
                    <a href="#contacto" class="btn-hero" onclick="parent.location.hash='contacto'">Optimiza tu red ahora</a>
                </div>
            </div>
            <div class="slide-image">
                <img src="{img_hero}" alt="Dashboard ISP">
            </div>
        </div>
    </div>
    
    <div class="slide" id="slide-2">
        <div class="slide-content">
            <div class="slide-text">
                <span class="hero-tag">NEXUS CORE</span>
                <h1 class="hero-title">El primer software<br>para administrar<br>tu VGT</h1>
                <p class="hero-subtitle">No más multas, no más cortes.<br>Todo en un mismo lugar.</p>
                <div style="margin-top: 2rem;">
                    <a href="#contacto" class="btn-hero" onclick="parent.location.hash='contacto'">Optimiza tu red ahora</a>
                </div>
            </div>
            <div class="slide-image">
                <img src="{img_vgt_nexus}" alt="VGT Nexus">
            </div>
        </div>
    </div>

    <div class="carousel-dots">
        <span class="dot active" onclick="currentSlide(0)"></span>
        <span class="dot" onclick="currentSlide(1)"></span>
        <span class="dot" onclick="currentSlide(2)"></span>
    </div>
</div>

<script>
    let slideIndex = 0;
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    const intervalTime = 8000;
    let slideInterval;

    function showSlide(n) {{
        if (n >= slides.length) {{ slideIndex = 0; }}
        else if (n < 0) {{ slideIndex = slides.length - 1; }}
        else {{ slideIndex = n; }}

        slides.forEach(slide => slide.classList.remove('active'));
        dots.forEach(dot => dot.classList.remove('active'));

        slides[slideIndex].classList.add('active');
        dots[slideIndex].classList.add('active');
    }}

    function currentSlide(n) {{
        clearInterval(slideInterval);
        showSlide(n);
        slideInterval = setInterval(nextSlide, intervalTime);
    }}

    function nextSlide() {{
        showSlide(slideIndex + 1);
    }}

    slideInterval = setInterval(nextSlide, intervalTime);
</script>
</body>
</html>
"""
components.html(carousel_html, height=600, scrolling=False)
st.markdown("<br><br><br>", unsafe_allow_html=True)


# ============================================================================
# SECCIÓN DE GESTIÓN DE PROYECTOS
# ============================================================================
col_proj_text, col_proj_img = st.columns([1, 1.2], gap="large", vertical_alignment="center")

with col_proj_text:
    st.markdown("""
    <div style="padding: 2rem 0;">
        <h2 style="font-family: 'Poppins', sans-serif; font-size: 2.8rem; font-weight: 700; line-height: 1.2; color: #1E293B; margin: 0 0 1rem 0;">
            Accede al manejo de postes, gestiona tu VGT por proyectos.
        </h2>
        <p style="font-size: 1.3rem; font-weight: 600; color: #6366F1; margin-bottom: 0.8rem;">
            Hecha para minimizar tus pérdidas
        </p>
        <p style="font-size: 1.1rem; color: #64748B; line-height: 1.6;">
            Unifica tu data, observa todos los postes que usas en un solo lugar
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_proj_img:
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="{img_proyectos}" alt="Dashboard de Proyectos VGT" style="max-width: 100%; border-radius: 16px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);">
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# ============================================================================
# PROBLEM SECTION (DARK REDESIGN)
# ============================================================================
st.markdown("""
<div id="problematicas" style="position: relative; width: 100vw; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; background-color: #1E293B; padding-top: 4rem; padding-bottom: 4rem; margin-top: 2rem; margin-bottom: 4rem; color: #FFFFFF;">
<div style="max-width: 1200px; margin: 0 auto; padding: 0 1rem;">
<!-- Header dentro del contenedor oscuro -->
<div style="text-align: center; margin-bottom: 3rem;">
<h2 style="font-family: 'Poppins', sans-serif; font-size: 2.5rem; font-weight: 700; color: #FFFFFF; margin: 0 0 0.5rem 0;">
El Desorden Cuesta Dólares
</h2>
<p style="font-size: 1.1rem; color: #94A3B8; margin: 0;">
Identifica si tu ISP sufre de estos síntomas comunes
</p>
</div>
<!-- Grid de tarjetas (Flexbox para asegurar uniformidad) -->
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem;">
<!-- Card 1 -->
<div style="flex: 1; min-width: 280px; text-align: center; padding: 1rem;">
<div style="margin-bottom: 1.5rem; display: flex; justify-content: center;">
<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="6" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><line x1="20" y1="4" x2="8.12" y2="15.88"></line><line x1="14.47" y1="14.48" x2="20" y2="20"></line><line x1="8.12" y1="8.12" x2="12" y2="12"></line>
</svg>
</div>
<h3 style="font-family: 'Poppins', sans-serif; font-size: 1.5rem; font-weight: 700; color: #6C63FF; margin-bottom: 1rem;">
Cortes<br>Imprevistos
</h3>
<p style="font-size: 1rem; color: #E2E8F0; line-height: 1.6;">
Cada corte es una emergencia. Pierdes horas buscando el punto de falla y clientes molestos cancelan el servicio.
</p>
</div>
<!-- Card 2 -->
<div style="flex: 1; min-width: 280px; text-align: center; padding: 1rem;">
<div style="margin-bottom: 1.5rem; display: flex; justify-content: center;">
<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline>
</svg>
</div>
<h3 style="font-family: 'Poppins', sans-serif; font-size: 1.5rem; font-weight: 700; color: #6C63FF; margin-bottom: 1rem;">
Multas<br>Regulatorias
</h3>
<p style="font-size: 1rem; color: #E2E8F0; line-height: 1.6;">
Los entes reguladores exigen documentación al día. Una multa por falta de VGTs puede superar los <strong>$3,000</strong>.
</p>
</div>
<!-- Card 3 -->
<div style="flex: 1; min-width: 280px; text-align: center; padding: 1rem;">
<div style="margin-bottom: 1.5rem; display: flex; justify-content: center;">
<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line>
</svg>
</div>
<h3 style="font-family: 'Poppins', sans-serif; font-size: 1.5rem; font-weight: 700; color: #6C63FF; margin-bottom: 1rem;">
Inventario<br>Ciego
</h3>
<p style="font-size: 1rem; color: #E2E8F0; line-height: 1.6;">
¿Sabes exactamente cuántos postes usas? ¿Sabes donde se ubican? Sin datos precisos, podrías estar pagando de más o arriesgándote a cortes.
</p>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# ============================================================================
# SECCIÓN DE VENTAJAS CLAVE
# ============================================================================
col_vent_text, col_vent_img = st.columns([1, 1.3], gap="large", vertical_alignment="center")

with col_vent_text:
    st.markdown("""
    <div style="padding: 2rem 0;">
        <h2 style="font-family: 'Poppins', sans-serif; font-size: 2.2rem; font-weight: 700; line-height: 1.2; color: #1E293B; margin: 0 0 1.5rem 0;">
            Algunas ventajas clave de nuestra solución:
        </h2>
        <div style="font-size: 1.15rem; color: #475569; line-height: 1.6;">
            <div style="display: flex; align-items: start; margin-bottom: 0.8rem;">
                <div style="flex-shrink: 0; margin-right: 12px; margin-top: 4px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
                <div>Visualización geoespacial de proyectos en mapas interactivos en tiempo real</div>
            </div>
            <div style="display: flex; align-items: start; margin-bottom: 0.8rem;">
                <div style="flex-shrink: 0; margin-right: 12px; margin-top: 4px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
                <div>Sincronización entre la App Móvil y la Web App</div>
            </div>
            <div style="display: flex; align-items: start; margin-bottom: 0.8rem;">
                <div style="flex-shrink: 0; margin-right: 12px; margin-top: 4px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
                <div>Control detallado y centralizado de la infraestructura de telecomunicaciones</div>
            </div>
            <div style="display: flex; align-items: start; margin-bottom: 0.8rem;">
                <div style="flex-shrink: 0; margin-right: 12px; margin-top: 4px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
                <div>Persistencia de datos garantizada para el resguardo de información crítica</div>
            </div>
            <div style="display: flex; align-items: start; margin-bottom: 0.8rem;">
                <div style="flex-shrink: 0; margin-right: 12px; margin-top: 4px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
                <div>Panel para el control de pagos de tu VGT</div>
            </div>
            <div style="display: flex; align-items: start; margin-bottom: 0.8rem;">
                <div style="flex-shrink: 0; margin-right: 12px; margin-top: 4px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
                <div>Asistencia personalizada para la gestión de tu información</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_vent_img:
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="{img_ventajas}" alt="Ventajas de VGT Nexus" style="max-width: 120%; border-radius: 16px;">
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PRICING SECTION
# ============================================================================
st.markdown("""
<div id="precios"></div>
<div class="section-header">
    <span class="section-header-pill">Precios</span>
    <h2>Planes Flexibles</h2>
    <p>Escala según el tamaño de tu red. Sin contratos forzosos.</p>
</div>
""", unsafe_allow_html=True)

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
    <div style="text-align: center; margin-top: 2rem; font-size: 0.85rem; color: #7E84A3;">
        © 2026 VGT Nexus. Todos los derechos reservados.<br>
        Desarrollado por Miguel Esteller
    </div>
</div>
""", unsafe_allow_html=True)