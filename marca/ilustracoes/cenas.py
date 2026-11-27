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
    c.append(pessoa(905, 450, 0.82, PELES["morena"], BRANCO, "cacheado", TEXTO, fone=ROSA, barba=True, pose="queixo", espelhar=True))
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
# Um desenho por dor, 120x120, direto no fundo branco da página (sem círculo atrás):
# nada de peça branca; folhas e telas em lilás, contornos em texto.
def _dor(corpo):
    return 120, 120, corpo, BRANCO


def dor_alcance():
    """"Sabe que o que você estuda importa, mas não sabe como fazer isso chegar em quem
    não é da área": a ideia acesa, ligada por um fio a uma dúvida."""
    return _dor(fio(48, 60, 90, 84, curva=0.3, cor=ROXO, espessura=5)
                + f'<circle cx="44" cy="50" r="34" fill="{LILAS}"/>' + icone_ideia(44, 50, 34).split('/>', 1)[1]
                + f'<circle cx="92" cy="88" r="22" fill="{AMARELO}"/>' + interrogacao(92, 86, 26, TEXTO))


def dor_tempo():
    """"Quer aparecer nas redes, mas não sabe por onde começar, e não tem tempo":
    o relógio e o celular."""
    return _dor(relogio(48, 56, 38, AMARELO, TEXTO)
                + f'<rect x="72" y="44" width="36" height="62" rx="8" fill="{TEXTO}"/>'
                + f'<rect x="77" y="51" width="26" height="42" rx="4" fill="{LILAS}"/>'
                + f'<path d="M 85 63 L 85 81 L 98 72 Z" fill="{ROSA}"/>')


def dor_tom():
    """"O que sai técnico demais não é lido, e o que sai simples demais parece raso":
    um texto cheio demais e outro quase vazio."""
    return _dor(f'<g transform="rotate(-8 38 60)">' + documento(12, 22, 52, 72, LILAS, TEXTO) + '</g>'
                + f'<g transform="rotate(8 84 62)"><rect x="60" y="28" width="52" height="72" rx="9" fill="{AZUL}"/>'
                + f'<path d="M 70 50 L 88 50" stroke="{BRANCO}" stroke-width="5" stroke-linecap="round"/></g>')


def dor_rotina():
    """"Como conciliar isso com a rotina de pesquisa, aula e orientação": livros com a
    caneca em cima e o notebook, tudo na mesma estante."""
    return _dor(f'<g transform="translate(4 70) scale(0.36)">' + livros(0, 0) + '</g>'
                + f'<rect x="20" y="48" width="20" height="22" rx="5" fill="{LARANJA}"/>'
                + f'<path d="M 40 53 Q 49 53 48 60 Q 47 66 40 65" fill="none" stroke="{LARANJA}" stroke-width="4"/>'
                + f'<rect x="64" y="52" width="48" height="36" rx="6" fill="{TEXTO}"/>'
                + f'<circle cx="88" cy="69" r="5" fill="{AMARELO}"/>'
                + f'<rect x="58" y="87" width="60" height="9" rx="4" fill="{TEXTO}"/>'
                + f'<rect x="2" y="96" width="116" height="8" rx="4" fill="{LILAS_MEDIO}"/>')


def dor_impacto():
    """"Precisa mostrar o impacto do seu trabalho pra editais, avaliações e CAPES":
    o relatório com o selo de aprovado."""
    return _dor(documento(24, 12, 66, 88, LILAS_MEDIO, BRANCO, selo=ROSA))


# ---------------------------------------------------------------- ícones dos serviços (/ciencia/, fundo branco)
def servico_projeto():
    """Projeto: "escopo e prazo definidos" → calendário com o prazo cumprido."""
    return 120, 120, calendario(16, 22, 88, 84, ROXO, LILAS, "check"), BRANCO


def servico_parceria():
    """Parceria contínua: "caminhada de longo prazo" → duas pessoas lado a lado, um coração entre elas."""
    return 120, 120, (pessoa(40, 46, 0.19, PELES["escura"], ROSA, "coque", TEXTO)
                      + pessoa(82, 48, 0.19, PELES["clara"], AMARELO, "curto", CABELO_CASTANHO, barba=True)
                      + coracao(61, 20, 18, ROSA)
                      + f'<rect x="6" y="100" width="108" height="10" rx="5" fill="{LILAS_MEDIO}"/>'), BRANCO


def servico_formacao():
    """Formação: "aprender a comunicar a própria ciência" → quadro de aula."""
    return 120, 120, quadro(8, 24, 104, 66, LILAS, AMARELO), BRANCO


# ---------------------------------------------------------------- ícones da linha do tempo da CAPES (/ciencia/, fundo cinza claro)
def capes_qualis():
    """Até 2024, "lista de revistas com nota Qualis" → pilha de revistas com uma estrela."""
    return 120, 120, (f'<g transform="translate(15 52) scale(0.6)">' + livros(0, 0) + '</g>'
                      + estrela(60, 30, 20, AMARELO)), CLARO


def capes_artigo():
    """2025, "a classificação passa a ser do artigo" → o artigo com a estrela."""
    return 120, 120, (documento(28, 14, 64, 90, BRANCO, LILAS_MEDIO)
                      + f'<circle cx="88" cy="86" r="20" fill="{LARANJA}"/>' + estrela(88, 87, 12, BRANCO)), CLARO


def capes_coleta():
    """2025 a 2028, "coleta de dados anual" → calendário com os anos marcados."""
    return 120, 120, calendario(14, 22, 92, 84, LARANJA, BRANCO, "dias"), CLARO


def capes_quadrienal():
    """2029, "Avaliação Quadrienal, notas de 1 a 7" → a medalha da avaliação."""
    return 120, 120, medalha(60, 76, 30, AMARELO, ROSA, ROXO), CLARO


CENAS = {
    "ilustra-home-topo-v2": home_topo,
    "ilustra-home-conversa-v1": home_conversa,
    "ilustra-ciencia-topo-v1": ciencia_topo,
    "ilustra-ciencia-perguntas-v1": ciencia_perguntas,
    "ilustra-ciencia-dor-alcance-v1": dor_alcance,
    "ilustra-ciencia-dor-tempo-v1": dor_tempo,
    "ilustra-ciencia-dor-tom-v1": dor_tom,
    "ilustra-ciencia-dor-rotina-v1": dor_rotina,
    "ilustra-ciencia-dor-impacto-v1": dor_impacto,
    "ilustra-ciencia-servico-projeto-v1": servico_projeto,
    "ilustra-ciencia-servico-parceria-v1": servico_parceria,
    "ilustra-ciencia-servico-formacao-v1": servico_formacao,
    "ilustra-ciencia-capes-qualis-v1": capes_qualis,
    "ilustra-ciencia-capes-artigo-v1": capes_artigo,
    "ilustra-ciencia-capes-coleta-v1": capes_coleta,
    "ilustra-ciencia-capes-quadrienal-v1": capes_quadrienal,
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
