import streamlit as st
import base64
from PIL import Image
import io
import qrcode
import os

# Configurações da página
st.set_page_config(
    page_title="Cartão Virtual",
    page_icon="📇",
    layout="centered"
)

# Cores do escritório
cor_principal = "#bc0a53"  # Rosa/Vermelho
cor_secundaria = "#4c4c4c"  # Cinza

# CSS personalizado
st.markdown(f"""
<style>
    .main {{
        background-color: white;
        padding: 0 !important;
    }}
    .block-container {{
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 45rem;
    }}
    .card-container {{
        background: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    .perfil-img {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid {cor_principal};
        margin: 0 auto;
        display: block;
    }}
    .nome-titulo {{
        color: {cor_secundaria};
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 0;
    }}
    .cargo-titulo {{
        color: {cor_principal};
        font-size: 16px;
        text-align: center;
        margin-top: 5px;
        font-weight: 500;
    }}
    .empresa-titulo {{
        color: {cor_secundaria};
        font-size: 14px;
        text-align: center;
        margin-top: 5px;
    }}
    .contato-card {{
        margin-top: 20px;
        border: 1px solid #eee;
        border-radius: 10px;
        padding: 10px;
        display: flex;
        align-items: center;
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }}
    .contato-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    .icon-box {{
        width: 40px;
        height: 40px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 15px;
        background-color: {cor_principal}30;
    }}
    .icon-box i {{
        color: {cor_principal};
        font-size: 20px;
    }}
    .contato-info {{
        flex-grow: 1;
    }}
    .contato-tipo {{
        font-size: 12px;
        color: #888;
        margin: 0;
    }}
    .contato-valor {{
        font-size: 14px;
        color: #333;
        margin: 0;
    }}
    .btn-salvar {{
        background-color: {cor_principal};
        color: white;
        border: none;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        width: 100%;
        margin-top: 20px;
        transition: all 0.3s ease;
    }}
    .btn-salvar:hover {{
        background-color: {cor_principal}dd;
        transform: translateY(-2px);
    }}
    .social-container {{
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 25px;
    }}
    .social-icon {{
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: {cor_principal};
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .social-icon:hover {{
        transform: scale(1.1);
    }}
    .social-icon i {{
        color: white;
        font-size: 20px;
    }}
    .logo-section {{
        text-align: center;
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #eee;
    }}
    .wavy-bg {{
        position: relative;
        height: 80px;
        overflow: hidden;
        margin-bottom: -40px;
    }}
    .wavy-bg svg {{
        position: absolute;
        bottom: 0;
        width: 100%;
    }}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# Função para gerar VCard
def gerar_vcard(nome, cargo, empresa, telefone, email, site, endereco):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{nome}
FN:{nome}
ORG:{empresa}
TITLE:{cargo}
TEL;TYPE=WORK,VOICE:{telefone}
EMAIL:{email}
URL:{site}
ADR;TYPE=WORK:;;{endereco}
END:VCARD
"""
    return vcard

# Função para criar QR Code com VCard
def gerar_qr_vcard(vcard_str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_str)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Converter imagem para bytes
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return buffered.getvalue()

# Função para criar URL download do VCard
def get_vcard_download_link(vcard_str, filename="contato.vcf"):
    b64_vcard = base64.b64encode(vcard_str.encode()).decode()
    href = f'<a href="data:text/vcard;base64,{b64_vcard}" download="{filename}" class="btn-salvar">SALVAR CONTATO</a>'
    return href

# Informações do profissional (edite com suas informações)
info = {
    "nome": "Seu Nome",
    "cargo": "Seu Cargo",
    "empresa": "Nome da Sua Empresa",
    "foto": "https://via.placeholder.com/150",  # Substitua pela URL da sua foto
    "telefone": "+55 11 99999-9999",
    "email": "seuemail@empresa.com.br",
    "site": "www.seusite.com.br",
    "endereco": "Sua Rua, 123 - Bairro - Cidade/UF",
    "instagram": "seu_instagram",
    "linkedin": "seu_linkedin",
    "twitter": "seu_twitter",
    "facebook": "seu_facebook",
    "whatsapp": "+5511999999999",  # Formato sem espaços ou caracteres especiais
    "logo": "https://via.placeholder.com/200x50"  # Substitua pela URL do logo da empresa
}

# Gerar string do VCard
vcard_str = gerar_vcard(
    info["nome"], 
    info["cargo"], 
    info["empresa"], 
    info["telefone"], 
    info["email"], 
    info["site"], 
    info["endereco"]
)

# Gerar QR Code do VCard
qr_code_image = gerar_qr_vcard(vcard_str)

# Interface do cartão de visitas
col1, col2, col3 = st.columns([1, 8, 1])

with col2:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    # Área curva superior
    st.markdown(f"""
    <div class="wavy-bg">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
            <path fill="{cor_principal}" fill-opacity="1" d="M0,64L60,80C120,96,240,128,360,138.7C480,149,600,139,720,122.7C840,107,960,85,1080,90.7C1200,96,1320,128,1380,144L1440,160L1440,0L1380,0C1320,0,1200,0,1080,0C960,0,840,0,720,0C600,0,480,0,360,0C240,0,120,0,60,0L0,0Z"></path>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    # Foto e informações básicas
    st.markdown(f'<img src="{info["foto"]}" class="perfil-img">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="nome-titulo">{info["nome"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="cargo-titulo">{info["cargo"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="empresa-titulo">{info["empresa"]}</p>', unsafe_allow_html=True)
    
    # Redes sociais
    st.markdown("""
    <div class="social-container">
        <a href="https://instagram.com/USUARIO" target="_blank" class="social-icon">
            <i class="fab fa-instagram"></i>
        </a>
        <a href="https://linkedin.com/in/USUARIO" target="_blank" class="social-icon">
            <i class="fab fa-linkedin-in"></i>
        </a>
        <a href="https://twitter.com/USUARIO" target="_blank" class="social-icon">
            <i class="fab fa-twitter"></i>
        </a>
        <a href="https://facebook.com/USUARIO" target="_blank" class="social-icon">
            <i class="fab fa-facebook-f"></i>
        </a>
    </div>
    """.replace("USUARIO", info["instagram"])
      .replace("USUARIO", info["linkedin"])
      .replace("USUARIO", info["twitter"])
      .replace("USUARIO", info["facebook"]), 
      unsafe_allow_html=True)
    
    # Informações de contato
    st.markdown("""
    <div class="contato-card">
        <div class="icon-box">
            <i class="fas fa-phone"></i>
        </div>
        <div class="contato-info">
            <p class="contato-tipo">Telefone</p>
            <p class="contato-valor">TELEFONE</p>
        </div>
    </div>
    """.replace("TELEFONE", info["telefone"]), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contato-card">
        <div class="icon-box">
            <i class="fas fa-envelope"></i>
        </div>
        <div class="contato-info">
            <p class="contato-tipo">E-mail</p>
            <p class="contato-valor">EMAIL</p>
        </div>
    </div>
    """.replace("EMAIL", info["email"]), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contato-card">
        <div class="icon-box">
            <i class="fas fa-globe"></i>
        </div>
        <div class="contato-info">
            <p class="contato-tipo">Site</p>
            <p class="contato-valor">SITE</p>
        </div>
    </div>
    """.replace("SITE", info["site"]), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contato-card">
        <div class="icon-box">
            <i class="fas fa-map-marker-alt"></i>
        </div>
        <div class="contato-info">
            <p class="contato-tipo">Endereço</p>
            <p class="contato-valor">ENDERECO</p>
        </div>
    </div>
    """.replace("ENDERECO", info["endereco"]), unsafe_allow_html=True)
    
    # QR Code
    col_btn, col_qr = st.columns([3, 1])
    
    with col_btn:
        # Botão para salvar contato (VCard download)
        st.markdown(get_vcard_download_link(vcard_str), unsafe_allow_html=True)
        
        # Link para WhatsApp
        st.markdown(f"""
        <a href="https://wa.me/{info['whatsapp']}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #25D366; color: white; border: none; padding: 12px 20px; 
            font-size: 16px; font-weight: bold; border-radius: 10px; cursor: pointer; width: 100%; 
            margin-top: 10px; display: flex; align-items: center; justify-content: center; gap: 10px;">
                <i class="fab fa-whatsapp"></i> WHATSAPP
            </button>
        </a>
        """, unsafe_allow_html=True)
    
    with col_qr:
        st.image(qr_code_image, width=100)
    
    # Logo da empresa
    st.markdown(f"""
    <div class="logo-section">
        <img src="{info['logo']}" style="max-width: 150px; max-height: 50px;">
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Rodapé
st.markdown("""
<div style="text-align: center; margin-top: 30px; color: #888; font-size: 12px;">
    © 2025 Todos os direitos reservados
</div>
""", unsafe_allow_html=True)
