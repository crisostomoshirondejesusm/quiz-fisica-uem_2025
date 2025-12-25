import streamlit as st
import time
import streamlit.components.v1 as components
import os

# 1. Configurações da Página
st.set_page_config(page_title="Exame Unificado UEM 2025", layout="centered")

# 2. Banco de Dados Intercalado (Física e Matemática)
if "perguntas" not in st.session_state:
    # Lista de Física (Original do seu código)
    f_qs = [
        {"id": "F41", "p": "Um recipiente de vidro está quase cheio com água em temperatura ambiente. Ao colocá-lo sobre uma chama de fogão, a água começa a se aquecer por:", "opts": ["A. Condução", "B. irradiação", "C. convecção", "D. condução e convecção", "E. convecção e irradiação"], "c": "C", "img": None},
        {"id": "F42", "p": "Quais são as características capazes de distinguir um tipo de onda electromagnética de outro?", "opts": ["A. intensidade, velocidade, área, comprimento", "B. amplitude, velocidade da propagação, frequência, comprimento de onda", "C. amplitude, polarização, frequência, direcção", "D. altura, intensidade, timbre, velocidade", "E. amplitude, perturbação, propagação"], "c": "B", "img": None},
        {"id": "F43", "p": "Um transmissor de rádio opera a 20 MHz. Qual é o comprimento de onda do transmissor?", "opts": ["A. 15 m", "B. 25 m", "C. 35 m", "D. 45 m", "E. 55 m"], "c": "A", "img": None},
        {"id": "F44", "p": "Um corpo de massa 100 g recebeu 1250 cal ao ser aquecido de 30°C a 80°C. O seu calor específico é:", "opts": ["A. 0.025 cal/g.°C", "B. 2.50 cal/g.°C", "C. 2,5 cal/g.°C", "D. 25 cal/g.°C", "E. 0,25 cal/g.°C"], "c": "E", "img": None},
        {"id": "F45", "p": "Uma lâmpada incandescente (corpo negro) tem T=3000K. Determine o comprimento de onda de emissão máxima (nm). (b=2,9x10^-3 mK)", "opts": ["A. 966", "B. 765", "C. 438", "D. 350", "E. 320"], "c": "A", "img": None},
        {"id": "F46", "p": "O gráfico representa a emissividade de corpos X, Y e Z. Qual dos corpos é o menos quente?", "opts": ["A. Ty=Tx", "B. Ty", "C. Tz", "D. Tz=Ty", "E. Tx"], "c": "B", "img": "q46.png"},
        {"id": "F47", "p": "Uma estrela tem área de 1/10 * 10^15 m² e potência de 24,3x10^23 W. Qual a temperatura (K)?", "opts": ["A. 19000", "B. 24000", "C. 28000", "D. 30000", "E. 34000"], "c": "A", "img": None},
        {"id": "F48", "p": "Determine a energia de fotões de raios X com comprimento de onda de 1,0x10^-10 m.", "opts": ["A. 5,99x10^-15J", "B. 4,99x10^-15J", "C. 3,99x10^-15J", "D. 2,99x10^-15J", "E. 1,99x10^-15J"], "c": "E", "img": None},
        {"id": "F49", "p": "Variação de energia de um átomo ao absorver um quantum com comprimento de onda de 198,6 nm.", "opts": ["A. 0.25x10^-18J", "B. 0.5x10^-18J", "C. 1x10^-18J", "D. 2x10^-18J", "E. 3x10^-18J"], "c": "C", "img": None},
        {"id": "F50", "p": "O efeito fotoeléctrico ocorre devido à interação entre:", "opts": ["A. protões e electrões", "B. fotões e electrões", "C. electrões e electrões", "D. fotões e fotões", "E. protões e fotões"], "c": "B", "img": None},
        # ... (Pode-se completar a lista de física aqui seguindo o padrão)
    ]

    # Lista de Matemática (Extraída do PDF)
    m_qs = [
        {"id": "M01", "p": "Indique as soluções da equação $-|x-2|+6=2$:", "opts": ["A. x=2 v x=6", "B. x=-4 v x=4", "C. x=2", "D. x=-2 v x=6", "E. x=4"], "c": "D", "img": None},
        {"id": "M02", "p": "Dizemos que $|x|>3$ se:", "opts": ["A. x ∈ ]-∞,-3[ ∪ ]3,+∞[", "B. x ∈ R", "C. x ∈ ]-3,3[", "D. x ∈ ]-∞,-3] ∪ [3,+∞[", "E. x ∈ ]3,+∞["], "c": "A", "img": None},
        {"id": "M03", "p": "O conjunto dos números reais que se encontra a uma distância igual ou inferior a 3/2 do número π é dado por:", "opts": ["A. x - 3/2 = π", "B. |x - π| ≤ 3/2", "C. |x - 3/2| ≤ π", "D. x + 3/2 ≥ π", "E. x ≤ 3/2"], "c": "B", "img": None},
        {"id": "M04", "p": "A função $y=|ax^2+bx+c|, (a≠0, b≠0, c≠0)$ é uma função:", "opts": ["A. Positiva", "B. Positiva quando x≥0 e negativa caso contrário", "C. Par", "D. Ímpar", "E. Nenhuma delas"], "c": "E", "img": None},
        {"id": "M05", "p": "Para que valores de x é válida a equação $|x+\pi|=-(x+\pi)$?", "opts": ["A. x ≥ 0", "B. x = -π", "C. x ≥ π", "D. x ≤ 0", "E. x ≤ -π"], "c": "E", "img": None},
        {"id": "M06", "p": "Qual a intersecção das funções $f(x)=-|x|+4$ e $g(x)=|x+1|$?", "opts": ["A. x=-3 v x=3", "B. x=-1 v x=4", "C. x=0", "D. x=-x", "E. x=-1 v x=3/2"], "c": "E", "img": None},
        {"id": "M07", "p": "Considerando todos os divisores do número 60, determine a probabilidade de se escolher um número primo:", "opts": ["A. 0,25", "B. 0,3", "C. 1,2", "D. 0,6", "E. 0,75"], "c": "A", "img": None},
        {"id": "M08", "p": "A solução da equação $C_2^n=6$ é:", "opts": ["A. n=4 v n=-3", "B. n=-4 v n=3", "C. n=3", "D. n=4", "E. n=6"], "c": "D", "img": None},
        {"id": "M09", "p": "Um código numérico contém quatro dígitos. Quantos números de quatro dígitos existem?", "opts": ["A. 40", "B. 400", "C. 10000", "D. 8000", "E. 40000"], "c": "C", "img": None},
        {"id": "M10", "p": "Quantas palavras podem escrever-se usando LÁPIS, terminadas em 3 consoantes?", "opts": ["A. 6", "B. 5!", "C. 2! x 3!", "D. 12", "E. 10"], "c": "D", "img": None},
    ]

    # Intercalar: 1 Física, 1 Matemática
    intercaladas = []
    for f, m in zip(f_qs, m_qs):
        intercaladas.append(f)
        intercaladas.append(m)
    
    st.session_state.perguntas = intercaladas

# 3. Gestão de Estado
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False
if "ver_gabarito" not in st.session_state: st.session_state.ver_gabarito = False
if "inicio_t" not in st.session_state: st.session_state.inicio_t = time.time()
if "quest_t" not in st.session_state: st.session_state.quest_t = time.time()

def reiniciar_total():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

def proxima_questao():
    if st.session_state.i + 1 < len(st.session_state.perguntas):
        st.session_state.i += 1
        st.session_state.quest_t = time.time()
    else:
        st.session_state.quiz_fim = True
    st.rerun()

# 4. Interface Principal
st.title("🎓 Exame Admissão UEM 2025")
st.subheader("Física & Matemática Intercalados")

if not st.session_state.quiz_fim:
    # Cronômetro: 90 min (5400s) para o total
    t_global_restante = max(0, 5400 - int(time.time() - st.session_state.inicio_t))
    t_quest_restante = max(0, 120 - int(time.time() - st.session_state.quest_t)) # 2 min por questão
    
    if t_quest_restante <= 0:
        proxima_questao()

    c_t1, c_t2, c_t3 = st.columns(3)
    c_t1.metric("⏳ Tempo Total", f"{t_global_restante//60}m {t_global_restante%60}s")
    c_t2.metric("⏱️ Questão", f"{t_quest_restante}s")
    c_t3.metric("📊 Progresso", f"{st.session_state.i + 1} / {len(st.session_state.perguntas)}")
    
    st.divider()

    idx = st.session_state.i
    quest = st.session_state.perguntas[idx]
    
    # Identificador de Matéria
    tipo = "🍎 FÍSICA" if str(quest['id']).startswith('F') else "📐 MATEMÁTICA"
    st.info(f"Matéria: {tipo}")

    # Exibição de Imagem
    if quest["img"]:
        caminho_img = f"imagens/{quest['img']}"
        if os.path.exists(caminho_img):
            st.image(caminho_img, caption=f"Figura da Questão {quest['id']}", use_container_width=True)
        else:
            # Espaço reservado para imagem se o arquivo não existir
            st.info(f"🖼️ [Espaço para imagem: {quest['img']}]")

    st.markdown(f"#### Questão {quest['id']}: \n {quest['p']}")
    
    marcada = st.session_state.respostas.get(idx, None)
    id_radio = 0
    if marcada:
        for i_opt, txt in enumerate(quest["opts"]):
            if txt.startswith(marcada): id_radio = i_opt

    escolha = st.radio("Selecione a opção:", quest["opts"], index=id_radio, key=f"r{idx}")

    if st.button("✅ CONFIRMAR E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas[idx] = escolha[0] # Pega apenas a letra (A, B, C...)
        proxima_questao()

    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅️ ANTERIOR", use_container_width=True, disabled=(idx==0)):
            st.session_state.i -= 1
            st.session_state.quest_t = time.time()
            st.rerun()
    with c2:
        if st.button("PULAR ➡️", use_container_width=True):
            proxima_questao()

    time.sleep(1)
    st.rerun()

else:
    st.success("🏁 FIM DO EXAME!")
    total_q = len(st.session_state.perguntas)
    acertos = sum(1 for i, q in enumerate(st.session_state.perguntas) if st.session_state.respostas.get(i) == q["c"])
    
    st.markdown("### 📊 Resultado Final")
    res_c1, res_c2 = st.columns(2)
    res_c1.metric("Acertos", f"{acertos} / {total_q}")
    res_c2.metric("Nota (0-20)", f"{(acertos/total_q)*20:.1f}")

    if st.button("🔄 REINICIAR TUDO", use_container_width=True):
        reiniciar_total()

    st.divider()
    if st.button("🔍 VER CORRECÇÃO", use_container_width=True):
        st.session_state.ver_gabarito = not st.session_state.ver_gabarito

    if st.session_state.ver_gabarito:
        for i, q in enumerate(st.session_state.perguntas):
            sua = st.session_state.respostas.get(i, "Vazio")
            cor = "✅" if sua == q["c"] else "❌"
            with st.expander(f"Q{q['id']}: {cor}"):
                st.write(f"**Pergunta:** {q['p']}")
                st.write(f"Sua resposta: {sua} | Resposta correta: **{q['c']}**")
