"""Cenas prontas da Seja Creator, montadas com o kit.

Rodar:  python3 marca/ilustracoes/cenas.py
Gera os SVG em public/assets/ e prévias PNG em marca/ilustracoes/previas/
(sobre a cor de fundo em que cada cena vai aparecer). Abra as prévias antes de usar.
Mudou o desenho de uma cena já publicada? Suba o número da versão no nome do arquivo.
"""
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa: E402,F403

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ASSETS = os.path.join(RAIZ, "public", "assets")
PREVIAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "previas")


def home_topo():
    """Home, primeiro bloco: o grupo de pesquisa em volta da mesa e, acima, a ideia
    ligada às plataformas (vídeo, reels, podcast, post, site/newsletter).
    Fundo: bg1 (degradê azul→roxo do hero). A mesa encosta na seção branca seguinte."""
    W, H = 1200, 680
    ideia = (600, 250)
    c = []
    # fios primeiro, para ficarem atrás das peças
    for alvo in [(318, 292), (390, 236), (600, 148), (806, 196), (892, 300)]:
        c.append(fio(ideia[0], ideia[1], alvo[0], alvo[1], curva=0.18))
    c.append(icone_video(90, 215))
    c.append(icone_celular(330, 40))
    c.append(icone_podcast(600, 82, 66))
    c.append(icone_post(780, 70))
    c.append(icone_pagina(890, 215))
    c.append(icone_ideia(*ideia, r=78))
    c.append(brilhos(390, 140, AMARELO, 3, -165, 55, 112, 26, 8))
    c.append(brilhos(600, 82, AMARELO, 3, -25, 50, 80, 24, 8))
    c.append(brilhos(205, 290, AMARELO, 3, 150, 50, 132, 26, 8))
    c.append(brilhos(1005, 300, AMARELO, 2, -60, 40, 130, 26, 8))
    # o grupo (quem fala por último, para o braço ficar na frente)
    c.append(pessoa(300, 450, 0.82, PELES["escura"], AMARELO, "cacheado", TEXTO, brinco=BRANCO, pose="queixo"))
    c.append(pessoa(705, 455, 0.82, PELES["media"], LARANJA, "coque", TEXTO, brinco=AMARELO, pose="escreve"))
    c.append(pessoa(905, 450, 0.82, PELES["morena"], BRANCO, "cacheado", TEXTO, fone=ROSA, pose="queixo", espelhar=True))
    c.append(pessoa(490, 445, 0.82, PELES["clara"], ROSA, "branco", oculos=ROXO, pose="fala"))
    c.append(mesa(170, 600, 860, 200))
    c.append(livros(240, 524))
    c.append(notebook_costas(800, 492, 170, 112))
    c.append(f'<path d="M 520 650 L 650 650 L 668 680 L 530 680 Z" fill="{LILAS}"/>')
    c.append(caneca(950, 530))
    return W, H, "".join(c), "#5A3EE0"


def home_conversa():
    """Home, "Agende uma conversa": café virtual. Uma pessoa com fone e caneca,
    a outra na janela da chamada de vídeo, acenando. Fundo: roxo."""
    W, H = 560, 500
    c = []
    # janela da chamada
    c.append(f'<rect x="230" y="40" width="300" height="250" rx="24" fill="{BRANCO}"/>')
    c.append(f'<circle cx="256" cy="62" r="6" fill="{ROSA}"/><circle cx="276" cy="62" r="6" fill="{AMARELO}"/><circle cx="296" cy="62" r="6" fill="{ROXO}"/>')
    c.append(f'<clipPath id="tela-chamada"><rect x="246" y="82" width="268" height="192" rx="14"/></clipPath>')
    c.append(f'<rect x="246" y="82" width="268" height="192" rx="14" fill="{LILAS}"/>')
    c.append(f'<g clip-path="url(#tela-chamada)">'
             + pessoa(370, 180, 0.56, PELES["escura"], AMARELO, "cacheado", TEXTO, oculos=TEXTO, pose="fala")
             + '</g>')
    c.append(brilhos(232, 42, AMARELO, 3, -175, 70, 16, 30, 8))
    # quem está do lado de cá
    c.append(pessoa(150, 300, 0.8, PELES["morena"], ROSA, "comprido", TEXTO, fone=AMARELO, objeto="caneca"))
    c.append(balao(330, 316, 170, 80, BRANCO, "baixo-esquerda", ROSA))
    c.append(mesa(30, 446, 500, 200))
    c.append(f'<path d="M 300 476 L 420 476 L 436 500 L 310 500 Z" fill="{LILAS}"/>')  # a pessoa fica atrás da mesa; nunca deixar o tronco cortado no ar
    return W, H, "".join(c), ROXO


def ciencia_topo():
    """/ciencia/, primeiro bloco: "A ciência que você faz precisa chegar em quem importa."
    A pesquisadora fala; a ideia dela passa pelas plataformas (vídeo, podcast, post) e
    chega a pessoas de fora da academia. Fundo: bg1. A mesa encosta na seção branca seguinte."""
    W, H = 1200, 640
    ideia = (330, 190)
    c = []
    # fios primeiro: ideia -> vídeo -> podcast -> post, descendo até o público
    c.append(fio(ideia[0] + 60, ideia[1] - 30, 482, 110, curva=-0.12))
    c.append(fio(678, 110, 752, 150, curva=-0.12))
    c.append(fio(852, 170, 982, 220, curva=-0.12))
    c.append(icone_video(480, 40, 200, 130))
    c.append(icone_podcast(800, 160, 56))
    c.append(icone_post(980, 170, 120, 92))
    c.append(icone_ideia(*ideia, r=70))
    c.append(brilhos(330, 190, AMARELO, 3, -165, 50, 90, 26, 8))
    c.append(brilhos(1040, 216, AMARELO, 2, -60, 40, 92, 24, 8))
    # o público, de fora da academia
    c.append(pessoa(790, 430, 0.7, PELES["clara"], LARANJA, "branco", oculos=TEXTO))
    c.append(pessoa(1090, 440, 0.68, PELES["morena"], ROSA, "comprido", CABELO_CASTANHO, brinco=AMARELO))
    c.append(pessoa(940, 420, 0.72, PELES["media"], BRANCO, "curto", TEXTO, fone=ROSA, objeto="celular"))
    # a pesquisadora fala por último, para o braço ficar na frente
    c.append(pessoa(210, 420, 0.8, PELES["escura"], AMARELO, "coque", TEXTO, brinco=BRANCO, pose="fala"))
    c.append(mesa(30, 585, 1140, 200))
    c.append(notebook_costas(110, 482, 140, 92))
    c.append(livros(320, 509))
    c.append(caneca(590, 515, LARANJA))
    return W, H, "".join(c), "#5A3EE0"

def ciencia_perguntas():
    """/ciencia/, "Perguntas frequentes": a dúvida de quem pesquisa e a conversa que
    responde. O pesquisador pensa (mão no queixo, balão com interrogação); a pessoa da
    Seja fala e responde (balão com reticências). Fundo: roxo, então nada de roupa roxa."""
    W, H = 560, 470
    c = []
    # balões primeiro (acima das cabeças), com a ponta para quem fala
    c.append(balao(64, 36, 150, 96, BRANCO, "baixo-esquerda", None))
    c.append(interrogacao(139, 82, 50, ROSA))
    c.append(brilhos(236, 52, AMARELO, 3, -50, 60, 12, 24, 8))
    c.append(balao(285, 64, 170, 84, BRANCO, "baixo-direita", ROSA))
    # o pesquisador pensa; quem fala vem por último, com o braço na frente
    c.append(pessoa(130, 262, 0.6, PELES["clara"], LARANJA, "curto", CABELO_CASTANHO, oculos=TEXTO, pose="queixo"))
    c.append(pessoa(410, 262, 0.6, PELES["escura"], AMARELO, "cacheado", TEXTO, brinco=ROSA, pose="fala", espelhar=True))
    c.append(mesa(20, 420, 520, 200))
    c.append(caneca(204, 350, ROSA))
    return W, H, "".join(c), ROXO


CENAS = {
    "ilustra-home-topo-v1": home_topo,
    "ilustra-home-conversa-v1": home_conversa,
    "ilustra-ciencia-topo-v1": ciencia_topo,
    "ilustra-ciencia-perguntas-v1": ciencia_perguntas,
}


def gerar(nomes=None):
    os.makedirs(PREVIAS, exist_ok=True)
    conversor = shutil.which("rsvg-convert")
    for nome, fn in CENAS.items():
        if nomes and nome not in nomes:
            continue
        w, h, corpo, fundo = fn()
        destino = os.path.join(ASSETS, f"{nome}.svg")
        with open(destino, "w") as f:
            f.write(svg(w, h, corpo))
        print("svg:", os.path.relpath(destino, RAIZ))
        if conversor:
            png = os.path.join(PREVIAS, f"{nome}.png")
            subprocess.run([conversor, "-b", fundo, destino, "-o", png], check=True)
            print("prévia:", os.path.relpath(png, RAIZ))
        else:
            print("rsvg-convert não encontrado: abra o SVG num navegador para conferir.")


if __name__ == "__main__":
    gerar(sys.argv[1:] or None)
