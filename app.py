import streamlit as st
import time
import streamlit.components.v1 as components

# Configurações da Página
st.set_page_config(page_title="Exame Física UEM 2025", layout="centered")

# Função de Captura de Tela (JavaScript para disparar a impressão/PDF do navegador)
def screenshot_button():
    if st.button("📸 CAPTURAR RESULTADOS (PRINT/PDF)", use_container_width=True, type="primary"):
        components.html("<script>window.print();</script>", height=0)

# -------------------------------
# BANCO DE QUESTÕES
# -------------------------------
TEMPO_QUESTAO_MAX = 60
TEMPO_TOTAL_MAX = 90 * 60 

if "perguntas" not in st.session_state:
    st.session_state.perguntas = [
        {"pergunta": "40) Um recipiente com água é colocado sobre um fogão aceso. O aquecimento da água ocorre principalmente por:", "opcoes": ["A) Condução", "B) Irradiação", "C) Convecção", "D) Radiação", "E) Evaporação"], "correta": "C"},
        {"pergunta": "41) Quais grandezas permitem distinguir um tipo de onda de outro?", "opcoes": ["A) Intensidade, área e velocidade", "B) Amplitude, velocidade, frequência e comprimento de onda", "C) Polarização, massa e energia", "D) Altura, timbre e intensidade", "E) Sentido e direção apenas"], "correta": "B"},
        {"pergunta": "42) Um transmissor de rádio opera a 20 MHz. Qual é o comprimento de onda emitido?", "opcoes": ["A) 5 m", "B) 10 m", "C) 15 m", "D) 20 m", "E) 25 m"], "correta": "C"},
        {"pergunta": "43) Um corpo de 1 kg absorve 1250 cal ao ser aquecido de 30 °C a 80 °C. O calor específico é:", "opcoes": ["A) 0,025 cal/g°C", "B) 0,25 cal/g°C", "C) 1,25 cal/g°C", "D) 25 cal/g°C", "E) 150 cal/g°C"], "correta": "B"},
        {"pergunta": "44) Uma lâmpada incandescente (T = 3000 K) emite radiação máxima com comprimento de onda:", "opcoes": ["A) 96 nm", "B) 165 nm", "C) 350 nm", "D) 500 nm", "E) 966 nm"], "correta": "E"},
        {"pergunta": "45) Em um gráfico de emissividade, qual corpo é o menos quente?", "opcoes": ["A) X", "B) Y", "C) Z", "D) X e Y", "E) Y e Z"], "correta": "B"},
        {"pergunta": "46) Uma estrela tem área igual à do Sol e potência 2,43×10²⁴ W. Qual é a temperatura aproximada?", "opcoes": ["A) 19 000 K", "B) 24 000 K", "C) 28 000 K", "D) 30 000 K", "E) 34 000 K"], "correta": "A"},
        {"pergunta": "47) Qual é a energia de um fotão de frequência 7,5×10¹⁸ Hz?", "opcoes": ["A) 1,99×10⁻¹⁵ J", "B) 2,99×10⁻¹⁵ J", "C) 3,99×10⁻¹⁵ J", "D) 4,99×10⁻¹⁵ J", "E) 5,99×10⁻¹⁵ J"], "correta": "D"},
        {"pergunta": "48) A interação eletromagnética ocorre entre:", "opcoes": ["A) Protões e neutrões", "B) Protões e protões", "C) Eletrões e eletrões", "D) Fotões e fotões", "E) Eletrões e fotões"], "correta": "E"},
        {"pergunta": "49) Um fotão tem comprimento de onda 198,6 nm. Qual é a sua energia?", "opcoes": ["A) 1,0×10⁻¹⁸ J", "B) 2,0×10⁻¹⁸ J", "C) 3,0×10⁻¹⁸ J", "D) 4,0×10⁻¹⁸ J", "E) 5,0×10⁻¹⁸ J"], "correta": "B"},
        {"pergunta": "50) A radioatividade é consequência de:", "opcoes": ["A) Combustão química", "B) Alterações no núcleo dos átomos", "C) Escape de eletrões", "D) Ruptura de ligações químicas", "E) Variação de temperatura"], "correta": "B"}
    ]

# -------------------------------
# ESTADO DA SESSÃO
# -------------------------------
if "
