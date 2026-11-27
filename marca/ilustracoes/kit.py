"""Kit de ilustrações da Seja Creator.

Peças reutilizáveis para montar cenas no estilo da marca: pessoas em busto, de frente,
sem rosto, em formas chapadas; objetos e ícones das plataformas. Tudo vira SVG puro
(sem <style>, sem texto, sem degradê, sem sombra), com as cores da marca.

Leia marca/ilustracoes/ILUSTRACOES.md antes de usar. Cenas prontas: cenas.py.
"""
import math

# Cores da marca (iguais ao design system)
ROXO = "#8338EB"; ROSA = "#FF006E"; AZUL = "#3A86FE"; LARANJA = "#FB5507"; AMARELO = "#FFBE0C"
TEXTO = "#1A1A2E"; BRANCO = "#FFFFFF"; CLARO = "#F5F4F8"
# Apoio só para ilustração: tons claros da própria paleta
LILAS = "#EDE3FF"; LILAS_MEDIO = "#B78BF5"; ROSA_CLARO = "#FFC2DA"
CABELO_CASTANHO = "#8A4B2A"

# Tons de pele: variar sempre que houver mais de uma pessoa
PELES = {"escura": "#6B4226", "media": "#A0673E", "morena": "#C68642", "clara": "#F1C9A5"}


def svg(w, h, corpo, titulo=None):
    """Documento SVG final. `titulo` vira <title> (acessibilidade quando usado inline)."""
    t = f"<title>{titulo}</title>" if titulo else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">{t}{corpo}</svg>')


# ---------------------------------------------------------------- pessoas
def pessoa(cx, cy, s=1.0, pele=PELES["morena"], roupa=ROXO, cabelo="cacheado", cor_cabelo=TEXTO,
           oculos=None, brinco=None, fone=None, pose=None, objeto=None, espelhar=False, barba=False):
    """Pessoa em busto, de frente, sem rosto. Molde único: só mudam os atributos.

    (cx, cy): centro da cabeça. Altura total ~ 400*s (cabelo até o fim do tronco).
    cabelo: cacheado | coque | curto | branco | comprido
    pose: None | fala (mão levantada) | queixo (mão no queixo) | escreve
    objeto: None | caneca | celular
    espelhar: inverte a pessoa (a mão da pose passa para o outro lado).
    barba: True desenha barba na cor do cabelo (use para ter homens nas cenas; com cabelo "curto" ou "cacheado").
    Desenhe quem tem pose "fala" por último, para o braço ficar na frente das outras pessoas.
    """
    fx = -1 if espelhar else 1
    g = []
    if cabelo == "cacheado":
        g.append(f'<circle cx="0" cy="-12" r="74" fill="{cor_cabelo}"/>')
        g.append(f'<circle cx="-58" cy="26" r="30" fill="{cor_cabelo}"/>')
        g.append(f'<circle cx="58" cy="26" r="30" fill="{cor_cabelo}"/>')
    elif cabelo == "comprido":
        g.append(f'<path d="M -64 -6 Q -66 -74 0 -74 Q 66 -74 64 -6 L 70 120 Q 0 132 -70 120 Z" fill="{cor_cabelo}"/>')
    g.append(f'<path d="M -114 320 L -114 196 Q -114 112 -38 104 L 38 104 Q 114 112 114 196 L 114 320 Z" fill="{roupa}"/>')
    g.append(f'<rect x="-21" y="36" width="42" height="76" rx="12" fill="{pele}"/>')
    g.append(f'<circle cx="-50" cy="8" r="12" fill="{pele}"/><circle cx="50" cy="8" r="12" fill="{pele}"/>')
    g.append(f'<ellipse cx="0" cy="0" rx="50" ry="58" fill="{pele}"/>')
    if cabelo == "cacheado":
        for x, y, r in [(-34, -44, 24), (-6, -56, 26), (26, -50, 24), (46, -26, 18), (-48, -22, 18)]:
            g.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{cor_cabelo}"/>')
    elif cabelo == "coque":
        g.append(f'<circle cx="6" cy="-78" r="28" fill="{cor_cabelo}"/>')
        g.append(f'<path d="M -53 6 Q -58 -64 0 -64 Q 58 -64 53 6 Q 46 -32 4 -38 Q -36 -38 -53 6 Z" fill="{cor_cabelo}"/>')
    elif cabelo in ("curto", "branco"):
        c = CLARO if cabelo == "branco" else cor_cabelo
        g.append(f'<path d="M -54 10 Q -60 -70 2 -68 Q 62 -66 54 10 Q 50 -28 14 -34 Q -28 -42 -54 10 Z" fill="{c}"/>')
        if cabelo == "branco":
            g.append(f'<circle cx="-40" cy="-46" r="20" fill="{c}"/><circle cx="-8" cy="-62" r="22" fill="{c}"/><circle cx="28" cy="-56" r="20" fill="{c}"/>')
    elif cabelo == "comprido":
        g.append(f'<path d="M -54 8 Q -58 -66 2 -66 Q 60 -64 54 8 Q 30 -34 -12 -36 Q -40 -30 -54 8 Z" fill="{cor_cabelo}"/>')
    if barba:
        g.append(f'<path d="M -50 -2 Q -52 66 0 70 Q 52 66 50 -2 Q 44 26 22 30 Q 0 22 -22 30 Q -44 26 -50 -2 Z" fill="{cor_cabelo}"/>')
    if oculos:
        g.append(f'<circle cx="-20" cy="2" r="16" fill="none" stroke="{oculos}" stroke-width="6"/>'
                 f'<circle cx="22" cy="2" r="16" fill="none" stroke="{oculos}" stroke-width="6"/>'
                 f'<path d="M -4 2 L 6 2" stroke="{oculos}" stroke-width="6"/>')
    if brinco:
        g.append(f'<circle cx="-50" cy="32" r="9" fill="none" stroke="{brinco}" stroke-width="5"/>')
    if fone:
        g.append(f'<path d="M -60 6 Q -66 -80 0 -82 Q 66 -80 60 6" fill="none" stroke="{fone}" stroke-width="13" stroke-linecap="round"/>')
        g.append(f'<rect x="-74" y="-16" width="26" height="46" rx="12" fill="{fone}"/>')
        g.append(f'<rect x="48" y="-16" width="26" height="46" rx="12" fill="{fone}"/>')
    if pose == "fala":
        g.append(f'<path d="M 80 180 Q 156 170 160 40" fill="none" stroke="{roupa}" stroke-width="48" stroke-linecap="round"/>')
        g.append(f'<ellipse cx="164" cy="14" rx="26" ry="30" fill="{pele}"/>')
        g.append(f'<path d="M 150 -6 Q 180 -26 198 -8" fill="none" stroke="{pele}" stroke-width="14" stroke-linecap="round"/>')
    elif pose == "queixo":
        g.append(f'<path d="M 70 330 L 46 112" fill="none" stroke="{roupa}" stroke-width="46" stroke-linecap="round"/>')
        g.append(f'<ellipse cx="38" cy="78" rx="24" ry="28" fill="{pele}"/>')
    elif pose == "escreve":
        g.append(f'<path d="M -60 210 Q -30 300 40 300" fill="none" stroke="{roupa}" stroke-width="44" stroke-linecap="round"/>')
        g.append(f'<ellipse cx="54" cy="298" rx="24" ry="20" fill="{pele}"/>')
        g.append(f'<path d="M 50 300 L 92 240" stroke="{TEXTO}" stroke-width="9" stroke-linecap="round"/>')
    if objeto == "caneca":
        g.append(f'<path d="M 62 300 Q 124 290 122 190" fill="none" stroke="{roupa}" stroke-width="44" stroke-linecap="round"/>')
        g.append(f'<rect x="96" y="104" width="64" height="74" rx="10" fill="{AMARELO}"/>'
                 f'<path d="M 160 120 Q 186 124 182 146 Q 178 164 160 162" fill="none" stroke="{AMARELO}" stroke-width="10"/>'
                 f'<ellipse cx="124" cy="176" rx="26" ry="22" fill="{pele}"/>')
    elif objeto == "celular":
        g.append(f'<path d="M 62 300 Q 126 290 124 160" fill="none" stroke="{roupa}" stroke-width="44" stroke-linecap="round"/>')
        g.append(f'<rect x="100" y="40" width="70" height="120" rx="14" fill="{TEXTO}"/>'
                 f'<rect x="108" y="52" width="54" height="86" rx="6" fill="{LILAS}"/>'
                 f'<path d="M 128 80 L 128 110 L 150 95 Z" fill="{ROXO}"/>'
                 f'<ellipse cx="126" cy="156" rx="26" ry="22" fill="{pele}"/>')
    return f'<g transform="translate({cx},{cy}) scale({s * fx},{s})">' + "".join(g) + "</g>"


# ---------------------------------------------------------------- detalhes
def brilhos(cx, cy, cor=AMARELO, n=3, ang0=-150, abertura=50, raio=0, comprimento=34, espessura=9):
    """Tracinhos de destaque em volta de um ponto (como na referência)."""
    out = []
    for i in range(n):
        a = math.radians(ang0 + i * abertura / max(n - 1, 1))
        x1, y1 = cx + raio * math.cos(a), cy + raio * math.sin(a)
        x2, y2 = cx + (raio + comprimento) * math.cos(a), cy + (raio + comprimento) * math.sin(a)
        out.append(f'<path d="M {x1:.0f} {y1:.0f} L {x2:.0f} {y2:.0f}" stroke="{cor}" '
                   f'stroke-width="{espessura}" stroke-linecap="round"/>')
    return "".join(out)


def fio(x1, y1, x2, y2, curva=0.25, cor=BRANCO, espessura=5):
    """Linha curva que liga duas peças (ideia → plataformas)."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    qx, qy = mx - dy * curva, my + dx * curva
    return (f'<path d="M {x1:.0f} {y1:.0f} Q {qx:.0f} {qy:.0f} {x2:.0f} {y2:.0f}" fill="none" '
            f'stroke="{cor}" stroke-width="{espessura}" stroke-linecap="round"/>')


# ---------------------------------------------------------------- ícones das plataformas
def icone_podcast(cx, cy, r=110):
    """Microfone com fone de ouvido, num círculo branco."""
    k = r / 110
    def p(v): return v * k
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BRANCO}"/>'
            f'<path d="M {cx-p(62)} {cy+p(8)} Q {cx-p(64)} {cy-p(74)} {cx} {cy-p(76)} Q {cx+p(64)} {cy-p(74)} {cx+p(62)} {cy+p(8)}" fill="none" stroke="{ROXO}" stroke-width="{p(12)}" stroke-linecap="round"/>'
            f'<rect x="{cx-p(80)}" y="{cy-p(16)}" width="{p(30)}" height="{p(56)}" rx="{p(14)}" fill="{ROSA}"/>'
            f'<rect x="{cx+p(50)}" y="{cy-p(16)}" width="{p(30)}" height="{p(56)}" rx="{p(14)}" fill="{ROSA}"/>'
            f'<rect x="{cx-p(22)}" y="{cy-p(50)}" width="{p(44)}" height="{p(78)}" rx="{p(22)}" fill="{BRANCO}" stroke="{TEXTO}" stroke-width="{p(7)}"/>'
            f'<path d="M {cx-p(12)} {cy-p(28)} L {cx+p(12)} {cy-p(28)} M {cx-p(12)} {cy-p(14)} L {cx+p(12)} {cy-p(14)} M {cx-p(12)} {cy} L {cx+p(12)} {cy}" stroke="{ROXO}" stroke-width="{p(6)}" stroke-linecap="round"/>'
            f'<path d="M {cx-p(36)} {cy+p(6)} Q {cx-p(36)} {cy+p(48)} {cx} {cy+p(48)} Q {cx+p(36)} {cy+p(48)} {cx+p(36)} {cy+p(6)}" fill="none" stroke="{TEXTO}" stroke-width="{p(7)}" stroke-linecap="round"/>'
            f'<path d="M {cx} {cy+p(48)} L {cx} {cy+p(70)} M {cx-p(22)} {cy+p(72)} L {cx+p(22)} {cy+p(72)}" stroke="{TEXTO}" stroke-width="{p(7)}" stroke-linecap="round"/>')


def icone_ideia(cx, cy, r=86):
    """Lâmpada acesa num círculo branco: a pesquisa / a ideia no centro."""
    k = r / 86
    def p(v): return v * k
    raios = "".join(
        f'<path d="M {cx + p(40)*math.cos(math.radians(a)):.0f} {cy - p(8) + p(40)*math.sin(math.radians(a)):.0f} '
        f'L {cx + p(58)*math.cos(math.radians(a)):.0f} {cy - p(8) + p(58)*math.sin(math.radians(a)):.0f}" '
        f'stroke="{LARANJA}" stroke-width="{p(7)}" stroke-linecap="round"/>'
        for a in (-150, -115, -90, -65, -30))
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BRANCO}"/>' + raios +
            f'<circle cx="{cx}" cy="{cy-p(8)}" r="{p(26)}" fill="{AMARELO}"/>'
            f'<rect x="{cx-p(14)}" y="{cy+p(12)}" width="{p(28)}" height="{p(14)}" rx="{p(4)}" fill="{AMARELO}"/>'
            f'<rect x="{cx-p(13)}" y="{cy+p(28)}" width="{p(26)}" height="{p(8)}" rx="{p(4)}" fill="{ROXO}"/>'
            f'<rect x="{cx-p(9)}" y="{cy+p(38)}" width="{p(18)}" height="{p(8)}" rx="{p(4)}" fill="{ROXO}"/>')


def icone_video(x, y, w=230, h=150):
    """Player de vídeo: cartão branco, tela roxa, play e barra de progresso."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{BRANCO}"/>'
            f'<rect x="{x+16}" y="{y+16}" width="{w-32}" height="{h-32}" rx="12" fill="{ROXO}"/>'
            f'<path d="M {x+w/2-18} {y+h/2-30} L {x+w/2-18} {y+h/2+14} L {x+w/2+22} {y+h/2-8} Z" fill="{BRANCO}"/>'
            f'<path d="M {x+36} {y+h-36} L {x+w-36} {y+h-36}" stroke="{LILAS}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M {x+36} {y+h-36} L {x+w*0.45} {y+h-36}" stroke="{AMARELO}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cx="{x+w*0.45}" cy="{y+h-36}" r="10" fill="{AMARELO}"/>')


def icone_celular(x, y, w=120, h=200, pele=PELES["media"]):
    """Celular com vídeo vertical (reels/shorts): uma pessoa e o play."""
    cx = x + w / 2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24" fill="{ROXO}"/>'
            f'<rect x="{x+12}" y="{y+16}" width="{w-24}" height="{h-32}" rx="12" fill="{LILAS_MEDIO}"/>'
            f'<clipPath id="tela-cel-{x}-{y}"><rect x="{x+12}" y="{y+16}" width="{w-24}" height="{h-32}" rx="12"/></clipPath>'
            f'<g clip-path="url(#tela-cel-{x}-{y})">{pessoa(cx, y + h*0.42, 0.34, pele, AMARELO, "coque", TEXTO)}</g>'
            f'<circle cx="{cx}" cy="{y+h-40}" r="16" fill="{BRANCO}"/>'
            f'<path d="M {cx-5} {y+h-48} L {cx-5} {y+h-32} L {cx+8} {y+h-40} Z" fill="{ROXO}"/>')


def icone_post(x, y, w=170, h=130):
    """Post de imagem (carrossel): três cartões empilhados, montanha e sol."""
    return (f'<rect x="{x+34}" y="{y+26}" width="{w}" height="{h}" rx="16" fill="{LILAS_MEDIO}"/>'
            f'<rect x="{x+17}" y="{y+13}" width="{w}" height="{h}" rx="16" fill="{ROSA_CLARO}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{BRANCO}"/>'
            f'<path d="M {x+20} {y+h-20} L {x+w*0.38} {y+h*0.45} L {x+w*0.56} {y+h*0.68} L {x+w*0.7} {y+h*0.52} L {x+w-20} {y+h-20} Z" fill="{ROXO}"/>'
            f'<circle cx="{x+w*0.72}" cy="{y+h*0.3}" r="{h*0.12:.0f}" fill="{AMARELO}"/>')


def icone_pagina(x, y, w=230, h=170):
    """Página de site / blog / newsletter: janela com linhas de texto e envelope."""
    linhas = "".join(
        f'<path d="M {x+110} {y+56+i*24} L {x+w-24 - (30 if i % 2 else 0)} {y+56+i*24}" stroke="{LILAS_MEDIO}" stroke-width="9" stroke-linecap="round"/>'
        for i in range(4))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{BRANCO}"/>'
            f'<path d="M {x} {y+18} Q {x} {y} {x+18} {y} L {x+w-18} {y} Q {x+w} {y} {x+w} {y+18} L {x+w} {y+34} L {x} {y+34} Z" fill="{ROXO}"/>'
            f'<circle cx="{x+20}" cy="{y+17}" r="5" fill="{BRANCO}"/><circle cx="{x+36}" cy="{y+17}" r="5" fill="{BRANCO}"/><circle cx="{x+52}" cy="{y+17}" r="5" fill="{BRANCO}"/>'
            f'<rect x="{x+22}" y="{y+50}" width="72" height="56" rx="8" fill="{LILAS_MEDIO}"/>'
            + linhas +
            f'<rect x="{x+w-74}" y="{y+h-46}" width="92" height="64" rx="10" fill="{AMARELO}"/>'
            f'<path d="M {x+w-64} {y+h-36} L {x+w-28} {y+h-6} L {x+w+8} {y+h-36}" fill="none" stroke="{ROXO}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')


def mesa(x, y, w, h=220):
    """Mesa branca em que o grupo se reúne (geralmente sangrando pela borda de baixo)."""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="44" fill="{BRANCO}"/>'


def notebook_costas(cx, y, w=200, h=130):
    """Notebook aberto visto por trás, com o ponto amarelo no centro."""
    return (f'<rect x="{cx-w/2}" y="{y}" width="{w}" height="{h}" rx="14" fill="{TEXTO}"/>'
            f'<circle cx="{cx}" cy="{y+h*0.48}" r="{w*0.07:.0f}" fill="{AMARELO}"/>'
            f'<rect x="{cx-w/2-20}" y="{y+h-6}" width="{w+40}" height="18" rx="8" fill="{TEXTO}"/>')


def livros(x, y):
    return (f'<rect x="{x}" y="{y+50}" width="150" height="26" rx="8" fill="{ROXO}"/>'
            f'<rect x="{x+10}" y="{y+24}" width="130" height="26" rx="8" fill="{AMARELO}"/>'
            f'<rect x="{x+14}" y="{y}" width="120" height="24" rx="8" fill="{LILAS_MEDIO}"/>')


def caneca(x, y, cor=AMARELO):
    return (f'<rect x="{x}" y="{y}" width="64" height="70" rx="10" fill="{cor}"/>'
            f'<path d="M {x+64} {y+16} Q {x+92} {y+18} {x+88} {y+40} Q {x+84} {y+58} {x+64} {y+56}" fill="none" stroke="{cor}" stroke-width="10"/>')


def balao(x, y, w, h, cor=BRANCO, ponta="baixo-esquerda", pontos=ROSA):
    """Balão de fala com reticências (conversa). ponta: baixo-esquerda | baixo-direita."""
    if ponta == "baixo-esquerda":
        cauda = f'<path d="M {x+w*0.2} {y+h-4} L {x+w*0.12} {y+h+34} L {x+w*0.38} {y+h-4} Z" fill="{cor}"/>'
    else:
        cauda = f'<path d="M {x+w*0.8} {y+h-4} L {x+w*0.88} {y+h+34} L {x+w*0.62} {y+h-4} Z" fill="{cor}"/>'
    r = min(w, h) * 0.11
    dots = "".join(f'<circle cx="{x + w*(0.3 + 0.2*i):.0f}" cy="{y + h/2:.0f}" r="{r:.0f}" fill="{pontos}"/>' for i in range(3)) if pontos else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*0.34:.0f}" fill="{cor}"/>' + cauda + dots


def interrogacao(cx, cy, tam=40, cor=ROSA):
    """Ponto de interrogação desenhado (sem texto), para balões de dúvida. tam = altura total."""
    k = tam / 40
    def p(v): return v * k
    return (f'<path d="M {cx-p(10)} {cy-p(10)} Q {cx-p(10)} {cy-p(20)} {cx} {cy-p(20)} Q {cx+p(11)} {cy-p(20)} {cx+p(11)} {cy-p(9)} '
            f'Q {cx+p(11)} {cy-p(2)} {cx+p(3)} {cy+p(2)} Q {cx} {cy+p(4)} {cx} {cy+p(9)}" fill="none" stroke="{cor}" '
            f'stroke-width="{p(7)}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy+p(18)}" r="{p(4.2)}" fill="{cor}"/>')


# ---------------------------------------------------------------- peças para ícones e cenas novas
def relogio(cx, cy, r=40, cor=BRANCO, ponteiro=TEXTO):
    """Relógio de parede: falta de tempo, rotina."""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{cor}"/>'
            f'<path d="M {cx} {cy} L {cx} {cy-r*0.6:.0f} M {cx} {cy} L {cx+r*0.45:.0f} {cy+r*0.2:.0f}" stroke="{ponteiro}" '
            f'stroke-width="{max(r*0.14, 3):.0f}" stroke-linecap="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{max(r*0.1, 2.5):.0f}" fill="{ponteiro}"/>')


def documento(x, y, w=90, h=116, cor=BRANCO, linhas=LILAS_MEDIO, selo=None):
    """Folha com linhas de texto (projeto, relatório, edital). selo: cor do selo redondo com check."""
    out = (f'<path d="M {x} {y+10} Q {x} {y} {x+10} {y} L {x+w*0.72:.0f} {y} L {x+w} {y+h*0.22:.0f} L {x+w} {y+h-10} '
           f'Q {x+w} {y+h} {x+w-10} {y+h} L {x+10} {y+h} Q {x} {y+h} {x} {y+h-10} Z" fill="{cor}"/>'
           f'<path d="M {x+w*0.72:.0f} {y} L {x+w*0.72:.0f} {y+h*0.22:.0f} L {x+w} {y+h*0.22:.0f} Z" fill="{LILAS}"/>')
    for i, f in enumerate((0.62, 0.5, 0.62, 0.38)):
        yy = y + h * 0.34 + i * h * 0.13
        out += f'<path d="M {x+w*0.14:.0f} {yy:.0f} L {x+w*(0.14+f):.0f} {yy:.0f}" stroke="{linhas}" stroke-width="{h*0.055:.0f}" stroke-linecap="round"/>'
    if selo:
        sx, sy, sr = x + w * 0.82, y + h * 0.86, w * 0.26
        out += (f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="{sr:.0f}" fill="{selo}"/>'
                f'<path d="M {sx-sr*0.42:.0f} {sy:.0f} L {sx-sr*0.08:.0f} {sy+sr*0.34:.0f} L {sx+sr*0.46:.0f} {sy-sr*0.3:.0f}" '
                f'fill="none" stroke="{BRANCO}" stroke-width="{sr*0.22:.0f}" stroke-linecap="round" stroke-linejoin="round"/>')
    return out


def coracao(cx, cy, s=30, cor=ROSA):
    """Coração (curtida, reação do público). s = largura."""
    k = s / 30
    return (f'<path d="M {cx} {cy+12*k:.1f} C {cx-18*k:.1f} {cy+1*k:.1f} {cx-15*k:.1f} {cy-14*k:.1f} {cx-6*k:.1f} {cy-13*k:.1f} '
            f'C {cx-2*k:.1f} {cy-13*k:.1f} {cx} {cy-9*k:.1f} {cx} {cy-7*k:.1f} C {cx} {cy-9*k:.1f} {cx+2*k:.1f} {cy-13*k:.1f} {cx+6*k:.1f} {cy-13*k:.1f} '
            f'C {cx+15*k:.1f} {cy-14*k:.1f} {cx+18*k:.1f} {cy+1*k:.1f} {cx} {cy+12*k:.1f} Z" fill="{cor}"/>')


def tripe_celular(cx, y_tela, altura=230):
    """Celular de pé num tripé, gravando (bolinha rosa de gravação). y_tela = topo do celular."""
    return (f'<path d="M {cx} {y_tela+120} L {cx-46} {y_tela+altura} M {cx} {y_tela+120} L {cx+46} {y_tela+altura} '
            f'M {cx} {y_tela+120} L {cx} {y_tela+altura}" stroke="{TEXTO}" stroke-width="9" stroke-linecap="round"/>'
            f'<rect x="{cx-40}" y="{y_tela}" width="80" height="128" rx="14" fill="{TEXTO}"/>'
            f'<rect x="{cx-32}" y="{y_tela+10}" width="64" height="98" rx="8" fill="{LILAS}"/>'
            f'<circle cx="{cx}" cy="{y_tela+58}" r="16" fill="{ROSA}"/>'
            f'<circle cx="{cx}" cy="{y_tela+58}" r="7" fill="{BRANCO}"/>')


def janela(x, y, w, h, id_clip, fundo=LILAS, conteudo="", barra=ROXO):
    """Janela de vídeo/rede social com o que estiver dentro recortado pela tela.
    conteudo: SVG desenhado dentro (ex.: uma pessoa). id_clip precisa ser único na cena."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{BRANCO}"/>'
            f'<circle cx="{x+20}" cy="{y+18}" r="5" fill="{barra}"/><circle cx="{x+36}" cy="{y+18}" r="5" fill="{AMARELO}"/>'
            f'<clipPath id="{id_clip}"><rect x="{x+12}" y="{y+34}" width="{w-24}" height="{h-46}" rx="12"/></clipPath>'
            f'<rect x="{x+12}" y="{y+34}" width="{w-24}" height="{h-46}" rx="12" fill="{fundo}"/>'
            f'<g clip-path="url(#{id_clip})">{conteudo}</g>')

