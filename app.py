import streamlit as st
import time
import os

# 1. Configurações da Página
st.set_page_config(page_title="Exame Unificado UEM 2025", layout="wide")

# FUNÇÃO PARA REINICIAR
def reset_perguntas():
    if "perguntas" in st.session_state:
        del st.session_state["perguntas"]
    if "respostas" in st.session_state:
        del st.session_state["respostas"]
    st.session_state.i = 0
    st.session_state.quiz_fim = False
    st.rerun()

# 2. Banco de Dados com 80 Questões Integrais
if "perguntas" not in st.session_state:
    # [cite_start]MATEMÁTICA (1-40) - Transcritas do PDF [cite: 1]
    m_qs = [
        {"id": 1, "p": "Indique as soluções da equação $-|x-2|+6=2$:", "opts": ["A. x=2 v x=6", "B. x=-4 v x=4", "C. x=2", "D. x=-2 v x=6", "E. x=4"], "c": "D"},
        {"id": 2, "p": "Dizemos que $|x|>3$ se:", "opts": ["A. x ∈ ]-∞,-3[ ∪ ]3,+∞[", "B. x ∈ R", "C. x ∈ ]-3,3[", "D. x ∈ ]-∞,-3] ∪ [3,+∞[", "E. x ∈ ]3,+∞["], "c": "A"},
        {"id": 3, "p": "O conjunto dos números reais que se encontra a uma distância igual ou inferior a 3/2 do número π é dado pela expressão:", "opts": ["A. x - 3/2 = π", "B. |x - π| ≤ 3/2", "C. |x - 3/2| ≤ π", "D. x + 3/2 ≥ π", "E. x ≤ 3/2"], "c": "B"},
        {"id": 4, "p": "A função $y=|ax^{2}+bx+c|,(a\\ne0,b\\ne0~e~c\\ne0)$ é uma função:", "opts": ["A. Positiva", "B. Positiva quando x≥0 e negativa caso contrário", "C. Par", "D. Ímpar", "E. Nenhuma delas"], "c": "E"},
        {"id": 5, "p": "Para que valores de x é válida a equação $|x+\pi|=-(x+\pi)$?", "opts": ["A. x ≥ 0", "B. x = -π", "C. x ≥ π", "D. x ≤ 0", "E. x ≤ -π"], "c": "E"},
        {"id": 6, "p": "Qual a intersecção das funções $f(x)=-|x|+4$ e $g(x)=|x+1|$?", "opts": ["A. x=-3 v x=3", "B. x=-1 v x=4", "C. x=0", "D. x=-x", "E. x=-1 v x=3/2"], "c": "E"},
        {"id": 7, "p": "Considerando todos os divisores do número 60, determine a probabilidade de se escolher, ao acaso, um número primo:", "opts": ["A. 0,25", "B. 0,3", "C. 1,2", "D. 0,6", "E. 0,75"], "c": "A"},
        {"id": 8, "p": "A solução da equação $C_{2}^{n}=6$ é:", "opts": ["A. n=4 v n=-3", "B. n=-4 v n=3", "C. n=3", "D. n=4", "E. n=6"], "c": "D"},
        {"id": 9, "p": "Um código numérico contém quatro dígitos. Quantos números de quatro dígitos existem?", "opts": ["A. 40", "B. 400", "C. 10000", "D. 8000", "E. 40000"], "c": "C"},
        {"id": 10, "p": "Quantas palavras, com ou sem sentido, podem escrever-se usando as letras da palavra LÁPIS, terminadas em 3 consoantes?", "opts": ["A. 6", "B. 5!", "C. 2!x3!", "D. 12", "E. 10"], "c": "D"},
        {"id": 11, "p": "De quantas formas diferentes podem sentar-se cinco pessoas numa fila de 8 lugares?", "opts": ["A. 5^8", "B. A(8,5)x3", "C. C(8,5)x3!", "D. A(6,5)xA(3,8)", "E. C(8,5)x5!"], "c": "E"},
        {"id": 12, "p": "Uma caixa contém bolas amarelas e azuis. O número de bolas azuis é 14. A probabilidade de tirar azul é 2/3. Quantas bolas amarelas há?", "opts": ["A. 7", "B. 28", "C. 3", "D. 10", "E. 9"], "c": "A"},
        {"id": 13, "p": "Numa linha do Triângulo de Pascal, escolhendo dois elementos ao acaso, qual a probabilidade de ser igual a 105 (sabendo que a linha começa por 1, 15, 105)?", "opts": ["A. 3/21", "B. 2/3", "C. 1/15", "D. 1/5", "E. 1/8"], "c": "E"},
        {"id": 14, "p": "Qual o domínio de definição da função $f(x)=\\sqrt{x-1} \\cdot \\ln(1-x^{2})$?", "opts": ["A. R", "B. ]-1,1[", "C. [1,+∞[", "D. {1}", "E. Conjunto Vazio"], "c": "E"},
        {"id": 15, "p": "A imagem da função $f(x)=5 \\cos(2x)+1$ encontra-se em:", "opts": ["A. [-1,1]", "B. [-5,5]", "C. [-4,6]", "D. [0,1]", "E. Nenhuma delas"], "c": "C"},
        {"id": 16, "p": "Uma função afim g(x) tem zero em x=3 e g(-2)=-5. Qual a sua expressão analítica?", "opts": ["A. g(x)=-x+3", "B. g(x)=-x+7", "C. g(x)=x^2-9", "D. g(x)=x-3", "E. g(x)=3x+1"], "c": "D"},
        {"id": 17, "p": "Considere $f(x)=-x^{2}+4$. Indique a afirmação verdadeira:", "opts": ["A. É monótona", "B. Tem domínio R", "C. É injectiva", "D. Tem um só zero", "E. Tem mínimo absoluto"], "c": "B"},
        {"id": 18, "p": "Qual a expressão de uma função com assímptotas verticais em x=-2, x=3 e horizontal em y=2?", "opts": ["A. (x-3)/(x-5)", "B. (-2x+3)/(x^2-x-6)", "C. x/(-2x^2-x-3)", "D. 2x/(-x+4)", "E. (2x^2+7)/(x^2-x-6)"], "c": "E"},
        {"id": 19, "p": "Se $f(x)=2^{x}-2$ e $g(x)=f(x+k)$ passa em (-4, -3/2), qual o valor de k?", "opts": ["A. 3", "B. -3", "C. 4", "D. -4", "E. 0"], "c": "A"},
        {"id": 20, "p": "Zeros da função composta $(f \\circ g^{-1})(x)$ sendo $f(x)=x^{2}-9$ e $g(x)=2x+4$:", "opts": ["A. {-2, 10}", "B. {-3, 2, 3}", "C. {-3, 0}", "D. {0}", "E. {1, 3}"], "c": "A"},
        {"id": 21, "p": "Numa P.A. $u_{5}+u_{6}=31$ e $u_{7}+u_{9}=46$. Determine $u_{1}$ e a razão r:", "opts": ["A. u1=1, r=3", "B. u1=-2, r=2", "C. u1=2, r=3", "D. u1=3, r=4", "E. u1=3, r=2"], "c": "C"},
        {"id": 22, "p": "Numa P.G. com $v_{5}=4$ e $v_{8}=108$, determine $v_{6}$:", "opts": ["A. 6", "B. 12", "C. 51", "D. 76", "E. 98"], "c": "B"},
        {"id": 23, "p": "A sucessão $u_{n} = \\log_{1/2}(3^{n})$ é uma:", "opts": ["A. P.A. Crescente", "B. P.A. Decrescente", "C. P.G. Crescente", "D. P.G. Decrescente", "E. Não é progressão"], "c": "B"},
        {"id": 24, "p": "Qual expressão representa uma sucessão convergente?", "opts": ["A. (-1)^n * n", "B. (-1)^n + n", "C. (-1)^n - n", "D. (-1)^n / n", "E. (-1)^n * n!"], "c": "D"},
        {"id": 25, "p": "Sobre a sucessão $v_{n}$ (n se n<10; 1+1/n se n≥10), indique a verdadeira:", "opts": ["A. Ilimitada", "B. Decrescente", "C. Crescente", "D. Divergente", "E. Limitada"], "c": "E"},
        {"id": 26, "p": "Limite de $(2n^{2}+3n+4)/(n^{2}+4)$ quando n tende ao infinito:", "opts": ["A. 0", "B. 1", "C. 2", "D. 3", "E. +∞"], "c": "C"},
        {"id": 27, "p": "Limite de $(1+1/n)^{2n}$ quando n tende ao infinito:", "opts": ["A. 1", "B. 2e", "C. e^2", "D. -∞", "E. +∞"], "c": "C"},
        {"id": 28, "p": "Valor de 'a' para que $f(x)$ (2-x se x<a; x^2+2 se x≥a) seja contínua:", "opts": ["A. -5", "B. -4", "C. -3/2", "D. -1", "E. -1/2"], "c": "D"},
        {"id": 29, "p": "Se $y=3x-5$ é assímptota oblíqua de g(x), então:", "opts": ["A. lim[g(x)+3x]=-5", "B. lim[g(x)+3x]=5", "C. lim[g(x)+3x-5]=0", "D. lim[g(x)-3x+5]=0", "E. Nenhuma"], "c": "D"},
        {"id": 30, "p": "Na figura (gráfico com salto em x=2), a afirmação verdadeira é:", "opts": ["A. Limite existe e é 2", "B. Limite não existe", "C. lim à esquerda = f(2)", "D. lim à direita = f(2)", "E. f é contínua"], "c": "B"},
        {"id": 31, "p": "Qual o valor do limite de $\\sin(2x)/x$ quando x tende a 0?", "opts": ["A. -1", "B. 0", "C. 1/2", "D. 1", "E. 2"], "c": "E"},
        {"id": 32, "p": "Limite de $[(5x-2)/x] - [(4x^{2}+2x+1)/(2x^{2}+1)]$ para x ao infinito:", "opts": ["A. -∞", "B. 0", "C. 3", "D. 9", "E. +∞"], "c": "C"},
        {"id": 33, "p": "A derivada da função $f(x) = \\ln(2x^2/3 + 2)$ é:", "opts": ["A. 2x^2/3 + 2", "B. 4x/3", "C. (2x^2+3)/4x", "D. (4x)/(2x^2+6)", "E. e^f(x)"], "c": "D"},
        {"id": 34, "p": "Se $g(x) = g'(x)$, qual destas expressões representa g(x)?", "opts": ["A. g(x)=5", "B. g(x)=3e^x", "C. g(x)=2cos(x)", "D. g(x)=x^2+1", "E. g(x)=√x"], "c": "B"},
        {"id": 35, "p": "Para que o declive da tangente a $y=kx^{2}+10x+1$ em x=2 seja 2, k vale:", "opts": ["A. 2", "B. -3", "C. 1/2", "D. -2", "E. 1/3"], "c": "D"},
        {"id": 36, "p": "Equação da recta tangente a $f(x)=\\sin(\\pi x)$ em x=1:", "opts": ["A. y=1", "B. y=1-x", "C. y=-πx", "D. y=\\pi-\\pi x", "E. y=\\pi x-1"], "c": "D"},
        {"id": 37, "p": "Sobre $f(x)=x^{3}-3x^{2}-24x+1$, qual está correcta?", "opts": ["A. Mín em x=4, Máx em x=-2", "B. Dois máximos", "C. Mín em x=2", "D. Mín em x=0, Máx em x=2", "E. Sem extremos"], "c": "A"},
        {"id": 38, "p": "A concavidade de f com $f'(x)=2xe^{1-x^2}$ está voltada para cima em:", "opts": ["A. ]-∞,-1[U]1,∞[", "B. ]-√2/2, √2/2[", "C. ]-∞, -√2/2[U]√2/2, ∞[", "D. ]-∞,0[", "E. R"], "c": "B"},
        {"id": 39, "p": "A primitiva da função $f(x) = e^{x}+1$ é:", "opts": ["A. 2e^x", "B. e^(x^2)/2", "C. e^x/2 + x", "D. xe^(x-1)+x", "E. e^x + x"], "c": "E"},
        {"id": 40, "p": "Resultado de $(3-2i) \\cdot (-4+i)$:", "opts": ["A. 10+2i", "B. 11i", "C. -12-2i", "D. -10+11i", "E. -10"], "c": "D"}
    ]

    # FÍSICA (41-80) - Enunciados Integrais
    f_qs = [
        {"id": 41, "p": "Um recipiente de vidro está quase cheio com água em temperatura ambiente. Ao colocá-lo sobre uma chama de fogão, a água começa a se aquecer por:", "opts": ["A. Condução", "B. irradiação", "C. convecção", "D. condução e convecção", "E. convecção e irradiação"], "c": "C"},
        {"id": 42, "p": "Quais são as características fundamentais capazes de distinguir um tipo de onda electromagnética de outro no vácuo?", "opts": ["A. Intensidade e velocidade", "B. Frequência e comprimento de onda", "C. Amplitude e polarização", "D. Altura e timbre", "E. Apenas amplitude"], "c": "B"},
        {"id": 43, "p": "Um transmissor de rádio opera a 20 MHz. Qual é o comprimento de onda do transmissor?", "opts": ["A. 15 m", "B. 25 m", "C. 35 m", "D. 45 m", "E. 55 m"], "c": "A"},
        {"id": 44, "p": "Um corpo de 100g recebeu 1250 cal ao ser aquecido de 30°C a 80°C. O calor específico é:", "opts": ["A. 0.025", "B. 2.50", "C. 2,5", "D. 25", "E. 0,25 cal/g.°C"], "c": "E"},
        {"id": 45, "p": "Lâmpada de corpo negro com T=3000K. Comprimento de onda de emissão máxima (nm): (b=2,9x10^-3 mK)", "opts": ["A. 966", "B. 765", "C. 438", "D. 350", "E. 320"], "c": "A"},
        {"id": 46, "p": "O gráfico representa a emissividade de corpos X, Y e Z. Qual é o menos quente?", "opts": ["A. Ty=Tx", "B. Ty", "C. Tz", "D. Tz=Ty", "E. Tx"], "c": "B"},
        {"id": 47, "p": "Estrela com área de 1/10 * 10^15 m² e potência de 24,3x10^23 W. Temperatura (K):", "opts": ["A. 19000", "B. 24000", "C. 28000", "D. 30000", "E. 34000"], "c": "A"},
        {"id": 48, "p": "Energia de fotões de raios X com comprimento de onda de 1,0x10^-10 m:", "opts": ["A. 5,99x10^-15J", "B. 4,99x10^-15J", "C. 3,99x10^-15J", "D. 2,99x10^-15J", "E. 1,99x10^-15J"], "c": "E"},
        {"id": 49, "p": "Variação de energia de um átomo ao absorver um quantum com λ = 198,6 nm:", "opts": ["A. 0.25x10^-18J", "B. 0.5x10^-18J", "C. 1x10^-18J", "D. 2x10^-18J", "E. 3x10^-18J"], "c": "C"},
        {"id": 50, "p": "O efeito fotoeléctrico ocorre devido à interação entre:", "opts": ["A. Protões e electrões", "B. Fotões e electrões", "C. Electrões e electrões", "D. Fotões e fotões", "E. Protões e fotões"], "c": "B"},
        {"id": 51, "p": "Número de fotões (λ=0,5µm, P=2x10^-17W) que entram no olho por segundo:", "opts": ["A. 50", "B. 70", "C. 100", "D. 120", "E. 140"], "c": "A"},
        {"id": 52, "p": "Número de fotões de energias diferentes que um átomo de H emite na 3ª órbita:", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "c": "C"},
        {"id": 53, "p": "Energia cinética de electrões acelerados por 5000 V:", "opts": ["A. 2,0x10^-16J", "B. 4,0x10^-16J", "C. 6,0x10^-16J", "D. 8,0x10^-16J", "E. 10,0x10^-16J"], "c": "D"},
        {"id": 54, "p": "Tensão (kV) para frequência máxima de raios X de 3x10^19 Hz:", "opts": ["A. 124", "B. 130", "C. 132", "D. 140", "E. 142"], "c": "A"},
        {"id": 55, "p": "No diagrama de níveis, qual transição emite fotão com maior momento linear?", "opts": ["A. Transição 1", "B. Transição 2", "C. Transição 3", "D. Transição 4", "E. Transição 5"], "c": "A"},
        {"id": 56, "p": "A radioactividade é consequência de:", "opts": ["A. Energia térmica", "B. Alterações no núcleo", "C. Escape de electrões", "D. Rupturas químicas", "E. Reorganização atômica"], "c": "B"},
        {"id": 57, "p": "Sobre as radiações, é correto afirmar que:", "opts": ["A. Alfa é 2p+2n", "B. Beta são positrões", "C. Gama é massa pura", "D. Alfa são neutrões", "E. Beta são electrões do núcleo"], "c": "E"},
        {"id": 58, "p": "Quantos neutrões tem o núcleo de 208/83 Bi?", "opts": ["A. 83", "B. 125", "C. 208", "D. 291", "E. 308"], "c": "B"},
        {"id": 59, "p": "Na reacção 27/13Al + gama -> 26/12Mg + X, X é:", "opts": ["A. Alumínio", "B. Oxigénio", "C. Carbono", "D. Hidrogénio", "E. Hélio"], "c": "D"},
        {"id": 60, "p": "Radiação que atinge o ponto 3 no experimento do bloco de chumbo:", "opts": ["A. Infravermelha", "B. Ultravioleta", "C. Alfa", "D. Beta", "E. Gama"], "c": "D"},
        {"id": 61, "p": "Qual reação representa a fissão nuclear (lixo radioativo)?", "opts": ["A. Fusão solar", "B. Decaimento beta", "C. Cadeia U-235", "D. Emissão gama", "E. Fusão de H"], "c": "C"},
        {"id": 62, "p": "Energia de ligação por nucleão (A=20, Energia Total = 160 MeV):", "opts": ["A. 4", "B. 8", "C. 16", "D. 32", "E. 40"], "c": "B"},
        {"id": 63, "p": "Energia libertada em fusão com defeito de massa de 0,02 uma:", "opts": ["A. 14,6", "B. 15,6", "C. 16,6", "D. 17,6", "E. 18,6 MeV"], "c": "E"},
        {"id": 64, "p": "Na reacção: n + U235 -> Cs144 + T + 2n, quais os números de T?", "opts": ["A. 37 e 90", "B. 38 e 91", "C. 39 e 90", "D. 40 e 91", "E. 41 e 90"], "c": "A"},
        {"id": 65, "p": "Tempo para Iodo-131 (meia-vida 8 dias) chegar a 1/16 da massa inicial:", "opts": ["A. 8 dias", "B. 16 dias", "C. 24 dias", "D. 32 dias", "E. 40 dias"], "c": "D"},
        {"id": 66, "p": "Relação entre as vazões Q nas secções 1, 2 e 3 de um tubo:", "opts": ["A. Q1<Q2<Q3", "B. Q1>Q2>Q3", "C. Q1=Q2=Q3", "D. Q1+Q2=Q3", "E. Q1=Q2+Q3"], "c": "C"},
        {"id": 67, "p": "Velocidade do gás na saída sabendo P1=8atm, v1=10m/s e P2=1atm:", "opts": ["A. 40", "B. 50", "C. 60", "D. 70", "E. 80 m/s"], "c": "B"},
        {"id": 68, "p": "Velocidade v2 em tubo com v1=3m/s, r1=0,1m e r2=0,05m:", "opts": ["A. 6", "B. 9", "C. 12", "D. 15", "E. 18 m/s"], "c": "C"},
        {"id": 69, "p": "Vazão (dm³/s) de torneira que enche 12000L em 40 minutos:", "opts": ["A. 5", "B. 10", "C. 15", "D. 20", "E. 25"], "c": "A"},
        {"id": 70, "p": "Força em prensa hidráulica (A1=4m², A2=0,0025m²) para levantar 1000kg:", "opts": ["A. 4,25", "B. 5,25", "C. 6,25", "D. 7,25", "E. 8,25 N"], "c": "C"},
        {"id": 71, "p": "Velocidade para encher piscina (18x10x2m) em 10h com conduto de 25cm²:", "opts": ["A. 2", "B. 4", "C. 6", "D. 8", "E. 10 m/s"], "c": "B"},
        {"id": 72, "p": "Número de moles em recipiente cúbico (0,5m), P=59760Pa, T=300K:", "opts": ["A. 3", "B. 5", "C. 7", "D. 9", "E. 11"], "c": "A"},
        {"id": 73, "p": "Processos no gráfico V vs T (1->2, 2->3, 3->1):", "opts": ["A. Isobárica, Isovolumétrica", "B. Isovolumétrica, Isobárica, Isotérmica", "C. Isotérmica, Isobárica", "D. Adiabática", "E. Cíclica"], "c": "B"},
        {"id": 74, "p": "Volume de H a 293K (inicial 0,15L a 300K, P constante):", "opts": ["A. 0,10", "B. 0,12", "C. 0,14", "D. 0,15", "E. 0,16 L"], "c": "C"},
        {"id": 75, "p": "Qual representação de processos em gases ideais é FALSA?", "opts": ["A", "B", "C", "D", "E"], "c": "E"},
        {"id": 76, "p": "Variação de energia interna total (Q1=500, W1=200; Q2=-300, W2=-100):", "opts": ["A. 50", "B. 100", "C. 150", "D. 200", "E. 250 J"], "c": "B"},
        {"id": 77, "p": "Trabalho em expansão adiabática que recebe 10 kJ de energia interna:", "opts": ["A. 0", "B. 5", "C. 10", "D. 15", "E. 20 kJ"], "c": "C"},
        {"id": 78, "p": "Trabalho total no ciclo XY-YZ-ZX do gráfico p vs V:", "opts": ["A. 1,6x10^5", "B. 2,0x10^5", "C. 3,2x10^5", "D. 4,8x10^5", "E. 0 J"], "c": "A"},
        {"id": 79, "p": "Período e amplitude de massa 0,2kg, k=0,8pi² N/m, afastada 3cm:", "opts": ["A. 0,5s e 2cm", "B. 1,0s e 3cm", "C. 1,5s e 4cm", "D. 2,0s e 5cm", "E. 2,5s e 6cm"], "c": "B"},
        {"id": 80, "p": "Amplitude de aceleração do corpo no gráfico MHS:", "opts": ["A. pi²", "B. 2pi²", "C. 3pi²", "D. 4pi²", "E. 5pi²"], "c": "B"}
    ]

    # Mesclagem Intercalada (M1, F41, M2, F42...)
    lista_final = []
    for m, f in zip(m_qs, f_qs):
        lista_final.append(m)
        lista_final.append(f)
    st.session_state.perguntas = lista_final

# 3. Estados de Controle
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False

# 4. Interface Principal
st.title("📚 Simulador Integrado UEM 2025")
st.sidebar.markdown("### Progresso do Exame")
st.sidebar.progress((st.session_state.i + 1) / 80)
if st.sidebar.button("⚠️ Reiniciar Simulado"):
    reset_perguntas()

if not st.session_state.quiz_fim:
    q = st.session_state.perguntas[st.session_state.i]
    
    # Identificador de Disciplina
    tipo = "📐 MATEMÁTICA" if q['id'] <= 40 else "⚡ FÍSICA"
    st.info(f"Questão {st.session_state.i + 1} de 80 | **{tipo}** (ID Original: {q['id']})")
    
    # Exibição do Enunciado
    st.markdown(f"#### {q['p']}")
    
    # Opções com preservação de estado
    marcada = st.session_state.respostas.get(st.session_state.i, None)
    idx_radio = 0
    if marcada:
        for idx, opt in enumerate(q["opts"]):
            if opt.startswith(marcada): idx_radio = idx

    escolha = st.radio("Selecione a alternativa:", q["opts"], index=idx_radio, key=f"rad_{st.session_state.i}")

    # Botões de Navegação
    st.divider()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⬅️ Anterior", disabled=(st.session_state.i == 0), use_container_width=True):
            st.session_state.i -= 1
            st.rerun()
            
    with col2:
        if st.button("💾 Salvar Resposta", use_container_width=True, type="primary"):
            st.session_state.respostas[st.session_state.i] = escolha[0]
            st.toast(f"Resposta {escolha[0]} salva!")
            
    with col3:
        txt_next = "Finalizar 🏁" if st.session_state.i == 79 else "Próxima ➡️"
        if st.button(txt_next, use_container_width=True):
            st.session_state.respostas[st.session_state.i] = escolha[0]
            if st.session_state.i < 79:
                st.session_state.i += 1
                st.rerun()
            else:
                st.session_state.quiz_fim = True
                st.rerun()

else:
    # Fim do Exame - Resultados
    st.success("🎉 Simulado concluído com sucesso!")
    
    # Cálculo
    acertos = sum(1 for idx, quest in enumerate(st.session_state.perguntas) if st.session_state.respostas.get(idx) == quest["c"])
    nota = (acertos / 80) * 20
    
    c1, c2 = st.columns(2)
    c1.metric("Acertos", f"{acertos} / 80")
    c2.metric("Nota Estimada", f"{nota:.2f} / 20")

    # Correção Detalhada
    with st.expander("🔍 Ver Correção Detalhada"):
        for idx, quest in enumerate(st.session_state.perguntas):
            resp_u = st.session_state.respostas.get(idx, "N/A")
            correta = quest["c"]
            cor = "green" if resp_u == correta else "red"
            st.markdown(f"**Q{quest['id']}:** {quest['p']}")
            st.markdown(f"Sua resposta: :{cor}[{resp_u}] | Correta: **{correta}**")
            st.divider()
