import streamlit as st
import time
import streamlit.components.v1 as components

# ======================================================
# 1. CONFIGURAÇÕES DA PÁGINA
# ======================================================
st.set_page_config(
    page_title="Simulado de Física UEM 2025",
    layout="centered"
)

# ======================================================
# 2. BANCO DE QUESTÕES (41 a 80)
# ======================================================
if "perguntas" not in st.session_state:
    st.session_state.perguntas = [
        {"id": 41, "p": "Um recipiente de vidro está quase cheio com água em temperatura ambiente. Ao colocá-lo sobre uma chama de fogão, a água começa a se aquecer por:", "opts": ["A. Condução", "B. Irradiação", "C. Convecção", "D. Condução e Convecção", "E. Convecção e Irradiação"], "c": "C", "img": None},
        {"id": 42, "p": "Quais são as características capazes de distinguir um tipo de onda electromagnética de outro?", "opts": ["A. Intensidade, velocidade, área", "B. Amplitude, velocidade, frequência, comprimento de onda", "C. Amplitude, polarização, frequência", "D. Altura, timbre, velocidade", "E. Amplitude, perturbação"], "c": "B", "img": None},
        {"id": 43, "p": "Um transmissor de rádio opera a 20 MHz. Qual é o comprimento de onda?", "opts": ["A. 15 m", "B. 25 m", "C. 35 m", "D. 45 m", "E. 55 m"], "c": "A", "img": None},
        {"id": 44, "p": "Um corpo de massa 100 g recebeu 1250 cal ao ser aquecido de 30°C a 80°C. O calor específico é:", "opts": ["A. 0,025", "B. 2,50", "C. 2,5", "D. 25", "E. 0,25"], "c": "E", "img": None},
        {"id": 45, "p": "Uma lâmpada incandescente tem T = 3000 K. Determine o comprimento de onda máximo (Lei de Wien).", "opts": ["A. 966 nm", "B. 765 nm", "C. 438 nm", "D. 350 nm", "E. 320 nm"], "c": "A", "img": "wien.png"},
        {"id": 46, "p": "O gráfico representa a emissividade de corpos X, Y e Z. Qual é o menos quente?", "opts": ["A. Tx", "B. Ty", "C. Tz", "D. Tx = Ty", "E. Ty = Tz"], "c": "B", "img": "wien.png"},
        {"id": 47, "p": "Uma estrela tem área 1×10¹⁴ m² e potência 2,43×10²⁴ W. Determine a temperatura.", "opts": ["A. 19000 K", "B. 24000 K", "C. 28000 K", "D. 30000 K", "E. 34000 K"], "c": "A", "img": None},
        {"id": 48, "p": "Energia de um fotão de raio X com λ = 1,0×10⁻¹⁰ m.", "opts": ["A. 5,99×10⁻¹⁵", "B. 4,99×10⁻¹⁵", "C. 3,99×10⁻¹⁵", "D. 2,99×10⁻¹⁵", "E. 1,99×10⁻¹⁵"], "c": "E", "img": None},
        {"id": 49, "p": "Energia absorvida por um átomo ao absorver um quantum de 198,6 nm.", "opts": ["A. 0,25×10⁻¹⁸", "B. 0,5×10⁻¹⁸", "C. 1×10⁻¹⁸", "D. 2×10⁻¹⁸", "E. 3×10⁻¹⁸"], "c": "C", "img": None},
        {"id": 50, "p": "O efeito fotoelétrico ocorre devido à interação entre:", "opts": ["A. Protões e eletrões", "B. Fotões e eletrões", "C. Eletrões entre si", "D. Fotões", "E. Protões e fotões"], "c": "B", "img": None},
        # 👉 Se quiseres, posso adicionar TODAS as 80 já prontas
    ]

# ======================================================
# 3. FUNÇÃO DE RESET
# ======================================================
def reiniciar_exame():
    st.session_state.clear()
    st.rerun()

# ======================================================
# 4. ESTADOS
# ======================================================
if "i" not in st.session_state:
    st.session_state.i = 0
if "respostas" not in st.session_state:
    st.session_state.respostas = {}
if "fim" not in st.session_state:
    st.session_state.fim = False
if "inicio" not in st.session_state:
    st.session_state.inicio = time.time()

# ======================================================
# 5. INTERFACE PRINCIPAL
# ======================================================
st.title("⚖️ Simulado de Física – UEM 2025")

DURACAO = 90 * 60  # 90 minutos
tempo_restante = max(0, DURACAO - int(time.time() - st.session_state.inicio))

st.metric("⏳ Tempo Restante", f"{tempo_restante//60}m {tempo_restante%60}s")
st.divider()

# ======================================================
# 6. QUIZ
# ======================================================
if not st.session_state.fim:

    q = st.session_state.perguntas[st.session_state.i]

    if q["img"]:
        st.image(f"images/{q['img']}", caption="Referência visual", use_container_width=True)

    st.subheader(f"Questão {q['id']}")
    escolha = st.radio(q["p"], q["opts"], key=f"q{st.session_state.i}")

    col1, col2 = st.columns(2)

    if col1.button("⬅️ Anterior", disabled=st.session_state.i == 0):
        st.session_state.i -= 1
        st.rerun()

    if col2.button("➡️ Próxima"):
        st.session_state.respostas[st.session_state.i] = escolha[0]
        if st.session_state.i == len(st.session_state.perguntas) - 1:
            st.session_state.fim = True
        else:
            st.session_state.i += 1
        st.rerun()

# ======================================================
# 7. RESULTADOS
# ======================================================
else:
    st.success("🎯 Fim do Simulado!")

    acertos = sum(
        1 for i, q in enumerate(st.session_state.perguntas)
        if st.session_state.respostas.get(i) == q["c"]
    )

    nota = (acertos / len(st.session_state.perguntas)) * 20

    st.metric("Acertos", f"{acertos} / {len(st.session_state.perguntas)}")
    st.metric("Nota Final", f"{nota:.1f} / 20")

    if st.button("📄 Guardar / Imprimir"):
        components.html("<script>window.print()</script>", height=0)

    if st.button("🔄 Refazer Exame"):
        reiniciar_exame()
