#!/usr/bin/env python3
"""Coiote Místico 1.0.0: selo e abertura verificáveis de tiragens Rider-Waite-Smith."""
import hashlib
import json
import os
import re
import secrets
import sys
from pathlib import Path

VERSAO = "TARO-RWS-3Q-V1"
PASTA = Path(os.environ.get("COIOTE_DIR", str(Path.home() / ".coiote-mistico")))

CATALOGO = [
    (0, "O Louco", "The Fool", "0", "Viajante à beira do precipício, rosa branca e cão."),
    (1, "O Mago", "The Magician", "I", "Bastão erguido, símbolo do infinito e quatro emblemas sobre a mesa."),
    (2, "A Sacerdotisa", "The High Priestess", "II", "Pilares B e J, véu com romãs e rolo parcialmente coberto."),
    (3, "A Imperatriz", "The Empress", "III", "Trigo, coroa de estrelas e escudo com o símbolo de Vênus."),
    (4, "O Imperador", "The Emperor", "IV", "Trono com cabeças de carneiro e montanhas."),
    (5, "O Hierofante", "The Hierophant", "V", "Tiara, dois acólitos e chaves cruzadas."),
    (6, "Os Enamorados", "The Lovers", "VI", "Duas figuras sob um anjo e uma serpente em uma das árvores."),
    (7, "O Carro", "The Chariot", "VII", "Condutor sob dossel estrelado, com uma esfinge clara e outra escura."),
    (8, "A Força", "Strength", "VIII", "Mulher junto à boca de um leão, com o símbolo do infinito acima da cabeça."),
    (9, "O Eremita", "The Hermit", "IX", "Figura encapuzada com cajado e estrela dentro da lanterna."),
    (10, "A Roda da Fortuna", "Wheel of Fortune", "X", "Roda inscrita, esfinge acima e quatro figuras aladas nos cantos."),
    (11, "A Justiça", "Justice", "XI", "Figura entre pilares, com balança e espada erguida."),
    (12, "O Enforcado", "The Hanged Man", "XII", "Figura suspensa por um pé, com a outra perna dobrada e uma auréola."),
    (13, "A Morte", "Death", "XIII", "Esqueleto em armadura, cavalo branco e estandarte escuro com rosa branca."),
    (14, "A Temperança", "Temperance", "XIV", "Anjo verte líquido entre duas taças, com um pé na água e outro em terra."),
    (15, "O Diabo", "The Devil", "XV", "Figura alada sobre pedestal e duas figuras humanas acorrentadas."),
    (16, "A Torre", "The Tower", "XVI", "Raio, coroa deslocada e figuras em queda."),
    (17, "A Estrela", "The Star", "XVII", "Uma estrela grande, sete menores e água vertida de dois jarros."),
    (18, "A Lua", "The Moon", "XVIII", "Cão, lobo e crustáceo que emerge da água, com duas torres ao fundo."),
    (19, "O Sol", "The Sun", "XIX", "Criança em cavalo branco, estandarte vermelho e girassóis."),
    (20, "O Julgamento", "Judgement", "XX", "Anjo com trombeta e figuras que se erguem de caixões."),
    (21, "O Mundo", "The World", "XXI", "Figura dançante dentro de uma grinalda, com quatro figuras nos cantos."),
    (22, "Ás de Paus", "Ace of Wands", None, "Mão saindo da nuvem segura um bastão com brotos."),
    (23, "Dois de Paus", "Two of Wands", None, "Figura com globo entre dois bastões, no alto de uma muralha."),
    (24, "Três de Paus", "Three of Wands", None, "Figura de costas entre três bastões, olhando embarcações ao longe."),
    (25, "Quatro de Paus", "Four of Wands", None, "Guirlanda suspensa nos quatro bastões e figuras em celebração."),
    (26, "Cinco de Paus", "Five of Wands", None, "Cinco jovens erguem bastões que se cruzam."),
    (27, "Seis de Paus", "Six of Wands", None, "Figura a cavalo com coroa de louros e outra coroa no bastão."),
    (28, "Sete de Paus", "Seven of Wands", None, "Figura em terreno elevado empunha um bastão diante de seis que sobem."),
    (29, "Oito de Paus", "Eight of Wands", None, "Oito bastões cruzam o céu em diagonal."),
    (30, "Nove de Paus", "Nine of Wands", None, "Figura com a cabeça enfaixada, um bastão na mão e oito atrás."),
    (31, "Dez de Paus", "Ten of Wands", None, "Figura curvada carrega dez bastões em direção às construções."),
    (32, "Pajem de Paus", "Page of Wands", None, "Jovem contempla um bastão erguido em paisagem árida."),
    (33, "Cavaleiro de Paus", "Knight of Wands", None, "Cavaleiro com bastão sobre cavalo que ergue as patas dianteiras."),
    (34, "Rainha de Paus", "Queen of Wands", None, "Girassol na mão e gato preto aos pés."),
    (35, "Rei de Paus", "King of Wands", None, "Bastão, motivos de salamandra e uma salamandra junto ao trono."),
    (36, "Ás de Copas", "Ace of Cups", None, "Mão sustenta um cálice transbordante sob uma pomba."),
    (37, "Dois de Copas", "Two of Cups", None, "Duas taças erguidas sob um caduceu e uma cabeça de leão alada."),
    (38, "Três de Copas", "Three of Cups", None, "Três figuras erguem taças sobre um chão com frutos da colheita."),
    (39, "Quatro de Copas", "Four of Cups", None, "Figura junto à árvore, três taças no chão e uma quarta oferecida pela nuvem."),
    (40, "Cinco de Copas", "Five of Cups", None, "Figura de capa escura, três taças tombadas e duas de pé."),
    (41, "Seis de Copas", "Six of Cups", None, "Figura jovem oferece a outra uma taça com flores brancas."),
    (42, "Sete de Copas", "Seven of Cups", None, "Silhueta diante de sete taças sobre nuvens, cada qual com uma visão."),
    (43, "Oito de Copas", "Eight of Cups", None, "Figura se afasta das oito taças sob a lua."),
    (44, "Nove de Copas", "Nine of Cups", None, "Figura sentada de braços cruzados, com nove taças atrás."),
    (45, "Dez de Copas", "Ten of Cups", None, "Dez taças em um arco-íris sobre uma família."),
    (46, "Pajem de Copas", "Page of Cups", None, "Jovem olha para o peixe que emerge da taça."),
    (47, "Cavaleiro de Copas", "Knight of Cups", None, "Cavaleiro estende uma taça sobre um cavalo claro."),
    (48, "Rainha de Copas", "Queen of Cups", None, "Rainha à beira da água contempla um cálice fechado e ornamentado."),
    (49, "Rei de Copas", "King of Cups", None, "Rei com taça e cetro em um trono cercado pelo mar."),
    (50, "Ás de Espadas", "Ace of Swords", None, "Mão na nuvem ergue uma espada cuja ponta passa por uma coroa."),
    (51, "Dois de Espadas", "Two of Swords", None, "Figura vendada, espadas cruzadas e lua crescente sobre o mar."),
    (52, "Três de Espadas", "Three of Swords", None, "Três espadas atravessam um coração sob a chuva."),
    (53, "Quatro de Espadas", "Four of Swords", None, "Efígie deitada, três espadas na parede e uma junto ao túmulo."),
    (54, "Cinco de Espadas", "Five of Swords", None, "Figura recolhe espadas enquanto outras duas se afastam."),
    (55, "Seis de Espadas", "Six of Swords", None, "Barco com passageiros e seis espadas fincadas."),
    (56, "Sete de Espadas", "Seven of Swords", None, "Figura leva cinco espadas e deixa duas junto ao acampamento."),
    (57, "Oito de Espadas", "Eight of Swords", None, "Figura vendada e amarrada, cercada por oito espadas."),
    (58, "Nove de Espadas", "Nine of Swords", None, "Figura sentada na cama com o rosto entre as mãos, sob nove espadas."),
    (59, "Dez de Espadas", "Ten of Swords", None, "Figura caída com dez espadas nas costas e uma faixa clara no horizonte."),
    (60, "Pajem de Espadas", "Page of Swords", None, "Jovem sustenta a espada com as duas mãos em colina ventosa."),
    (61, "Cavaleiro de Espadas", "Knight of Swords", None, "Cavaleiro com espada erguida sobre cavalo em disparada."),
    (62, "Rainha de Espadas", "Queen of Swords", None, "Rainha com espada vertical e a mão livre estendida."),
    (63, "Rei de Espadas", "King of Swords", None, "Rei sentado de frente, com espada erguida."),
    (64, "Ás de Ouros", "Ace of Pentacles", None, "Mão apresenta um pentáculo sobre um jardim com arco vegetal."),
    (65, "Dois de Ouros", "Two of Pentacles", None, "Dois pentáculos ligados por uma alça em forma de infinito, com barcos ao fundo."),
    (66, "Três de Ouros", "Three of Pentacles", None, "Artesão e duas figuras sob um arco de pedra com três pentáculos."),
    (67, "Quatro de Ouros", "Four of Pentacles", None, "Um pentáculo junto ao peito, um sobre a coroa e dois sob os pés."),
    (68, "Cinco de Ouros", "Five of Pentacles", None, "Duas figuras passam pela neve diante de um vitral iluminado."),
    (69, "Seis de Ouros", "Six of Pentacles", None, "Figura com balança distribui moedas a uma pessoa ajoelhada."),
    (70, "Sete de Ouros", "Seven of Pentacles", None, "Pessoa apoiada em uma ferramenta contempla a planta com pentáculos."),
    (71, "Oito de Ouros", "Eight of Pentacles", None, "Artesão grava um pentáculo, com outros expostos ao lado."),
    (72, "Nove de Ouros", "Nine of Pentacles", None, "Figura em um vinhedo, com falcão encapuzado sobre a luva."),
    (73, "Dez de Ouros", "Ten of Pentacles", None, "Pessoas de diferentes gerações e dois cães sob um arco."),
    (74, "Pajem de Ouros", "Page of Pentacles", None, "Jovem contempla um pentáculo erguido entre as mãos."),
    (75, "Cavaleiro de Ouros", "Knight of Pentacles", None, "Cavaleiro sustenta um pentáculo sobre um cavalo escuro parado."),
    (76, "Rainha de Ouros", "Queen of Pentacles", None, "Rainha contempla um pentáculo no colo, com um coelho no primeiro plano."),
    (77, "Rei de Ouros", "King of Pentacles", None, "Rei com pentáculo e cetro, em trono com cabeças de touro, cercado por videiras."),
]


def saida(codigo, **dados):
    dados["ok"] = codigo == 0
    print(json.dumps(dados, ensure_ascii=False, indent=2))
    sys.exit(codigo)


def serializar(registro):
    return json.dumps(registro, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def sha256(dados):
    return hashlib.sha256(dados).hexdigest()


def selar():
    try:
        perguntas = json.loads(sys.stdin.read())
    except json.JSONDecodeError as erro:
        saida(2, erro="entrada_invalida", mensagem=f"JSON inválido: {erro}")
    if not (isinstance(perguntas, list) and len(perguntas) == 3
            and all(isinstance(p, str) and p.strip() for p in perguntas)):
        saida(2, erro="entrada_invalida", mensagem="Envie um array JSON com exatamente três perguntas não vazias.")
    baralho = list(range(78))
    secrets.SystemRandom().shuffle(baralho)
    if sorted(baralho) != list(range(78)):
        saida(3, erro="baralho_invalido", mensagem="Falha ao embaralhar.")
    dados = serializar([VERSAO, perguntas, secrets.token_hex(32), baralho])
    selo = sha256(dados)
    PASTA.mkdir(parents=True, exist_ok=True)
    caminho = PASTA / f"{selo}.json"
    caminho.write_bytes(dados)
    if sha256(caminho.read_bytes()) != selo:
        saida(3, erro="gravacao_falhou", mensagem="O registro gravado não reproduz o selo.")
    saida(0, selo=selo, perguntas=perguntas)


def carregar(selo):
    if not re.fullmatch(r"[0-9a-f]{64}", selo):
        saida(2, erro="selo_invalido", mensagem="O selo deve ter 64 caracteres hexadecimais minúsculos.")
    caminho = PASTA / f"{selo}.json"
    if not caminho.is_file():
        saida(3, erro="registro_ausente", mensagem="Não há registro para este selo neste ambiente.")
    dados = caminho.read_bytes()
    if sha256(dados) != selo:
        saida(3, erro="hash_divergente", mensagem="O registro não reproduz o selo publicado.")
    try:
        registro = json.loads(dados.decode("utf-8"))
        versao, perguntas, nonce, baralho = registro
    except (ValueError, TypeError, UnicodeDecodeError):
        saida(3, erro="registro_corrompido", mensagem="O registro não tem a estrutura esperada.")
    valido = (
        versao == VERSAO
        and isinstance(perguntas, list) and len(perguntas) == 3
        and all(isinstance(p, str) for p in perguntas)
        and isinstance(nonce, str) and re.fullmatch(r"[0-9a-f]{64}", nonce)
        and isinstance(baralho, list)
        and all(type(c) is int for c in baralho)
        and sorted(baralho) == list(range(78))
        and serializar(registro) == dados
    )
    if not valido:
        saida(3, erro="registro_invalido", mensagem="O registro falhou na validação.")
    return dados, perguntas, baralho


def ler_posicoes(texto):
    partes = [p for p in re.split(r"[\s,;]+", texto.strip()) if p]
    if len(partes) != 3 or not all(re.fullmatch(r"\d+", p) for p in partes):
        saida(2, erro="escolha_invalida", mensagem="Envie exatamente três números inteiros.")
    posicoes = [int(p) for p in partes]
    if any(not 1 <= p <= 78 for p in posicoes):
        saida(2, erro="escolha_invalida", mensagem="Os números devem estar entre 1 e 78.")
    if len(set(posicoes)) != 3:
        saida(2, erro="escolha_invalida", mensagem="Os três números devem ser diferentes.")
    return posicoes


def abrir(selo, texto):
    posicoes = ler_posicoes(texto)
    dados, perguntas, baralho = carregar(selo)
    marca = PASTA / f"{selo}.abertura.json"
    if marca.is_file():
        anteriores = json.loads(marca.read_text(encoding="utf-8"))
        if anteriores != posicoes:
            saida(4, erro="rodada_ja_aberta", posicoes_fixadas=anteriores,
                  mensagem="Esta rodada já foi aberta com outras posições. Uma nova escolha exige novo selo.")
    else:
        marca.write_text(json.dumps(posicoes), encoding="utf-8")
    cartas = []
    for ordem, (pergunta, posicao) in enumerate(zip(perguntas, posicoes), start=1):
        cid, pt, en, numeral, elementos = CATALOGO[baralho[posicao - 1]]
        cartas.append({"ordem": ordem, "pergunta": pergunta, "posicao": posicao, "id": cid,
                       "nome": pt, "nome_en": en, "numeral_face": numeral, "elementos": elementos})
    saida(0, selo=selo, verificado=True, cartas=cartas, registro_json=dados.decode("utf-8"))


def conferir():
    linha = sys.stdin.read()
    if linha.endswith("\n"):
        linha = linha[:-1]
    saida(0, sha256=sha256(linha.encode("utf-8")))


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "selar" and len(sys.argv) == 2:
        selar()
    elif len(sys.argv) == 4 and sys.argv[1] == "abrir":
        abrir(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 2 and sys.argv[1] == "conferir":
        conferir()
    else:
        saida(2, erro="uso", mensagem='Uso: selar < perguntas.json | abrir SELO "n1 n2 n3" | conferir < linha.txt')


if __name__ == "__main__":
    main()
