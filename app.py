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
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {display: none !important;}
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
        text-decoration: none !important;
        cursor: pointer;
        letter-spacing: -0.5px;
    }
    
    .nav-logo:hover, .nav-logo:visited, .nav-logo:active, .nav-logo:focus {
        text-decoration: none !important;
        color: #F8FAFC !important;
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
    .pricing-card {
        background: white;
        border-radius: 20px;
        padding: 1.5rem 1rem;
        border: 1px solid #F1F5F9;
        transition: all 0.3s ease;
        height: 100%;
        min-height: 380px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    .pricing-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 20px -5px rgba(0, 0, 0, 0.1), 0 8px 8px -5px rgba(0, 0, 0, 0.04);
    }
    
    /* POPULAR CARD (Purple Gradient) */
    .pricing-card.popular {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
        border: none;
        color: white;
        box-shadow: 0 20px 40px -10px rgba(99, 102, 241, 0.4);
        transform: scale(1.02);
        z-index: 10;
        min-height: 400px;
    }
    .pricing-card.popular:hover {
        transform: scale(1.04) translateY(-3px);
    }

    /* DARK CARD - Kept for legacy */
    .pricing-card.dark-card {
        background: #1E293B;
        border: none;
        color: white;
        box-shadow: 0 20px 40px -10px rgba(30, 41, 59, 0.5);
    }
    
    .pricing-header { text-align: center; margin-bottom: 1rem; }
    .pricing-header h3 { font-size: 1.35rem; font-weight: 800; margin-bottom: 0.2rem; letter-spacing: -0.5px; }
    .pricing-header p { font-size: 0.8rem; font-weight: 500; color: #94A3B8; margin: 0; }
    .popular .pricing-header h3 { color: white !important; }
    .popular .pricing-header p { color: #E0E7FF !important; }
    .dark-card .pricing-header p { color: #94A3B8; }
    
    .pricing-price { font-size: 2.5rem; font-weight: 800; color: #1E293B; margin: 0 0 1.2rem 0; line-height: 1; text-align: center; }
    .pricing-price span { font-size: 0.9rem; font-weight: 500; color: #94A3B8; margin-left: 3px; }
    .popular .pricing-price { color: white; }
    .popular .pricing-price span { color: #E0E7FF; }
    .dark-card .pricing-price { color: white; }
    .dark-card .pricing-price span { color: #94A3B8; }
    
    .pricing-features { list-style: none; padding: 0; margin: 0 0 1.5rem 0; flex-grow: 1; }
    .pricing-features li {
        padding: 0.5rem 0;
        color: #475569;
        font-size: 0.85rem;
        display: flex;
        align-items: center;
        border-bottom: 1px solid transparent; 
    }
    
    .popular .pricing-features li { color: #F8FAFC; border-color: rgba(255,255,255,0.1); }
    .dark-card .pricing-features li { color: #E2E8F0; }
    
    .feature-icon {
        flex-shrink: 0;
        width: 16px;
        height: 16px;
        margin-right: 8px;
        color: #6366F1;
    }
    .popular .feature-icon { color: #ffffff !important; }
    .dark-card .feature-icon { color: #94A3B8; }
    
    /* BUTTONS */
    .btn-pricing {
        display: block; width: 100%; padding: 0.75rem; text-align: center; border-radius: 50px;
        font-weight: 700; text-decoration: none; transition: all 0.2s; font-size: 0.9rem;
    }
    
    .btn-outline {
        background: transparent; border: 2px solid #E2E8F0; color: #6366F1 !important;
    }
    .btn-outline:hover {
        border-color: #6366F1; background: #EEF2FF;
    }
    
    .btn-primary-white {
        background: white; color: #6366F1 !important; box-shadow: 0 8px 15px -5px rgba(0, 0, 0, 0.2);
    }
    .btn-primary-white:hover {
        background: #F8FAFC; transform: translateY(-2px); box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.3);
    }
    
    .btn-outline-white {
        background: transparent; border: 2px solid #475569; color: white !important;
    }
    .btn-outline-white:hover {
        border-color: white; background: rgba(255,255,255,0.05);
    }
    
    /* Popular Tag */
    .popular-tag {
        background: white; color: #6366F1; padding: 4px 12px; border-radius: 4px;
        font-size: 0.7rem; font-weight: 800; position: absolute; top: -12px; left: 50%;
        transform: translateX(-50%); text-transform: uppercase; letter-spacing: 0.5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    /* Free Trial Banner V2 */
    .free-trial-banner {
        background: #E0E7FF; border-radius: 12px; padding: 1rem 2rem; text-align: center;
        max-width: 800px; margin: 0 auto 4rem auto;
        display: flex; align-items: center; justify-content: center; gap: 1rem;
        color: #3730A3; font-weight: 500; font-size: 1.1rem;
    }

    /* EXTIPRAS SECTION REDESIGN */
    .extras-container {
        display: flex;
        gap: 24px;
        justify-content: center;
        margin-top: 3rem;
        flex-wrap: wrap;
    }

    .extra-card {
        background: white;
        border: 1px solid #F1F5F9;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.15);
        flex: 1;
        min-width: 320px;
        max-width: 500px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .extra-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 30px -10px rgba(99, 102, 241, 0.2);
        border-color: #E0E7FF;
    }

    .extra-left {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }

    /* FOOTER STYLES */
    .footer-cta-section {
        background-color: #0F172A;
        padding: 3rem 2rem;
        text-align: left;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1.5rem;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
    }
    .footer-cta-content { max-width: 600px; }
    .footer-cta-content h2 { font-size: 2rem; font-weight: 800; margin-bottom: 1rem; color: white !important; }
    .footer-cta-content p { font-size: 1.1rem; color: #94A3B8; margin-bottom: 2rem; line-height: 1.6; }
    .btn-cta-footer {
        background: #10B981; color: white !important; padding: 0.8rem 2rem; border-radius: 50px;
        font-weight: 700; text-decoration: none; transition: all 0.2s; display: inline-block;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }
    .btn-cta-footer:hover { background: #059669; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5); }

    .main-footer {
        background-color: #020617;
        padding: 2.5rem 2rem;
        color: white;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 2rem;
        border-bottom: 1px solid #1E293B;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
    }
    .footer-col { flex: 1; min-width: 200px; text-align: left; }
    .footer-col h4 { color: white; font-size: 0.95rem; font-weight: 700; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.5px; margin-left: 0; }
    .footer-links { list-style: none !important; padding: 0 !important; margin: 0 !important; padding-left: 0 !important; }
    .footer-links li { margin-bottom: 0.8rem; padding: 0 !important; margin-left: 0 !important; }
    .footer-links a { color: #94A3B8; text-decoration: none; font-size: 0.95rem; transition: color 0.2s; display: flex; align-items: center; gap: 8px; justify-content: flex-start; }
    .footer-links a:hover { color: white; }

    .platform-bar {
        background-color: #020617;
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #1E293B;
        color: white;
        flex-wrap: wrap;
        gap: 1rem;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
    }
    .platform-icons { display: flex; gap: 2rem; align-items: center; }
    .platform-item { display: flex; align-items: center; gap: 8px; color: #CBD5E1; font-weight: 500; font-size: 0.9rem; }
    
    .copyright-bar {
        background-color: #020617;
        padding: 1.5rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #64748B;
        font-size: 0.85rem;
        flex-wrap: wrap;
        gap: 1rem;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        padding-bottom: 2rem;
        margin-bottom: 0;
    }
    
    div[data-testid="stAppViewContainer"] > section:first-child > div:first-child {
        padding-bottom: 0rem !important;
    }

    .social-icons { display: flex; gap: 1.5rem; }
    .social-icons a { color: #94A3B8; transition: color 0.2s; }
    .social-icons a:hover { color: white; }


    .extra-icon-box {
        color: #6366F1;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .extra-icon-svg {
        width: 32px;
        height: 32px;
        stroke-width: 2;
    }

    .extra-title {
        font-size: 1.25rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.2;
        letter-spacing: -0.5px;
    }

    .extra-subtitle {
        font-size: 0.85rem;
        color: #64748B;
        font-weight: 500;
    }

    .extra-right {
        text-align: right;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: center;
        padding-left: 20px;
    }

    .extra-price {
        font-size: 2rem;
        font-weight: 800;
        color: #6366F1;
        line-height: 1;
    }
    
    .extra-price small {
        font-size: 1rem;
        font-weight: 600;
        color: #6366F1;
    }

    .extra-note {
        font-size: 0.75rem;
        color: #64748B;
        margin-top: 4px;
        font-weight: 500;
    }


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
    /* CONTACT FORM REDESIGN */
    /* CONTACT FORM REDESIGN */
    /* Container styling */
    div[data-testid="stForm"] {
        background: #FFFFFF;
        border-radius: 24px;
        padding: 3rem;
        box-shadow: 0 20px 40px -10px rgba(99, 102, 241, 0.1);
        border: 1px solid #F1F5F9;
    }
    
    /* INPUT FIELDS - Targeting by data-baseweb attribute which is more stable */
    div[data-baseweb="input"] > div, 
    div[data-baseweb="base-input"],
    textarea,
    div[data-baseweb="select"] > div {
        background-color: #F8FAFC !important;
        border: 2px solid #E2E8F0 !important;
        border-radius: 12px !important;
        color: #1E293B !important;
    }
    
    /* Input Text Color */
    input[type="text"], textarea {
        color: #1E293B !important;
    }

    /* Focus State */
    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within,
    textarea:focus {
        border-color: #6366F1 !important;
        background-color: #FFFFFF !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* LABELS */
    label[data-testid="stLabel"] {
        color: #1E293B !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.4rem !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* SUBMIT BUTTON */
    div[data-testid="stForm"] button {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 0.8rem 0 !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        width: 100% !important;
        transition: all 0.2s !important;
        box-shadow: 0 10px 20px -5px rgba(79, 70, 229, 0.3) !important;
        margin-top: 1rem !important;
        height: auto !important;
    }
    
    div[data-testid="stForm"] button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 25px -5px rgba(79, 70, 229, 0.4) !important;
        color: white !important;
        border-color: transparent !important;
    }
    
    div[data-testid="stForm"] button:active {
        transform: translateY(0) !important;
    }
    
    /* Hide the form container padding hack I added earlier since we are styling the form directly */
    .contact-form-container {
        display: none;
    }
    
    /* Hide Streamlit anchor link icons on headings */
    a.anchor-link, 
    .streamlit-expanderHeader a,
    h1 a, h2 a, h3 a, h4 a, h5 a, h6 a,
    [data-testid="stHeaderActionElements"],
    .header-link-container {
        display: none !important;
        visibility: hidden !important;
    }

</style>
""", unsafe_allow_html=True)

# ============================================================================
# NAVIGATION BAR
# ============================================================================
st.markdown("""
<div class="nav-container">
    <a href="javascript:void(0)" onclick="var container = window.parent.document.querySelector('[data-testid=\'stAppViewContainer\']'); if(container) { container.scrollTo({top: 0, behavior: 'smooth'}); } else { window.scrollTo({top: 0, behavior: 'smooth'}); }" class="nav-logo">
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
        .carousel-container {{ position: relative; width: 100%; height: 580px; overflow: hidden; }}
        
        .slide {{
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            opacity: 0; transition: opacity 1s ease-in-out;
            display: flex; align-items: center; justify-content: center;
            padding: 0 2rem; box-sizing: border-box; pointer-events: none;
        }}
        .slide.active {{ opacity: 1; pointer-events: auto; z-index: 2; }}
        
        .slide-content {{
            display: flex; align-items: center; justify-content: space-between;
            width: 100%; max-width: 1200px; margin: 0 auto; gap: 1rem;
        }}
        
        .slide-text {{ flex: 1; padding-right: 1rem; text-align: left; }}
        
        .slide-image {{ flex: 1.5; display: flex; justify-content: center; align-items: center; }}
        .slide-image img {{
            max-width: 130%; max-height: 550px; height: auto;
            object-fit: contain; filter: drop-shadow(0 10px 20px rgba(0,0,0,0.15));
        }}
        
        .hero-tag {{ display: inline-block; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px; color: #6366F1; margin-bottom: 0.8rem; text-transform: uppercase; }}
        .hero-title {{ font-family: 'Poppins', sans-serif; font-size: 3.2rem; font-weight: 700; line-height: 1.1; color: #1E293B; margin: 0 0 1.2rem 0; letter-spacing: -1px; }}
        .hero-subtitle {{ font-size: 1.05rem; color: #64748B; line-height: 1.5; margin-bottom: 1.8rem; max-width: 95%; }}
        
        .btn-hero {{
            display: inline-block; background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
            color: white; padding: 1rem 2.5rem; border-radius: 50px;
            text-decoration: none; font-weight: 600; font-size: 1.1rem;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.4);
        }}
        .btn-hero:hover {{ transform: translateY(-2px); box-shadow: 0 15px 30px -5px rgba(99, 102, 241, 0.5); }}
        
        .carousel-dots {{ position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); display: flex; gap: 12px; z-index: 10; }}
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
                    <a href="javascript:void(0)" class="btn-hero" onclick="goToPrices()">Optimiza tu VGT ahora</a>
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
                    <a href="javascript:void(0)" class="btn-hero" onclick="goToPrices()">Optimiza tu VGT ahora</a>
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
                    <a href="javascript:void(0)" class="btn-hero" onclick="goToPrices()">Optimiza tu VGT ahora</a>
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

    function goToPrices() {{
        try {{
            window.parent.document.getElementById('precios').scrollIntoView({{behavior: 'smooth'}});
        }} catch(e) {{
            window.parent.location.assign('#precios');
        }}
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
<div id="problematicas" style="position: relative; width: 100vw; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; background-color: #1E293B; padding-top: 4rem; padding-bottom: 4rem; margin-top: 2rem; margin-bottom: 1rem; color: #FFFFFF;">
<div style="max-width: 1200px; margin: 0 auto; padding: 0 1rem;">
<!-- Header dentro del contenedor oscuro -->
<div style="text-align: center; margin-bottom: 3rem;">
<h2 style="font-family: 'Poppins', sans-serif; font-size: 2.5rem; font-weight: 700; color: #FFFFFF; margin: 0 0 0.5rem 0;">
El desorden cuesta dinero
</h2>
<p style="font-size: 1.1rem; color: #94A3B8; margin: 0;">
Identifica si tu ISP sufre de estos síntomas comunes
</p>
</div>
<!-- Grid de tarjetas (Flexbox para asegurar uniformidad) -->
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem;">
<!-- Card 1 -->
<div style="flex: 1; min-width: 280px; text-align: center; padding: 1rem; display: flex; flex-direction: column; align-items: center; justify-content: flex-start;">
<div style="margin-bottom: 1.5rem; display: flex; justify-content: center;">
<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="6" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><line x1="20" y1="4" x2="8.12" y2="15.88"></line><line x1="14.47" y1="14.48" x2="20" y2="20"></line><line x1="8.12" y1="8.12" x2="12" y2="12"></line>
</svg>
</div>
<h3 style="font-family: 'Poppins', sans-serif; font-size: 1.5rem; font-weight: 700; color: #6C63FF; margin-bottom: 1rem; width: 100%; text-align: center;">
<span style="display: block;">Cortes</span><span style="display: block;">Imprevistos</span>
</h3>
<p style="font-size: 1rem; color: #E2E8F0; line-height: 1.6; max-width: 320px; margin: 0 auto; width: 100%; text-align: center;">
Cada corte es una emergencia. Pierdes horas buscando el punto de falla y clientes molestos cancelan el servicio.
</p>
</div>
<!-- Card 2 -->
<div style="flex: 1; min-width: 280px; text-align: center; padding: 1rem; display: flex; flex-direction: column; align-items: center; justify-content: flex-start;">
<div style="margin-bottom: 1.5rem; display: flex; justify-content: center;">
<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline>
</svg>
</div>
<h3 style="font-family: 'Poppins', sans-serif; font-size: 1.5rem; font-weight: 700; color: #6C63FF; margin-bottom: 1rem; width: 100%; text-align: center;">
<span style="display: block;">Multas</span><span style="display: block;">Regulatorias</span>
</h3>
<p style="font-size: 1rem; color: #E2E8F0; line-height: 1.6; max-width: 320px; margin: 0 auto; width: 100%; text-align: center;">
Los entes reguladores exigen documentación al día. Una multa por falta de VGTs puede superar los <strong>$3,000</strong>.
</p>
</div>
<!-- Card 3 -->
<div style="flex: 1; min-width: 280px; text-align: center; padding: 1rem; display: flex; flex-direction: column; align-items: center; justify-content: flex-start;">
<div style="margin-bottom: 1.5rem; display: flex; justify-content: center;">
<svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#6C63FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line>
</svg>
</div>
<h3 style="font-family: 'Poppins', sans-serif; font-size: 1.5rem; font-weight: 700; color: #6C63FF; margin-bottom: 1rem; width: 100%; text-align: center;">
<span style="display: block;">Inventario</span><span style="display: block;">Ciego</span>
</h3>
<p style="font-size: 1rem; color: #E2E8F0; line-height: 1.6; max-width: 320px; margin: 0 auto; width: 100%; text-align: center;">
¿Sabes exactamente cuántos postes usas? ¿Sabes dónde se ubican? Sin datos precisos, podrías estar pagando de más o arriesgándote a cortes.
</p>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

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
# VIDEO DEMO SECTION
# ============================================================================
st.markdown("""
<div id="video-demo" style="text-align: center; margin-top: 4rem; margin-bottom: 4rem;">
    <h2 style="font-family: 'Poppins', sans-serif; font-size: 2.5rem; font-weight: 700; color: #1E293B; margin-bottom: 2rem;">
        Conoce Vista Nexus en Acción
    </h2>
</div>
""", unsafe_allow_html=True)

col_video_1, col_video_2, col_video_3 = st.columns([1, 3, 1])
with col_video_2:
    st.video("VIDEO_DEMO.mp4")

st.markdown("<br><br><br>", unsafe_allow_html=True)

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
<div class="free-trial-banner">
    <span style="font-size: 1.25rem;">🎁</span> 
    <span>Prueba <strong>GRATIS</strong> por 1 Semana - Sin compromiso</span>
</div>
""", unsafe_allow_html=True)


# Checkmark Icon SVG
check_icon = """<svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>"""
# Checkmark Icon SVG (Light for Dark Card)
check_icon_light = """<svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="#94A3B8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>"""
# Checkmark Icon SVG (White for Popular Card)
check_icon_white = """<svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>"""


col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown(f"""
    <div class="pricing-card">
        <div class="pricing-header">
            <h3>Arranque</h3>
            <p>Pequeños ISPs</p>
        </div>
        <div class="pricing-price">$87.99<span>/mes</span></div>
        <ul class="pricing-features">
            <li>{check_icon} Hasta 500 postes</li>
            <li>{check_icon} Gestión básica</li>
            <li>{check_icon} App Móvil</li>
            <li>{check_icon} Soporte Email</li>
        </ul>
        <a href="#contacto" class="btn-pricing btn-outline">Elegir Plan</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="pricing-card popular" style="position: relative;">
        <div class="popular-tag">MÁS POPULAR</div>
        <div class="pricing-header">
            <h3>Expansión</h3>
            <p>Crecimiento acelerado</p>
        </div>
        <div class="pricing-price">$169.97<span>/mes</span></div>
        <ul class="pricing-features">
            <li>{check_icon_white} Hasta 1,000 postes</li>
            <li>{check_icon_white} Onboarding Asistido</li>
            <li>{check_icon_white} App Móvil Ilimitada</li>
            <li>{check_icon_white} Reportes PDF Avanzados</li>
            <li>{check_icon_white} Soporte Prioritario</li>
        </ul>
        <a href="#contacto" class="btn-pricing btn-primary-white">Elegir Plan</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="pricing-card">
        <div class="pricing-header">
            <h3>Enterprise</h3>
            <p>Grandes Redes</p>
        </div>
        <div class="pricing-price">A Medida</div>
        <ul class="pricing-features">
            <li>{check_icon} Postes Ilimitados</li>
            <li>{check_icon} Integración API</li>
            <li>{check_icon} Auditoría Masiva</li>
            <li>{check_icon} Gerente de Cuenta</li>
        </ul>
        <a href="#contacto" class="btn-pricing btn-outline">Contactar Ventas</a>
    </div>
    """, unsafe_allow_html=True)

# Icons for Extras
lightning_icon = """<svg class="extra-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>"""
pole_icon = """<svg class="extra-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"></path><path d="M8 6h8"></path><path d="M8 10h8"></path><path d="M7 19h10"></path></svg>"""

st.markdown(f"""
<div class="extras-container">
    <div class="extra-card">
        <div class="extra-left">
            <div class="extra-icon-box">{lightning_icon}</div>
            <div class="extra-title">Configuración<br>Inicial</div>
            <div class="extra-subtitle">Válido para plan Arranque</div>
        </div>
        <div class="extra-right">
            <div class="extra-price">$70</div>
            <div class="extra-note">(Pago único inicial)</div>
        </div>
    </div>
    <div class="extra-card">
        <div class="extra-left">
            <div class="extra-icon-box">{pole_icon}</div>
            <div class="extra-title">+100 Postes<br>Adicionales</div>
            <div class="extra-subtitle">Para cualquier plan</div>
        </div>
        <div class="extra-right">
            <div class="extra-price">$20<small>/mes</small></div>
            <div class="extra-note">(Costo por excedente)</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================================
# CONTACT FORM
# ============================================================================
st.markdown('<div id="contacto"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section-header" style="padding-top: 5rem; margin-bottom: 0rem;">
    <span class="section-header-pill">Contacto</span>
    <h2>Solicita tu Demo</h2>
    <p style="margin-bottom: 0px;">Déjanos tus datos y te contactaremos a la brevedad.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with st.container():
        st.markdown('<div class="contact-form-container">', unsafe_allow_html=True)
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
            submitted = st.form_submit_button("Enviar Solicitud", use_container_width=True)
            
            if submitted:
                st.success("¡Recibido! Nos pondremos en contacto contigo pronto.")
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
# Icons (Simple SVGs)
icon_apple = """<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.75 3C17.75 3 15.75 3 13.9 4.3C12 5.6 11.5 8 11.5 8C11.5 8 8.8 8.1 7.2 10.7C5.6 13.3 6.9 17.5 6.9 17.5C6.9 17.5 7.8 19.3 9.4 19.3C11 19.3 11.4 18.2 13.3 18.2C15.2 18.2 15.6 19.3 17.3 19.3C19 19.3 20 17.4 20 17.4C20 17.4 21.6 14.7 21.6 12.3C21.6 9.9 19.9 8.6 19.9 8.6C19.9 8.6 18.8 8.1 17.9 8.1C17 8.1 16 8.8 16 8.8C16 8.8 15 9.4 14 9.4C13 9.4 12.4 8.6 12.4 7.6C12.4 6.6 13.2 5.5 14.5 4.9C15.8 4.3 17.75 3 17.75 3Z"></path></svg>"""
icon_android = """<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 18.2h-11c-0.8 0-1.5-0.7-1.5-1.5v-7.5h14v7.5c0 0.8-0.7 1.5-1.5 1.5z M6.8 7.4h10.4l-1.9-3.3c-0.1-0.2-0.1-0.5 0.1-0.6 0.2-0.2 0.5-0.1 0.6 0.1l2 3.4h0.2c0.3 0 0.6 0.3 0.6 0.6v0.8h-12.8v-0.8c0-0.3 0.3-0.6 0.6-0.6h0.2l2-3.4c0.1-0.2 0.4-0.3 0.6-0.1 0.2 0.1 0.2 0.4 0.1 0.6l-1.9 3.3z"></path></svg>"""
icon_windows = """<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M0 3.4L9.5 2.1V11.5H0V3.4ZM10.4 2V11.5H24V0.1L10.4 2ZM0 12.5H9.5V20.6L0 19.3V12.5ZM10.4 12.5V22L24 23.9V12.5H10.4Z"></path></svg>"""
icon_web = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>"""

st.markdown(f"""
<div class="footer-cta-section">
<div class="footer-cta-content" style="max-width: 1200px; margin: 0 auto; width: 100%; display: inherit; justify-content: inherit; align-items: inherit;">
<div style="flex: 1;">
<h2>Todo el poder de VGT Nexus está en tus manos.</h2>
<p>Desarrollamos potentes soluciones que impactan e impulsan el crecimiento sostenible de los Proveedores de Internet en América Latina.<br><br>
Impulsamos la transformación digital de las empresas de telecomunicaciones a través de nuestras herramientas de alta tecnología.</p>
</div>
<a href="#contacto" class="btn-cta-footer">Solicitar Demo de VGT Nexus</a>
</div>
</div>

<div class="main-footer">
<div style="max-width: 1200px; margin: 0 auto; width: 100%; display: flex; justify-content: space-between; gap: 3rem; flex-wrap: wrap;">
<div class="footer-col" style="flex: 1.5;">
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 2rem;">
<svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 6V22L8 18L16 22L23 18V2L16 6L8 2L1 6Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
<div style="line-height: 1;">
<div style="font-size: 1.5rem; font-weight: 800; color: white;">VGT NEXUS</div>
</div>
</div>
</div>

<div class="footer-col">
<h4>Contacto</h4>
<ul class="footer-links">
<li><a href="mailto:holavgtnexus@gmail.com">📧 holavgtnexus@gmail.com</a></li>
<li><a href="tel:+584127750980">📞 0412-7750980</a></li>
</ul>
</div>

<div class="footer-col">
<h4>Escríbanos</h4>
<ul class="footer-links">
<li><a href="https://linktr.ee/holavgtnexus" target="_blank">🔗 VGT Nexus Links</a></li>
</ul>
</div>
</div>
</div>

<div class="platform-bar">
<div style="max-width: 1200px; margin: 0 auto; width: 100%; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
<div style="font-weight: 700;">Disponible en plataformas</div>
<div class="platform-icons">
<div class="platform-item">{icon_web} Web</div>
<div class="platform-item">{icon_android} Android</div>
</div>
</div>
</div>

<div class="copyright-bar">
<div style="max-width: 1200px; margin: 0 auto; width: 100%; display: flex; justify-content: center; align-items: center;">
<div>VGT Nexus</div>
</div>
</div>
""", unsafe_allow_html=True)