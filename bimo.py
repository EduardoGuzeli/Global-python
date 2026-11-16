"""
BIMO — Assistente de bem-estar | FIAP Global Solution 2026.2
Tema: CitizenTech

Aplicação de terminal em um único arquivo Python.
Requer Python 3.10+ e utiliza somente a biblioteca padrão.
Os dados são persistidos automaticamente em dados.json, na mesma pasta.
"""

import json
import os
import random
import shutil
import unicodedata
from datetime import date, timedelta


# ============================================================
# CONFIGURAÇÕES E DADOS FIXOS
# ============================================================

ARQUIVO_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados.json")

EMOCOES = (
    "feliz", "calmo", "grato", "ansioso",
    "triste", "irritado", "cansado", "sozinho"
)

NIVEIS = (
    ("Semente", 0),
    ("Broto", 50),
    ("Muda", 120),
    ("Árvore", 250),
    ("Floresta", 500),
)

CONQUISTAS = {
    "Primeiro passo": "Registrar o primeiro check-in",
    "Constância": "Manter 3 dias seguidos de check-in",
    "Semana de cuidado": "Manter 7 dias seguidos de check-in",
    "Escritor": "Criar 5 entradas no diário",
    "Bate-papo": "Conversar com o Bimo pela primeira vez",
}

EXPRESSOES_RISCO = (
    "me machucar",
    "me matar",
    "suicidio",
    "não quero viver",
    "nao quero viver",
    "desistir de tudo",
    "acabar com tudo",
    "sumir",
)

FRASES = {
    "acolhedor": {
        "baixo": [
            "Estou aqui para te ouvir. Um passo de cada vez.",
            "Você merece cuidado, inclusive nos dias difíceis.",
            "Não precisa resolver tudo agora. Vamos com calma."
        ],
        "neutro": [
            "Tudo bem não ter todas as respostas hoje.",
            "Que tal escolher uma pequena coisa boa para fazer por você?",
            "Um dia de cada vez também é um caminho."
        ],
        "bom": [
            "Fico feliz que esteja se sentindo assim!",
            "Guarde esse momento positivo com carinho.",
            "Que bom encontrar algo leve no seu dia!"
        ],
    },
    "divertido": {
        "baixo": [
            "Hoje pode estar puxado. Vamos no modo passo pequeno?",
            "Sem cobrança: até uma pausa já conta.",
            "Um passo de cada vez. Não precisa zerar o jogo hoje."
        ],
        "neutro": [
            "Dia meio termo também faz parte do jogo.",
            "Missão de hoje: fazer algo gentil por você.",
            "Nem todo dia precisa ser épico!"
        ],
        "bom": [
            "Aí sim! Energia boa merece ser celebrada.",
            "Ponto para você por perceber esse momento!",
            "Que notícia boa! Aproveite essa fase."
        ],
    },
    "calmo": {
        "baixo": [
            "Respire no seu ritmo. Você não precisa resolver tudo agora.",
            "Vamos atravessar este momento com tranquilidade.",
            "Permita-se uma pausa. Você também merece cuidado."
        ],
        "neutro": [
            "Observe como está se sentindo, sem se julgar.",
            "Um momento de pausa pode ajudar a organizar as ideias.",
            "Não há problema em seguir no seu próprio ritmo."
        ],
        "bom": [
            "Acolha essa tranquilidade e aproveite o presente.",
            "Que bom que hoje há algo leve para reconhecer.",
            "Aproveite esse momento com atenção e carinho."
        ],
    },
}


# ============================================================
# INTERFACE E VALIDAÇÃO
# ============================================================

def limpar_tela():
    """Limpa o terminal conforme o sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


def linha(caractere="─", tamanho=60):
    """Retorna uma linha decorativa."""
    return caractere * tamanho


def cabecalho(titulo):
    """Exibe um cabeçalho padronizado."""
    print("\n" + linha())
    print(titulo.center(60))
    print(linha())


def pausar():
    """Aguarda o usuário pressionar Enter."""
    input("\nPressione Enter para continuar...")


def pedir_inteiro(mensagem, minimo=None, maximo=None):
    """Solicita um número inteiro dentro dos limites informados."""
    while True:
        try:
            valor = int(input(mensagem).strip())
            if minimo is not None and valor < minimo:
                print(f"Digite um número a partir de {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Digite um número até {maximo}.")
                continue
            return valor
        except ValueError:
            print("✘ Entrada inválida. Digite um número inteiro.")
        except (KeyboardInterrupt, EOFError):
            raise


def pedir_texto(mensagem, minimo=0, maximo=None, permitir_vazio=False):
    """Solicita texto respeitando tamanho mínimo e máximo."""
    while True:
        texto = input(mensagem).strip()

        if not texto and permitir_vazio:
            return ""

        if len(texto) < minimo:
            print(f"Digite pelo menos {minimo} caracteres.")
            continue

        if maximo is not None and len(texto) > maximo:
            print(f"Limite de {maximo} caracteres. Você digitou {len(texto)}.")
            continue

        return texto


def confirmar(mensagem):
    """Solicita confirmação com s/n."""
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Responda com s ou n.")


# ============================================================
# SEGURANÇA E ORIENTAÇÕES
# ============================================================

def normalizar_texto(texto):
    """Converte para minúsculas e remove acentos."""
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


def detectar_risco(texto):
    """Verifica se o texto contém alguma expressão da lista de risco."""
    texto_normalizado = normalizar_texto(texto)
    return any(
        normalizar_texto(expressao) in texto_normalizado
        for expressao in EXPRESSOES_RISCO
    )


def mostrar_apoio():
    """Exibe mensagem acolhedora e contatos brasileiros de apoio."""
    print("\n" + "!" * 60)
    print("Bimo: Obrigado por compartilhar algo tão difícil.")
    print("Sinto muito que você esteja passando por isso.")
    print("Você não precisa lidar com esse momento sem apoio.")
    print("Se puder, procure agora alguém de confiança e conte como está.")
    print("\nCVV: ligue 188 (24 horas, gratuito) ou acesse cvv.org.br.")
    print("Em uma emergência, ligue para o SAMU: 192.")
    print("!" * 60)


def mostrar_aviso_fixo(curto=False):
    """Informa que o Bimo não substitui acompanhamento profissional."""
    if curto:
        print("\nℹ O Bimo é um apoio e NÃO substitui acompanhamento profissional.")
    else:
        print("IMPORTANTE: o Bimo é um apoio e NÃO substitui")
        print("o acompanhamento de um profissional de saúde mental.")


# ============================================================
# PERSISTÊNCIA JSON
# ============================================================

def carregar_dados():
    """Carrega o JSON ou cria uma estrutura vazia se ele não existir."""
    if not os.path.exists(ARQUIVO_DADOS):
        dados_iniciais = {"usuarios": {}}
        salvar_dados(dados_iniciais)
        return dados_iniciais

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, dict) or not isinstance(dados.get("usuarios"), dict):
            raise ValueError("A estrutura do arquivo JSON é inválida.")

        return dados

    except (json.JSONDecodeError, OSError, ValueError) as erro:
        print(f"✘ Erro ao carregar os dados: {erro}")

        try:
            backup = ARQUIVO_DADOS.replace(".json", "_corrompido.json")
            shutil.copy2(ARQUIVO_DADOS, backup)
            print(f"ℹ Cópia do arquivo corrompido salva em: {backup}")
        except OSError:
            print("ℹ Não foi possível criar uma cópia de segurança.")

        print("ℹ O programa continuará com um banco de dados vazio.")
        return {"usuarios": {}}


def salvar_dados(dados):
    """Salva os perfis em JSON com codificação UTF-8."""
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        return True
    except OSError as erro:
        print(f"✘ Não foi possível salvar os dados: {erro}")
        return False


# ============================================================
# CADASTRO E LOGIN
# ============================================================

def validar_nome(nome):
    """Valida nome com 2 a 20 caracteres, somente letras e espaços."""
    nome = nome.strip()
    return (
        2 <= len(nome) <= 20
        and all(caractere.isalpha() or caractere.isspace() for caractere in nome)
        and any(caractere.isalpha() for caractere in nome)
    )


def criar_perfil(nome):
    """Cria um perfil com os valores iniciais do projeto."""
    return {
        "nome": nome,
        "personalidade": "acolhedor",
        "pontos": 0,
        "streak": 0,
        "ultimo_checkin": None,
        "ultima_conversa": None,
        "conversou": False,
        "conquistas": [],
        "checkins": [],
        "diario": [],
    }


def acessar_usuario(dados):
    """Realiza login por nome ou cadastra um novo perfil."""
    while True:
        cabecalho("CADASTRO / LOGIN")
        nome = pedir_texto("Digite seu nome (2 a 20 letras): ", 2, 20)

        if not validar_nome(nome):
            print("✘ Use apenas letras e espaços, com 2 a 20 caracteres.")
            pausar()
            continue

        chave = nome.lower().strip()

        if chave in dados["usuarios"]:
            usuario = dados["usuarios"][chave]
            print(f"✔ Bem-vindo de volta, {usuario['nome']}!")
        else:
            usuario = criar_perfil(nome)
            dados["usuarios"][chave] = usuario
            print(f"✔ Perfil criado. Seja bem-vindo(a), {nome}!")

        salvar_dados(dados)
        pausar()
        return usuario


# ============================================================
# NÍVEIS, PONTOS, STREAK E CONQUISTAS
# ============================================================

def obter_nivel(pontos):
    """Retorna o nível atual e quantos pontos faltam para o próximo."""
    nivel_atual = NIVEIS[0][0]
    proximo_minimo = None

    for indice, (nome, minimo) in enumerate(NIVEIS):
        if pontos >= minimo:
            nivel_atual = nome
            if indice + 1 < len(NIVEIS):
                proximo_minimo = NIVEIS[indice + 1][1]

    faltam = max(0, proximo_minimo - pontos) if proximo_minimo is not None else 0
    return nivel_atual, faltam


def adicionar_pontos(usuario, quantidade):
    """Adiciona pontos ao perfil do usuário."""
    usuario["pontos"] = usuario.get("pontos", 0) + quantidade


def atualizar_streak(usuario, hoje=None):
    """Atualiza a sequência de dias consecutivos com check-in."""
    hoje = hoje or date.today()
    ultimo = usuario.get("ultimo_checkin")

    if not ultimo:
        usuario["streak"] = 1
    else:
        data_ultima = date.fromisoformat(ultimo)
        diferenca = (hoje - data_ultima).days

        if diferenca == 1:
            usuario["streak"] = usuario.get("streak", 0) + 1
        elif diferenca > 1:
            usuario["streak"] = 1

    usuario["ultimo_checkin"] = hoje.isoformat()
    return usuario["streak"]


def verificar_conquistas(usuario):
    """Desbloqueia conquistas elegíveis sem repetir registros."""
    checkins = usuario.get("checkins", [])
    diario = usuario.get("diario", [])
    conquistas = usuario.setdefault("conquistas", [])
    elegiveis = []

    if len(checkins) >= 1:
        elegiveis.append("Primeiro passo")
    if usuario.get("streak", 0) >= 3:
        elegiveis.append("Constância")
    if usuario.get("streak", 0) >= 7:
        elegiveis.append("Semana de cuidado")
    if len(diario) >= 5:
        elegiveis.append("Escritor")
    if usuario.get("conversou", False):
        elegiveis.append("Bate-papo")

    novas = [nome for nome in elegiveis if nome not in conquistas]

    for nome in novas:
        conquistas.append(nome)
        print(f"🏆 Conquista desbloqueada: {nome}!")


def estatisticas(usuario):
    """Retorna uma tupla com média de humor e emoção mais frequente."""
    checkins = usuario.get("checkins", [])

    if not checkins:
        return 0.0, "Ainda sem registros"

    media = sum(item["nota"] for item in checkins) / len(checkins)
    frequencias = {}

    for item in checkins:
        emocao = item["emocao"]
        frequencias[emocao] = frequencias.get(emocao, 0) + 1

    emocao_frequente = max(frequencias, key=frequencias.get)
    return media, emocao_frequente


def mostrar_recompensas(usuario):
    """Mostra pontos, nível, progresso, streak, conquistas e estatísticas."""
    cabecalho("SUAS RECOMPENSAS")

    pontos = usuario.get("pontos", 0)
    nivel, faltam = obter_nivel(pontos)
    proximo_minimo = next(
        (minimo for nome, minimo in NIVEIS if minimo > pontos),
        None
    )

    if proximo_minimo is None:
        barra = "[##########]"
        progresso = "Você alcançou o nível máximo!"
    else:
        anterior = max(minimo for nome, minimo in NIVEIS if minimo <= pontos)
        percentual = (pontos - anterior) / (proximo_minimo - anterior)
        preenchido = min(10, int(percentual * 10))
        barra = "[" + "#" * preenchido + "-" * (10 - preenchido) + "]"
        progresso = f"Faltam {faltam} pontos para o próximo nível."

    media, emocao = estatisticas(usuario)

    print(f"Perfil: {usuario['nome']}")
    print(f"Nível: {nivel} {barra}")
    print(progresso)
    print(f"Pontos: {pontos}")
    print(f"Streak: {usuario.get('streak', 0)} dia(s)")
    print(f"Média de humor: {media:.1f}" if media else "Média de humor: sem dados")
    print(f"Emoção mais frequente: {emocao}")

    print("\nConquistas:")
    for nome, descricao in CONQUISTAS.items():
        status = "✔" if nome in usuario.get("conquistas", []) else "🔒"
        print(f"{status} {nome} — {descricao}")

    pausar()


# ============================================================
# CHECK-IN DE HUMOR
# ============================================================

def realizar_checkin(usuario):
    """Registra um check-in diário, atualiza pontos e avalia sequência."""
    cabecalho("CHECK-IN DE HUMOR")
    hoje = date.today().isoformat()

    if usuario.get("ultimo_checkin") == hoje:
        print("ℹ Você já fez seu check-in hoje. Amanhã tem mais um momento para você.")
        pausar()
        return

    nota = pedir_inteiro("Como você está hoje? Dê uma nota de 1 a 5: ", 1, 5)

    print("\nEscolha a emoção que mais se aproxima do que sente:")
    for indice, emocao in enumerate(EMOCOES, start=1):
        print(f"{indice}. {emocao.capitalize()}")

    escolha = pedir_inteiro("Número da emoção: ", 1, len(EMOCOES))
    emocao = EMOCOES[escolha - 1]
    anotacao = pedir_texto(
        "Quer deixar uma anotação? (opcional): ",
        0,
        200,
        permitir_vazio=True
    )

    if anotacao and detectar_risco(anotacao):
        mostrar_apoio()
        pausar()
        return

    registro = {
        "data": hoje,
        "nota": nota,
        "emocao": emocao,
        "anotacao": anotacao,
    }

    usuario.setdefault("checkins", []).append(registro)
    adicionar_pontos(usuario, 10)
    streak = atualizar_streak(usuario)
    verificar_conquistas(usuario)

    # Verifica se houve nota baixa em três dias consecutivos, incluindo hoje.
    datas_baixas = {
        item["data"]
        for item in usuario["checkins"]
        if item["nota"] <= 2
    }
    tres_dias_baixos = all(
        (date.today() - timedelta(days=deslocamento)).isoformat() in datas_baixas
        for deslocamento in range(3)
    )

    if tres_dias_baixos:
        print("\nBimo: Percebi que os últimos dias parecem estar difíceis.")
        print("Se fizer sentido, conversar com um profissional pode ajudar.")
        print("CVV 188 (24h, gratuito) | cvv.org.br | Emergência: SAMU 192.")

    if nota <= 2:
        resposta = "Obrigado por me contar. Vamos com calma, um passo de cada vez."
    elif nota == 3:
        resposta = "Obrigado pelo check-in. Nem todo dia precisa ser extraordinário."
    else:
        resposta = "Que bom registrar um momento positivo! Aproveite essa sensação."

    print(f"\nBimo: {resposta}")
    print(f"✔ Check-in salvo. +10 pontos. Streak atual: {streak} dia(s).")
    pausar()


# ============================================================
# CONVERSA COM O BIMO
# ============================================================

def resposta_por_humor(usuario):
    """Escolhe uma frase de acordo com o último humor e personalidade."""
    checkins = usuario.get("checkins", [])

    if not checkins:
        return "Que tal começar com um check-in? Assim consigo acompanhar como você está."

    nota = checkins[-1]["nota"]

    if nota <= 2:
        faixa = "baixo"
    elif nota == 3:
        faixa = "neutro"
    else:
        faixa = "bom"

    personalidade = usuario.get("personalidade", "acolhedor")

    match personalidade:
        case "acolhedor":
            frases = FRASES["acolhedor"][faixa]
        case "divertido":
            frases = FRASES["divertido"][faixa]
        case "calmo":
            frases = FRASES["calmo"][faixa]
        case _:
            frases = FRASES["acolhedor"][faixa]

    return random.choice(frases)


def responder_mensagem(texto, usuario):
    """Responde a palavras-chave sem utilizar inteligência artificial externa."""
    texto_normalizado = normalizar_texto(texto)

    if detectar_risco(texto):
        return "RISCO"
    elif "obrigado" in texto_normalizado or "obrigada" in texto_normalizado:
        return "Você não precisa agradecer. Fico feliz em acompanhar esse momento."
    elif "ajuda" in texto_normalizado:
        return "Posso te ouvir. Se precisar, procure também alguém de confiança."
    elif "triste" in texto_normalizado or "ansioso" in texto_normalizado:
        return "Sinto muito que esteja assim. Quer me contar um pouco mais?"
    elif "feliz" in texto_normalizado or "bem" in texto_normalizado:
        return "Que bom! O que contribuiu para você se sentir assim?"
    else:
        return resposta_por_humor(usuario)


def conversar(usuario):
    """Executa o mini-loop de conversa e concede no máximo 5 pontos por dia."""
    cabecalho("CONVERSANDO COM O BIMO")
    print(f"Bimo: {resposta_por_humor(usuario)}")
    print("Digite uma mensagem curta. Escreva 'sair' para voltar ao menu.")

    encontrou_risco = False
    houve_interacao = False

    while True:
        mensagem = input("\nVocê: ").strip()

        if mensagem.lower() == "sair":
            print("Bimo: Até logo. Obrigado por conversar comigo.")
            break

        if not mensagem:
            print("Bimo: Pode escrever quando se sentir à vontade.")
            continue

        houve_interacao = True

        if detectar_risco(mensagem):
            mostrar_apoio()
            encontrou_risco = True
            break

        resposta = responder_mensagem(mensagem, usuario)

        if resposta == "RISCO":
            mostrar_apoio()
            encontrou_risco = True
            break

        print(f"Bimo: {resposta}")

    # Pontos só são concedidos depois de uma conversa sem detecção de risco.
    hoje = date.today().isoformat()
    if houve_interacao and not encontrou_risco and usuario.get("ultima_conversa") != hoje:
        adicionar_pontos(usuario, 5)
        usuario["ultima_conversa"] = hoje
        usuario["conversou"] = True
        verificar_conquistas(usuario)
        print("✔ +5 pontos por reservar um momento para conversar.")

    pausar()


# ============================================================
# MODO DIÁRIO
# ============================================================

def escrever_entrada(usuario):
    """Cria uma entrada no diário após verificar o conteúdo."""
    cabecalho("NOVA ENTRADA")
    texto = pedir_texto("Escreva (5 a 500 caracteres): ", 5, 500)

    if detectar_risco(texto):
        mostrar_apoio()
        return

    usuario.setdefault("diario", []).append({
        "data": date.today().isoformat(),
        "texto": texto,
    })

    adicionar_pontos(usuario, 15)
    verificar_conquistas(usuario)
    print("✔ Entrada salva. +15 pontos.")


def listar_entradas(usuario):
    """Lista as entradas da mais recente para a mais antiga."""
    cabecalho("SEU DIÁRIO")
    entradas = usuario.get("diario", [])

    if not entradas:
        print("Ainda não há entradas no diário.")
    else:
        for indice, entrada in enumerate(reversed(entradas), start=1):
            print(f"\n{indice}. {entrada['data']}")
            print(entrada["texto"])

    pausar()


def apagar_entrada(usuario):
    """Apaga uma entrada após validar o número e pedir confirmação."""
    entradas = usuario.get("diario", [])

    if not entradas:
        print("ℹ Não há entradas para apagar.")
        pausar()
        return

    cabecalho("APAGAR ENTRADA")
    entradas_recentes = list(reversed(entradas))

    for indice, entrada in enumerate(entradas_recentes, start=1):
        resumo = entrada["texto"][:55]
        print(f"{indice}. {entrada['data']} — {resumo}")

    numero = pedir_inteiro("Número da entrada a apagar: ", 1, len(entradas))

    if confirmar("Tem certeza de que deseja apagar essa entrada?"):
        indice_original = len(entradas) - numero
        removida = entradas.pop(indice_original)
        print(f"✔ Entrada de {removida['data']} apagada.")
    else:
        print("ℹ Exclusão cancelada.")

    pausar()


def menu_diario(usuario):
    """Controla o submenu do diário."""
    while True:
        cabecalho("MODO DIÁRIO")
        print("1. Escrever entrada")
        print("2. Ler entradas")
        print("3. Apagar entrada")
        print("0. Voltar")

        opcao = pedir_inteiro("Escolha: ", 0, 3)

        match opcao:
            case 1:
                escrever_entrada(usuario)
                pausar()
            case 2:
                listar_entradas(usuario)
            case 3:
                apagar_entrada(usuario)
            case 0:
                break


# ============================================================
# PERSONALIDADE
# ============================================================

def configurar_personalidade(usuario):
    """Permite alterar a personalidade do Bimo."""
    while True:
        cabecalho("PERSONALIDADE DO BIMO")
        print(f"Personalidade atual: {usuario['personalidade']}")
        print("1. Acolhedor")
        print("2. Divertido")
        print("3. Calmo")
        print("0. Voltar")

        opcao = pedir_inteiro("Escolha: ", 0, 3)

        match opcao:
            case 1:
                usuario["personalidade"] = "acolhedor"
            case 2:
                usuario["personalidade"] = "divertido"
            case 3:
                usuario["personalidade"] = "calmo"
            case 0:
                return

        if opcao != 0:
            print(f"✔ Personalidade alterada para {usuario['personalidade']}.")
            pausar()


# ============================================================
# MENU PRINCIPAL E EXECUÇÃO
# ============================================================

def mostrar_menu(usuario):
    """Mostra o menu e as informações do perfil conectado."""
    cabecalho("BIMO | SEU COMPANHEIRO DE BEM-ESTAR")

    if usuario:
        nivel, _ = obter_nivel(usuario.get("pontos", 0))
        print(f"Olá, {usuario['nome']}!  |  Nível: {nivel}")
    else:
        print("Você ainda não entrou em um perfil.")

    print("\n1. Cadastro / Login")
    print("2. Check-in de humor")
    print("3. Conversar com o Bimo")
    print("4. Modo diário")
    print("5. Configurar personalidade")
    print("6. Recompensas")
    print("0. Sair")

    mostrar_aviso_fixo(curto=True)


def main():
    """Inicia o Bimo e mantém o menu principal em execução."""
    dados = carregar_dados()
    usuario = None

    try:
        cabecalho("BIMO")
        print("Olá! Eu sou o Bimo, seu companheiro de bem-estar.")
        print("A Global Solution 2026.2 apresenta o desafio CitizenTech:")
        print("criar tecnologia a partir das necessidades reais das pessoas.")
        print("O Bimo atua na área de Saúde, oferecendo uma ferramenta simples")
        print("para apoiar hábitos de autocuidado e organizar percepções pessoais.")
        print("Funciona localmente no terminal, sem exigir conexão com a internet.")
        mostrar_aviso_fixo()
        pausar()

        while True:
            limpar_tela()
            mostrar_menu(usuario)
            opcao = pedir_inteiro("Escolha uma opção: ", 0, 6)

            match opcao:
                case 1:
                    usuario = acessar_usuario(dados)

                case 2:
                    if usuario is None:
                        print("ℹ Faça cadastro ou login para acessar essa funcionalidade.")
                        pausar()
                    else:
                        realizar_checkin(usuario)

                case 3:
                    if usuario is None:
                        print("ℹ Faça cadastro ou login para acessar essa funcionalidade.")
                        pausar()
                    else:
                        conversar(usuario)

                case 4:
                    if usuario is None:
                        print("ℹ Faça cadastro ou login para acessar essa funcionalidade.")
                        pausar()
                    else:
                        menu_diario(usuario)

                case 5:
                    if usuario is None:
                        print("ℹ Faça cadastro ou login para acessar essa funcionalidade.")
                        pausar()
                    else:
                        configurar_personalidade(usuario)

                case 6:
                    if usuario is None:
                        print("ℹ Faça cadastro ou login para acessar essa funcionalidade.")
                        pausar()
                    else:
                        mostrar_recompensas(usuario)

                case 0:
                    salvar_dados(dados)
                    print("\nBimo: Obrigado por reservar um momento para você.")
                    print("Cuide-se. Até a próxima! 💚")
                    break

            salvar_dados(dados)

    except (KeyboardInterrupt, EOFError):
        print("\n\nBimo: Tudo bem pausar por aqui. Vou salvar seu progresso.")
    finally:
        salvar_dados(dados)


if __name__ == "__main__":
    main()