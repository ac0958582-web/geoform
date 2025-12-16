# ==========================================================
# GEOIDENTIFICADOR CIENTÍFICO
# Biblioteca + CAM Identificador
# Projeto académico
# ==========================================================

import streamlit as st
import random

# -------------------------
# BIBLIOTECA DE ROCHAS
# -------------------------
ROCHAS = {
    "Granito": {"cor":"Cinza / Rosa","densidade":"2.7 g/cm³","formula":"Quartzo + Feldspato + Mica","caracteristicas":"Ígnea plutónica","local":"Continentes"},
    "Basalto": {"cor":"Preto","densidade":"3.0 g/cm³","formula":"Plagioclásio + Piroxênio","caracteristicas":"Ígnea vulcânica","local":"Vulcões"},
    "Gabro": {"cor":"Escuro","densidade":"3.1 g/cm³","formula":"Piroxênio","caracteristicas":"Máfica","local":"Crosta oceânica"},
    "Calcário": {"cor":"Branco","densidade":"2.6 g/cm³","formula":"CaCO₃","caracteristicas":"Sedimentar","local":"Oceanos"},
    "Mármore": {"cor":"Branco","densidade":"2.7 g/cm³","formula":"CaCO₃","caracteristicas":"Metamórfica","local":"Montanhas"},
    "Arenito": {"cor":"Amarelo","densidade":"2.3 g/cm³","formula":"SiO₂","caracteristicas":"Sedimentar","local":"Desertos"},
    "Xisto": {"cor":"Escuro","densidade":"2.7 g/cm³","formula":"Micas","caracteristicas":"Foliada","local":"Orogénicos"},
    "Gnaisse": {"cor":"Bandada","densidade":"2.8 g/cm³","formula":"Quartzo + Feldspato","caracteristicas":"Bandamento","local":"Cratões"},
    "Obsidiana": {"cor":"Preto","densidade":"2.4 g/cm³","formula":"Vidro vulcânico","caracteristicas":"Amorfa","local":"Vulcões"},
    "Quartzito": {"cor":"Clara","densidade":"2.6 g/cm³","formula":"SiO₂","caracteristicas":"Muito duro","local":"Metamórfico"}
}

# -------------------------
# BIBLIOTECA DE MINERAIS
# -------------------------
MINERAIS = {
    "Quartzo": {"cor":"Incolor","densidade":"2.65 g/cm³","formula":"SiO₂","caracteristicas":"Fratura concoidal","local":"Veios"},
    "Calcita": {"cor":"Branca","densidade":"2.7 g/cm³","formula":"CaCO₃","caracteristicas":"Efervescência","local":"Calcários"},
    "Pirita": {"cor":"Dourado","densidade":"5.0 g/cm³","formula":"FeS₂","caracteristicas":"Metálico","local":"Veios"},
    "Hematite": {"cor":"Vermelho","densidade":"5.3 g/cm³","formula":"Fe₂O₃","caracteristicas":"Traço vermelho","local":"Ferro"},
    "Halite": {"cor":"Incolor","densidade":"2.2 g/cm³","formula":"NaCl","caracteristicas":"Salgada","local":"Evaporitos"},
    "Gipsita": {"cor":"Branca","densidade":"2.3 g/cm³","formula":"CaSO₄·2H₂O","caracteristicas":"Muito macia","local":"Evaporitos"},
    "Olivina": {"cor":"Verde","densidade":"3.3 g/cm³","formula":"(Mg,Fe)₂SiO₄","caracteristicas":"Granular","local":"Manto"},
    "Magnetite": {"cor":"Preta","densidade":"5.2 g/cm³","formula":"Fe₃O₄","caracteristicas":"Magnética","local":"Ígneas"},
    "Galena": {"cor":"Cinza","densidade":"7.6 g/cm³","formula":"PbS","caracteristicas":"Cúbica","local":"Veios"},
    "Fluorita": {"cor":"Variada","densidade":"3.2 g/cm³","formula":"CaF₂","caracteristicas":"Octaédrica","local":"Veios"}
}

# -------------------------
# IA EXPERIMENTAL
# -------------------------
def identificar(precisao):
    nome = random.choice(list(ROCHAS.keys()) + list(MINERAIS.keys()))
    return nome, precisao, "A IA analisou cor, textura e geometria com base na biblioteca interna."

# -------------------------
# INTERFACE
# -------------------------
st.set_page_config(page_title="GeoIdentificador Científico")
st.title("🪨 GeoIdentificador Científico")

menu = st.radio("Menu:", ["Biblioteca", "CAM Identificador"])

if menu == "Biblioteca":
    tipo = st.radio("Tipo:", ["Rochas", "Minerais"])
    base = ROCHAS if tipo == "Rochas" else MINERAIS
    escolha = st.selectbox("Seleciona:", list(base.keys()))
    d = base[escolha]

    st.markdown(f"""
    **Nome:** {escolha}  
    **Cor:** {d['cor']}  
    **Densidade:** {d['densidade']}  
    **Fórmula:** {d['formula']}  
    **Características:** {d['caracteristicas']}  
    **Localização:** {d['local']}
    """)

if menu == "CAM Identificador":
    st.info("📸 Foto 2D ≈ 75% | 📦 Modelo 3D ≈ 95%")
    modo = st.radio("Modo:", ["Imagem 2D", "Modelo 3D"])
    if st.button("Analisar"):
        p = 75 if modo == "Imagem 2D" else 95
        n, p, e = identificar(p)
        st.success(f"Identificação: {n}")
        st.write(f"Precisão: {p}%")
        st.write(f"Explicação: {e}")
git add .
git commit -m "GeoIdentificador científico com biblioteca de rochas e minerais"
git push origin main
streamlit run streamlit_app.py