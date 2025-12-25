import streamlit as st
import time
import streamlit.components.v1 as components

# 1. Configurações da Página
st.set_page_config(page_title="Exame de Física UEM 2025", layout="centered")

# 2. Banco de Dados Completo (41 a 80)
if "perguntas" not in st.session_state:
    st.session_state.perguntas = [
        {"id": 41, "p": "Um recipiente de vidro está quase cheio com água em temperatura ambiente. Ao colocá-lo sobre uma chama de fogão, a água começa a se aquecer por:", "opts": ["A. Condução", "B. irradiação", "C. convecção", "D. condução e convecção", "E. convecção e irradiação"], "c": "C", "img": None},
        {"id": 42, "p": "Quais são as características capazes de distinguir um tipo de onda electromagnética de outro?", "opts": ["A. intensidade, velocidade, área, comprimento", "B. amplitude, velocidade da propagação, frequência, comprimento de onda", "C. amplitude, polarização, frequência, direcção", "D. altura, intensidade, timbre, velocidade", "E. amplitude, perturbação, propagação"], "c": "B", "img": None},
        {"id": 43, "p": "Um transmissor de rádio opera a 20 MHz. Qual é o comprimento de onda do transmissor?", "opts": ["A. 15 m", "B. 25 m", "C. 35 m", "D. 45 m", "E. 55 m"], "c": "A", "img": None},
        {"id": 44, "p": "Um corpo de massa 100 g recebeu 1250 cal ao ser aquecido de 30°C a 80°C. O seu calor específico é:", "opts": ["A. 0.025 cal/g.°C", "B. 2.50 cal/g.°C", "C. 2,5 cal/g.°C", "D. 25 cal/g.°C", "E. 0,25 cal/g.°C"], "c": "E", "img": None},
        {"id": 45, "p": "Uma lâmpada incandescente (corpo negro) tem T=3000K. Determine o comprimento de onda de emissão máxima (nm). (b=2,9x10^-3 mK)", "opts": ["A. 966", "B. 765", "C. 438", "D. 350", "E. 320"], "c": "A", "img": None},
        {"id": 46, "p": "O gráfico representa a emissividade de corpos X, Y e Z. Qual dos corpos é o menos quente?", "opts": ["A. Ty=Tx", "B. Ty", "C. Tz", "D. Tz=Ty", "E. Tx"], "c": "B", "img": "Gráfico de Emissividade"},
        {"id": 47, "p": "Uma estrela tem área de 1/10 * 10^15 m² e potência de 24,3x10^23 W. Qual a temperatura (K)?", "opts": ["A. 19000", "B. 24000", "C. 28000", "D. 30000", "E. 34000"], "c": "A", "img": None},
        {"id": 48, "p": "Determine a energia de fotões de raios X com comprimento de onda de 1,0x10^-10 m.", "opts": ["A. 5,99x10^-15J", "B. 4,99x10^-15J", "C. 3,99x10^-15J", "D. 2,99x10^-15J", "E. 1,99x10^-15J"], "c": "E", "img": None},
        {"id": 49, "p": "Variação de energia de um átomo ao absorver um quantum com comprimento de onda de 198,6 nm.", "opts": ["A. 0.25x10^-18J", "B. 0.5x10^-18J", "C. 1x10^-18J", "D. 2x10^-18J", "E. 3x10^-18J"], "c": "C", "img": None},
        {"id": 50, "p": "O efeito fotoeléctrico ocorre devido à interação entre:", "opts": ["A. protões e electrões", "B. fotões e electrões", "C. electrões e electrões", "D. fotões e fotões", "E. protões e fotões"], "c": "B", "img": None},
        {"id": 51, "p": "Quantos fotões entram no olho por segundo (comprimento 0,5 µm, potência 2x10^-17 W)?", "opts": ["A. 50", "B. 70", "C. 100", "D. 120", "E. 140"], "c": "A", "img": None},
        {"id": 52, "p": "Número de fotões de diferentes energias que um átomo de hidrogênio emite com electrão na 3ª órbita?", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "c": "C", "img": None},
        {"id": 53, "p": "Energia cinética adquirida por electrões acelerados por 5000 V?", "opts": ["A. 2,0x10^-16J", "B. 4,0x10^-16J", "C. 6,0x10^-16J", "D. 8,0x10^-16J", "E. 10,0x10^-16J"], "c": "D", "img": None},
        {"id": 54, "p": "Tensão (kV) no ânodo de tubo de raios X para frequência máxima de 3x10^19 Hz?", "opts": ["A. 124", "B. 130", "C. 132", "D. 140", "E. 142"], "c": "A", "img": None},
        {"id": 55, "p": "No diagrama de níveis de energia, qual transição emite fotão com maior momento linear?", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "c": "A", "img": "Níveis de Energia do Hidrogénio"},
        # restante banco permanece igual…
    ]

# 3. Gestão de Estado
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False
if "ver_gabarito" not in st.session_state: st.session_state.ver_gabarito = False
if "inicio_t" not in st.session_state: st.session_state.inicio_t = time.time()

# 4. Interface Principal
st.title("📝 Exame de Admissão Física I - UEM 2025")

if not st.session_state.quiz_fim:

    idx = st.session_state.i
    quest = st.session_state.perguntas[idx]

    if quest["img"]:
        st.info(f"📍 Referência Visual: {quest['img']}")
        if quest["id"] == 46:
            pass
        elif quest["id"] == 55:
            pass
        elif quest["id"] == 66:
            pass
        elif quest["id"] == 78:
            pass
