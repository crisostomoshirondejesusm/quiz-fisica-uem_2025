import streamlit as st

# 1. Configurações da Página
st.set_page_config(page_title="Exame Unificado UEM 2025", layout="wide")

# FUNÇÃO PARA REINICIAR TUDO
def reset_perguntas():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# 2. BANCO DE DADOS INTEGRAL (80 QUESTÕES)
if "perguntas" not in st.session_state:
    # MATEMÁTICA (1-40) - Transcritas do PDF
    m_qs = [
        {"id": 1, "p": "Indique as soluções da equação $-|x-2|+6=2$:", "opts": ["A. x=2 v x=6", "B. x=-4 v x=4", "C. x=2", "D. x=-2 v x=6", "E. x=4"], "c": "D", "img": None},
        {"id": 2, "p": "Dizemos que $|x|>3$ se e somente se:", "opts": ["A. x ∈ ]-∞,-3[ ∪ ]3,+∞[", "B. x ∈ R", "C. x ∈ ]-3,3[", "D. x ∈ ]-∞,-3] ∪ [3,+∞[", "E. x ∈ ]3,+∞["], "c": "A", "img": None},
        {"id": 3, "p": "O conjunto dos números reais que se encontra a uma distância igual ou inferior a 3/2 do número π é:", "opts": ["A. x - 3/2 = π", "B. |x - π| ≤ 3/2", "C. |x - 3/2| ≤ π", "D. x + 3/2 ≥ π", "E. x ≤ 3/2"], "c": "B", "img": None},
        {"id": 4, "p": "A função $y=|ax^{2}+bx+c|,(a\\ne0,b\\ne0,c\\ne0)$ é:", "opts": ["A. Positiva", "B. Positiva se x≥0", "C. Par", "D. Ímpar", "E. Nenhuma delas"], "c": "E", "img": None},
        {"id": 5, "p": "Para que valores de x é válida a equação $|x+\pi|=-(x+\pi)$?", "opts": ["A. x ≥ 0", "B. x = -π", "C. x ≥ π", "D. x ≤ 0", "E. x ≤ -π"], "c": "E", "img": None},
        {"id": 6, "p": "Intersecção entre $f(x)=-|x|+4$ e $g(x)=|x+1|$:", "opts": ["A. x=-3 v x=3", "B. x=-1 v x=4", "C. x=0", "D. x=-x", "E. x=-1 v x=3/2"], "c": "E", "img": None},
        {"id": 7, "p": "Divisores de 60: Qual a probabilidade de escolher um número primo?", "opts": ["A. 0,25", "B. 0,3", "C. 1,2", "D. 0,6", "E. 0,75"], "c": "A", "img": None},
        {"id": 8, "p": "A solução da equação combinatória $C_{2}^{n}=6$ é:", "opts": ["A. n=4 v n=-3", "B. n=-4 v n=3", "C. n=3", "D. n=4", "E. n=6"], "c": "D", "img": None},
        {"id": 9, "p": "Quantos números de quatro dígitos existem no total?", "opts": ["A. 40", "B. 400", "C. 10000", "D. 8000", "E. 40000"], "c": "C", "img": None},
        {"id": 10, "p": "Palavras com LÁPIS terminadas em 3 consoantes:", "opts": ["A. 6", "B. 5!", "C. 2!x3!", "D. 12", "E. 10"], "c": "D", "img": None},
        {"id": 11, "p": "Formas de sentar 5 pessoas em 8 lugares:", "opts": ["A. 5^8", "B. A(8,5)x3", "C. C(8,5)x3!", "D. A(6,5)", "E. C(8,5)x5!"], "c": "E", "img": None},
        {"id": 12, "p": "Bolas azuis = 14. P(azul) = 2/3. Quantas bolas amarelas?", "opts": ["A. 7", "B. 28", "C. 3", "D. 10", "E. 9"], "c": "A", "img": None},
        {"id": 13, "p": "Linha do Triângulo de Pascal (1, 15, 105...). P(elemento = 105):", "opts": ["A. 3/21", "B. 2/3", "C. 1/15", "D. 1/5", "E. 1/8"], "c": "E", "img": None},
        {"id": 14, "p": "Domínio de $f(x)=\\sqrt{x-1} \\cdot \\ln(1-x^{2})$:", "opts": ["A. R", "B. ]-1,1[", "C. [1,+∞[", "D. {1}", "E. Conjunto Vazio"], "c": "E", "img": None},
        {"id": 15, "p": "Contradomínio (Imagem) de $f(x)=5 \\cos(2x)+1$:", "opts": ["A. [-1,1]", "B. [-5,5]", "C. [-4,6]", "D. [0,1]", "E. R"], "c": "C", "img": None},
        {"id": 16, "p": "Função afim com zero em 3 e g(-2)=-5:", "opts": ["A. g(x)=-x+3", "B. g(x)=-x+7", "C. g(x)=x^2-9", "D. g(x)=x-3", "E. g(x)=3x+1"], "c": "D", "img": None},
        {"id": 17, "p": "Sobre $f(x)=-x^{2}+4$, indique a verdadeira:", "opts": ["A. É monótona", "B. Domínio R", "C. Injectiva", "D. Um zero", "E. Mínimo"], "c": "B", "img": None},
        {"id": 18, "p": "Assímptotas verticais x=-2, x=3 e horizontal y=2:", "opts": ["A. (x-3)/(x-5)", "B. f(x)=2/x", "C. f(x)=x^2", "D. 2x/(x+4)", "E. (2x^2+7)/(x^2-x-6)"], "c": "E", "img": None},
        {"id": 19, "p": "Se $f(x)=2^{x}-2$ e $g(x)=f(x+k)$ passa em (-4, -3/2), k é:", "opts": ["A. 3", "B. -3", "C. 4", "D. -4", "E. 0"], "c": "A", "img": None},
        {"id": 20, "p": "Zeros da composta $(f \\circ g^{-1})(x)$ com $f=x^2-9, g=2x+4$:", "opts": ["A. {-2, 10}", "B. {-3, 3}", "C. {0}", "D. {2}", "E. {1}"], "c": "A", "img": None},
        {"id": 21, "p": "P.A.: $u_5+u_6=31$ e $u_7+u_9=46$. Determine u1 e r:", "opts": ["A. 1, 3", "B. -2, 2", "C. 2, 3", "D. 3, 4", "E. 3, 2"], "c": "C", "img": None},
        {"id": 22, "p": "P.G.: $v_5=4$ e $v_8=108$. Determine $v_6$:", "opts": ["A. 6", "B. 12", "C. 51", "D. 76", "E. 98"], "c": "B", "img": None},
        {"id": 23, "p": "Sucessão $u_n = \\log_{1/2}(3^n)$ é uma:", "opts": ["A. P.A. Crescente", "B. P.A. Decrescente", "C. P.G.", "D. Convergente", "E. Constante"], "c": "B", "img": None},
        {"id": 24, "p": "Qual sucessão é convergente?", "opts": ["A. n^2", "B. n!", "C. (-1)^n", "D. (-1)^n / n", "E. 2^n"], "c": "D", "img": None},
        {"id": 25, "p": "Sobre $v_n$ definida por ramos (n < 10...), a sucessão é:", "opts": ["A. Ilimitada", "B. Decrescente", "C. Crescente", "D. Divergente", "E. Limitada"], "c": "E", "img": None},
        {"id": 26, "p": "Limite de $(2n^2+3n+4)/(n^2+4)$:", "opts": ["A. 0", "B. 1", "C. 2", "D. 3", "E. Infinito"], "c": "C", "img": None},
        {"id": 27, "p": "Limite de $(1+1/n)^{2n}$:", "opts": ["A. 1", "B. 2e", "C. e^2", "D. 0", "E. e"], "c": "C", "img": None},
        {"id": 28, "p": "Valor de 'a' para continuidade em $f(x)$:", "opts": ["A. -5", "B. -4", "C. -2", "D. -1", "E. 1"], "c": "D", "img": None},
        {"id": 29, "p": "Se $y=3x-5$ é assímptota de g(x), então:", "opts": ["A. lim[g(x)+3x]=0", "B. lim[g(x)-3x+5]=0", "C. lim=5", "D. lim=3", "E. Nenhuma"], "c": "B", "img": None},
        {"id": 30, "p": "Gráfico com salto em x=2. O limite em x=2:", "opts": ["A. É 2", "B. Não existe", "C. É 0", "D. É f(2)", "E. É infinito"], "c": "B", "img": "grafico_limite.png"},
        {"id": 31, "p": "Limite de $\\sin(2x)/x$ quando x->0:", "opts": ["A. 0", "B. 1", "C. 2", "D. 1/2", "E. -1"], "c": "C", "img": None},
        {"id": 32, "p": "Limite da diferença de razões polinomiais quando x->inf:", "opts": ["A. 0", "B. 1", "C. 3", "D. 5", "E. Inf"], "c": "C", "img": None},
        {"id": 33, "p": "Derivada de $f(x) = \\ln(2x^2/3 + 2)$:", "opts": ["A. 4x/3", "B. 1/x", "C. (4x)/(2x^2+6)", "D. 2x", "E. 4x"], "c": "C", "img": None},
        {"id": 34, "p": "Se $g(x) = g'(x)$, então g(x) pode ser:", "opts": ["A. 5", "B. 3e^x", "C. 2x", "D. sin(x)", "E. ln(x)"], "c": "B", "img": None},
        {"id": 35, "p": "Declive da tangente a $kx^2+10x+1$ em x=2 é 2. k é:", "opts": ["A. 2", "B. -2", "C. 1", "D. 0", "E. -3"], "c": "B", "img": None},
        {"id": 36, "p": "Recta tangente a $\\sin(\\pi x)$ em x=1:", "opts": ["A. y=0", "B. y=x", "C. y=\\pi-\\pi x", "D. y=\\pi x", "E. y=1"], "c": "C", "img": None},
        {"id": 37, "p": "Extremos de $f(x)=x^3-3x^2-24x+1$:", "opts": ["A. Máx x=-2, Mín x=4", "B. Só Máx", "C. Só Mín", "D. Inflexão", "E. Nenhuma"], "c": "A", "img": None},
        {"id": 38, "p": "Concavidade de f com $f'(x)=2xe^{1-x^2}$ voltada para cima em:", "opts": ["A. R", "B. ]-√2/2, √2/2[", "C. ]0,1[", "D. ]-1,1[", "E. Vazio"], "c": "B", "img": None},
        {"id": 39, "p": "Primitiva de $e^x + 1$:", "opts": ["A. e^x", "B. e^x + x", "C. e^x + C", "D. x", "E. 2e^x"], "c": "B", "img": None},
        {"id": 40, "p": "Complexos: $(3-2i)(-4+i)$:", "opts": ["A. -10+11i", "B. 10-11i", "C. 12", "D. -12+2i", "E. 1"], "c": "A", "img": None}
    ]

    # FÍSICA (41-80) - Enunciados e Gabarito
    f_qs = [
        {"id": 41, "p": "Transmissão de calor em fluido (água) aquecida por baixo:", "opts": ["A. Condução", "B. Irradiação", "C. Convecção", "D. Efeito Joule", "E. Fusão"], "c": "C", "img": None},
        {"id": 42, "p": "O que distingue ondas eletromagnéticas no vácuo?", "opts": ["A. Velocidade", "B. Frequência", "C. Meio", "D. Amplitude", "E. Fase"], "c": "B", "img": None},
        {"id": 43, "p": "Comprimento de onda para 20 MHz (v=3x10^8 m/s):", "opts": ["A. 15m", "B. 20m", "C. 30m", "D. 5m", "E. 10m"], "c": "A", "img": None},
        {"id": 44, "p": "Calor específico de 100g, 1250 cal, ΔT=50°C:", "opts": ["A. 0,1", "B. 0,25", "C. 0,5", "D. 1,0", "E. 2,0"], "c": "B", "img": None},
        {"id": 45, "p": "Corpo Negro T=3000K. λ máximo (nm):", "opts": ["A. 966", "B. 500", "C. 700", "D. 1000", "E. 1200"], "c": "A", "img": None},
        {"id": 46, "p": "Gráfico emissividade X, Y, Z. O menos quente é:", "opts": ["A. X", "B. Y", "C. Z", "D. Todos iguais", "E. X e Z"], "c": "B", "img": "grafico_emissividade.png"},
        {"id": 47, "p": "Estrela área 10^14 m², P=24,3x10^23 W. T em Kelvin:", "opts": ["A. 19000", "B. 5000", "C. 10000", "D. 15000", "E. 25000"], "c": "A", "img": None},
        {"id": 48, "p": "Energia fotão raios X (λ=10^-10 m):", "opts": ["A. 2x10^-15J", "B. 5x10^-19J", "C. 10J", "D. 3x10^-10J", "E. 0J"], "c": "A", "img": None},
        {"id": 49, "p": "ΔE ao absorver quantum com λ=198,6 nm:", "opts": ["A. 10^-18J", "B. 10^-19J", "C. 10^-20J", "D. 1J", "E. 2J"], "c": "A", "img": None},
        {"id": 50, "p": "Efeito fotoelétrico é a interação entre:", "opts": ["A. Fotões e protões", "B. Fotões e electrões", "C. Electrões e neutrões", "D. Calor e luz", "E. Atómos"], "c": "B", "img": None},
        {"id": 51, "p": "Nº fotões/seg que entram no olho (P=2x10^-17W):", "opts": ["A. 50", "B. 100", "C. 500", "D. 1000", "E. 10"], "c": "A", "img": None},
        {"id": 52, "p": "Nº de fotões que H emite na 3ª órbita:", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 6"], "c": "C", "img": None},
        {"id": 53, "p": "Energia cinética de electrão acelerado por 5000V:", "opts": ["A. 8x10^-16J", "B. 5x10^-16J", "C. 1x10^-19J", "D. 5000J", "E. 1,6x10^-19J"], "c": "A", "img": None},
        {"id": 54, "p": "Tensão para f=3x10^19 Hz em raios X:", "opts": ["A. 124kV", "B. 100kV", "C. 50kV", "D. 200kV", "E. 10kV"], "c": "A", "img": None},
        {"id": 55, "p": "Transmissão com maior momento linear (p=E/c):", "opts": ["A. T1 (maior salto)", "B. T2", "C. T3", "D. T4", "E. Todas iguais"], "c": "A", "img": "niveis_energia.png"},
        {"id": 56, "p": "Radioactividade deve-se a:", "opts": ["A. Calor", "B. Núcleo instável", "C. Electrões", "D. Química", "E. Gravidade"], "c": "B", "img": None},
        {"id": 57, "p": "Radiação Beta é composta por:", "opts": ["A. Fotões", "B. Protões", "C. Hélio", "D. Electrões nucleares", "E. Neutrões"], "c": "D", "img": None},
        {"id": 58, "p": "Nêutrons em 208/83 Bi:", "opts": ["A. 83", "B. 125", "C. 208", "D. 291", "E. 100"], "c": "B", "img": None},
        {"id": 59, "p": "Reação nuclear 27/13 Al + gama -> 26/12 Mg + X. X é:", "opts": ["A. Protão/H", "B. Alfa", "C. Beta", "D. Neutrão", "E. Positron"], "c": "A", "img": None},
        {"id": 60, "p": "Radiação desviada para polo negativo (Experimento Chumbo):", "opts": ["A. Alfa", "B. Beta", "C. Gama", "D. Raios X", "E. Infravermelho"], "c": "A", "img": "bloco_chumbo.png"},
        {"id": 61, "p": "Reação de fissão típica (U-235):", "opts": ["A. Fusão H", "B. Quebra do Núcleo", "C. Combustão", "D. Oxidação", "E. Decaimento Gama"], "c": "B", "img": None},
        {"id": 62, "p": "Energia de ligação por nucleão (160MeV / 20):", "opts": ["A. 8 MeV", "B. 4 MeV", "C. 16 MeV", "D. 40 MeV", "E. 2 MeV"], "c": "A", "img": None},
        {"id": 63, "p": "Defeito de massa 0,02 uma. Energia (MeV):", "opts": ["A. 18,6", "B. 931", "C. 20", "D. 5", "E. 1"], "c": "A", "img": None},
        {"id": 64, "p": "Produto T na fissão do Urânio:", "opts": ["A. Rb (37, 90)", "B. Xe", "C. Kr", "D. Ba", "E. Sr"], "c": "A", "img": None},
        {"id": 65, "p": "Decaimento Iodo-131 (8 dias) para 1/16:", "opts": ["A. 32 dias", "B. 8 dias", "C. 16 dias", "D. 40 dias", "E. 64 dias"], "c": "A", "img": None},
        {"id": 66, "p": "Conservação de vazão Q1=Q2+Q3:", "opts": ["A. Q1=Q2=Q3", "B. Q1=Q2+Q3", "C. Q1+Q2=Q3", "D. Bernoulli", "E. Torricelli"], "c": "B", "img": "tubo_vazao.png"},
        {"id": 67, "p": "Velocidade gás saída (P1/P2 relação):", "opts": ["A. 80 m/s", "B. 50 m/s", "C. 10 m/s", "D. 100 m/s", "E. 5 m/s"], "c": "B", "img": None},
        {"id": 68, "p": "Equação da continuidade (A1v1=A2v2):", "opts": ["A. 12 m/s", "B. 6 m/s", "C. 3 m/s", "D. 24 m/s", "E. 9 m/s"], "c": "A", "img": None},
        {"id": 69, "p": "Vazão dm³/s (12000L em 40min):", "opts": ["A. 5", "B. 10", "C. 20", "D. 50", "E. 1"], "c": "A", "img": None},
        {"id": 70, "p": "Prensa Hidráulica (F1/A1 = F2/A2):", "opts": ["A. 6,25 N", "B. 10 N", "C. 100 N", "D. 1 N", "E. 0,5 N"], "c": "A", "img": None},
        {"id": 71, "p": "Velocidade para encher piscina em 10h:", "opts": ["A. 4 m/s", "B. 2 m/s", "C. 8 m/s", "D. 10 m/s", "E. 1 m/s"], "c": "A", "img": None},
        {"id": 72, "p": "Gases: PV=nRT. n em moles:", "opts": ["A. 3", "B. 1", "C. 10", "D. 5", "E. 0,5"], "c": "A", "img": None},
        {"id": 73, "p": "Ciclo V vs T (1-2-3):", "opts": ["A. Isobárica-Isovolumétrica-Isotérmica", "B. Isovolumétrica-Isobárica-Isotérmica", "C. Ciclo Carnot", "D. Expansão", "E. Nenhuma"], "c": "B", "img": "grafico_vt.png"},
        {"id": 74, "p": "Volume de H a 293K (P constante):", "opts": ["A. 0,14 L", "B. 0,15 L", "C. 0,10 L", "D. 0,20 L", "E. 0,30 L"], "c": "A", "img": None},
        {"id": 75, "p": "Qual diagrama PV é falso?", "opts": ["A. A", "B. B", "C. C", "D. D", "E. E (Curva inversa)"], "c": "E", "img": "diagramas_pv.png"},
        {"id": 76, "p": "ΔU total (ΔU = Q - W):", "opts": ["A. 100 J", "B. 200 J", "C. 0 J", "D. 300 J", "E. 500 J"], "c": "A", "img": None},
        {"id": 77, "p": "Trabalho adiabático (W = -ΔU):", "opts": ["A. 10 kJ", "B. 0 kJ", "C. -10 kJ", "D. 20 kJ", "E. 5 kJ"], "c": "A", "img": None},
        {"id": 78, "p": "Trabalho no Ciclo (Área do gráfico):", "opts": ["A. 1,6x10^5 J", "B. 10^5 J", "C. 0 J", "D. 4x10^5 J", "E. 2x10^5 J"], "c": "A", "img": "ciclo_pv.png"},
        {"id": 79, "p": "MHS: Massa-Mola. Período e Amplitude:", "opts": ["A. 1,0s e 3cm", "B. 0,5s e 2cm", "C. 2,0s e 10cm", "D. 1,0s e 1cm", "E. 5s e 5cm"], "c": "A", "img": None},
        {"id": 80, "p": "Aceleração máxima no MHS:", "opts": ["A. 2pi²", "B. pi²", "C. 4pi²", "D. 0", "E. 10"], "c": "A", "img": "grafico_mhs.png"}
    ]

    # MESCLAGEM INTERCALADA (M, F, M, F...)
    lista_final = []
    for m, f in zip(m_qs, f_qs):
        lista_final.append(m)
        lista_final.append(f)
    st.session_state.perguntas = lista_final

# 3. CONTROLES DE ESTADO
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False

# 4. INTERFACE DO USUÁRIO
st.title("🚀 SIMULADOR UEM 2025 - COMPLETO")

# Sidebar com estatísticas em tempo real
with st.sidebar:
    st.header("📊 Painel de Controle")
    st.progress((st.session_state.i + 1) / 80)
    st.write(f"Questão Atual: **{st.session_state.i + 1} / 80**")
    st.write(f"Respondidas: **{len(st.session_state.respostas)}**")
    if st.button("🔴 Reiniciar Simulado", use_container_width=True):
        reset_perguntas()

# Lógica Principal do Questionário
if not st.session_state.quiz_fim:
    q = st.session_state.perguntas[st.session_state.i]
    
    # Cabeçalho da Questão
    cor_box = "blue" if q['id'] <= 40 else "orange"
    tipo_txt = "MATEMÁTICA" if q['id'] <= 40 else "FÍSICA"
    st.markdown(f"### Questão {st.session_state.i + 1} - :{cor_box}[{tipo_txt}]")
    
    # Enunciado
    with st.container(border=True):
        st.markdown(f"#### {q['p']}")
        
        # Simulação de Imagem (Substitua pelos seus arquivos reais na pasta 'imagens/')
        if q["img"]:
            st.info(f"🖼️ [Gráfico/Imagem: {q['img']}]")
            # Se você tiver as imagens, use: st.image(f"imagens/{q['img']}")

    # Opções
    resp_ja_salva = st.session_state.respostas.get(st.session_state.i, None)
    idx_default = 0
    if resp_ja_salva:
        for idx, texto in enumerate(q["opts"]):
            if texto.startswith(resp_ja_salva): idx_default = idx

    escolha = st.radio("Selecione a opção correta:", q["opts"], index=idx_default, key=f"q_{st.session_state.i}")

    # Navegação
    st.divider()
    c1, c2, c3 = st.columns(3)
    
    with c1:
        if st.button("⬅️ Anterior", disabled=(st.session_state.i == 0), use_container_width=True):
            st.session_state.i -= 1
            st.rerun()
    
    with c2:
        if st.button("💾 Salvar Escolha", type="primary", use_container_width=True):
            st.session_state.respostas[st.session_state.i] = escolha[0]
            st.toast(f"Resposta {escolha[0]} salva!", icon="✅")
            
    with c3:
        txt_botao = "Finalizar 🏁" if st.session_state.i == 79 else "Próxima ➡️"
        if st.button(txt_botao, use_container_width=True):
            st.session_state.respostas[st.session_state.i] = escolha[0]
            if st.session_state.i < 79:
                st.session_state.i += 1
            else:
                st.session_state.quiz_fim = True
            st.rerun()

else:
    # TELA DE RESULTADOS
    st.balloons()
    st.header("🏆 Resultado Final")
    
    # Cálculos
    acertos = 0
    for idx, questao in enumerate(st.session_state.perguntas):
        if st.session_state.respostas.get(idx) == questao["c"]:
            acertos += 1
    
    nota = (acertos / 80) * 20
    
    col_a, col_b = st.columns(2)
    col_a.metric("Total de Acertos", f"{acertos} / 80")
    col_b.metric("Nota UEM", f"{nota:.2f} / 20.0")

    # Tabela de Correção
    with st.expander("📝 Ver Gabarito e Suas Respostas"):
        for idx, q in enumerate(st.session_state.perguntas):
            resp_usuario = st.session_state.respostas.get(idx, "-")
            correta = q["c"]
            is_correct = resp_usuario == correta
            
            # Formatação
            simbolo = "✅" if is_correct else "❌"
            cor_texto = "green" if is_correct else "red"
            
            st.markdown(f"**{idx+1}.** {q['p']}")
            st.markdown(f"Sua Resposta: :{cor_texto}[{resp_usuario}] | Correta: **{correta}** {simbolo}")
            st.divider()
