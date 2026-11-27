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
    O pesquisador grava um vídeo explicando a pesquisa (celular no tripé) e o vídeo chega
    às telas de pessoas de fora da academia, que reagem. Fundo: bg1; a mesa encosta na
    seção branca seguinte."""
    W, H = 1200, 640
    cel = (560, 420)  # centro do celular no tripé
    c = []
    # fios do celular até as telas do público
    for alvo in [(720, 170), (958, 250), (760, 452)]:
        c.append(fio(cel[0] + 40, cel[1] - 20, alvo[0], alvo[1], curva=-0.12))
    # telas do público, cada uma com uma pessoa assistindo
    c.append(janela(700, 70, 230, 200, "tela-a",
                    conteudo=pessoa(815, 170, 0.62, PELES["clara"], LARANJA, "branco", oculos=TEXTO)))
    c.append(janela(956, 170, 210, 190, "tela-b", fundo=ROSA_CLARO,
                    conteudo=pessoa(1061, 268, 0.6, PELES["escura"], AMARELO, "curto", TEXTO, fone=ROSA)))
    c.append(janela(740, 362, 240, 200, "tela-c", fundo="#FFE7A8",
                    conteudo=pessoa(860, 462, 0.62, PELES["morena"], ROSA, "comprido", CABELO_CASTANHO, brinco=AMARELO)))
    c.append(coracao(930, 80, 44, ROSA))
    c.append(balao(1080, 64, 104, 64, BRANCO, "baixo-esquerda", ROSA))
    c.append(coracao(990, 400, 36, AMARELO))
    c.append(brilhos(560, 300, AMARELO, 3, -150, 60, 70, 24, 8))
    # o pesquisador explica para a câmera (fala por último entre as pessoas)
    c.append(pessoa(300, 400, 0.8, PELES["media"], AMARELO, "curto", TEXTO, barba=True, pose="fala"))
    c.append(mesa(40, 585, 640, 200))
    c.append(tripe_celular(cel[0], 355, 230))
    c.append(livros(80, 509))
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
    c.append(pessoa(130, 262, 0.6, PELES["clara"], LARANJA, "curto", CABELO_CASTANHO, oculos=TEXTO, barba=True, pose="queixo"))
    c.append(pessoa(410, 262, 0.6, PELES["escura"], AMARELO, "cacheado", TEXTO, brinco=ROSA, pose="fala", espelhar=True))
    c.append(mesa(20, 420, 520, 200))
    c.append(caneca(204, 350, ROSA))
    return W, H, "".join(c), ROXO


# ---------------------------------------------------------------- ícones das dores (/ciencia/)
# Um desenho por dor, num círculo colorido de 120x120. Fundo da página: branco.
def _dor(cor, corpo):
    return 120, 120, f'<circle cx="60" cy="60" r="60" fill="{cor}"/>' + corpo, BRANCO


def dor_alcance():
    """"Sabe que o que você estuda importa, mas não sabe como fazer isso chegar em quem
    não é da área": a ideia acesa, ligada por um fio a uma dúvida."""
    return _dor(ROXO, fio(46, 58, 86, 74, curva=0.3, espessura=4)
                + icone_ideia(42, 52, 26) + f'<circle cx="88" cy="80" r="18" fill="{AMARELO}"/>'
                + interrogacao(88, 78, 22, TEXTO))


def dor_tempo():
    """"Quer aparecer nas redes, mas não sabe por onde começar, e não tem tempo":
    o relógio e o celular."""
    return _dor(AMARELO, relogio(50, 56, 30, BRANCO, TEXTO)
                + f'<rect x="70" y="48" width="30" height="50" rx="7" fill="{TEXTO}"/>'
                + f'<rect x="74" y="54" width="22" height="34" rx="3" fill="{LILAS}"/>'
                + f'<path d="M 81 64 L 81 78 L 91 71 Z" fill="{ROSA}"/>')


def dor_tom():
    """"O que sai técnico demais não é lido, e o que sai simples demais parece raso":
    um texto cheio demais e outro quase vazio."""
    return _dor(AZUL, f'<g transform="rotate(-8 40 60)">' + documento(18, 30, 44, 58, BRANCO, TEXTO) + '</g>'
                + f'<g transform="rotate(8 82 62)"><rect x="60" y="34" width="44" height="58" rx="8" fill="{BRANCO}"/>'
                + f'<path d="M 68 52 L 84 52" stroke="{LILAS_MEDIO}" stroke-width="4" stroke-linecap="round"/></g>')


def dor_rotina():
    """"Como conciliar isso com a rotina de pesquisa, aula e orientação": livros,
    notebook e caneca disputando a mesma mesa."""
    return _dor(LARANJA, f'<g transform="translate(16 46) scale(0.3)">' + livros(0, 0) + '</g>'
                + f'<rect x="62" y="42" width="40" height="30" rx="5" fill="{TEXTO}"/>'
                + f'<circle cx="82" cy="56" r="4" fill="{AMARELO}"/>'
                + f'<rect x="56" y="71" width="52" height="6" rx="3" fill="{TEXTO}"/>'
                + f'<rect x="36" y="74" width="16" height="18" rx="4" fill="{AMARELO}"/>'
                + f'<path d="M 52 78 Q 59 78 58 84 Q 57 89 52 88" fill="none" stroke="{AMARELO}" stroke-width="3"/>'
                + f'<rect x="14" y="92" width="92" height="7" rx="3.5" fill="{BRANCO}"/>')

def dor_impacto():
    """"Precisa mostrar o impacto do seu trabalho pra editais, avaliações e CAPES":
    o relatório com o selo de aprovado."""
    return _dor(ROSA, documento(32, 22, 54, 72, BRANCO, LILAS_MEDIO, selo=AMARELO)
                + brilhos(88, 30, AMARELO, 3, -60, 70, 6, 10, 4))


CENAS = {
    "ilustra-home-topo-v1": home_topo,
    "ilustra-home-conversa-v1": home_conversa,
    "ilustra-ciencia-topo-v1": ciencia_topo,
    "ilustra-ciencia-perguntas-v1": ciencia_perguntas,
    "ilustra-ciencia-dor-alcance-v1": dor_alcance,
    "ilustra-ciencia-dor-tempo-v1": dor_tempo,
    "ilustra-ciencia-dor-tom-v1": dor_tom,
    "ilustra-ciencia-dor-rotina-v1": dor_rotina,
    "ilustra-ciencia-dor-impacto-v1": dor_impacto,
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
