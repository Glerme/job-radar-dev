# Config do programa internacional (busca vaga remota fora do Brasil que
# aceita/pede português ou espanhol). Separado do config.py de propósito —
# ver decisão registrada na conversa: misturar ia forçar o filtro de cidade
# do Nordeste e as keywords em português do JobRadar original a servir dois
# propósitos diferentes ao mesmo tempo, deixando os dois mais frágeis.
#
# Credenciais do Telegram e caminho do banco são os MESMOS do projeto
# principal (reaproveita o bot já configurado, e o dedup por link no mesmo
# jobs.db não tem risco de colisão — o id é hash do link, e vaga
# internacional nunca vai ter o mesmo link de uma vaga brasileira).
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, DB_PATH, CIDADES_EUROPA_IBERICA  # noqa: F401

# Cargo em múltiplos idiomas — vaga internacional pode ter o anúncio escrito
# em inglês, português ou espanhol, dependendo de quem contratou.
KEYWORDS_INTL = [
    "Frontend Developer",
    "Front-end Developer",
    "Full Stack Developer",
    "Fullstack Developer",
    "React Developer",
    "Frontend Engineer",
    "Full Stack Engineer",
    "React Engineer",
    "Desenvolvedor Frontend",
    "Desenvolvedor Front-end",
    "Desenvolvedor Full Stack",
    "Desenvolvedor React",
    "Desarrollador Frontend",
    "Desarrollador Full Stack",
    "Desarrollador React",
    "Ingeniero Frontend",
    "Ingeniero Full Stack",
    "Ingeniero de Software Frontend",
]

# Termos de busca: cargo front-end/fullstack + sinal de idioma (português/
# espanhol/bilíngue) ou mercado (LATAM, Spanish Market).
TERMOS_BUSCA_INTL = [
    "frontend developer spanish speaker",
    "frontend developer spanish speaking",
    "frontend developer portuguese speaker",
    "frontend developer portuguese speaking",
    "full stack developer spanish speaker",
    "full stack developer spanish speaking",
    "full stack developer portuguese speaker",
    "full stack developer portuguese speaking",
    "react developer spanish speaker",
    "react developer portuguese speaker",
    "remote frontend developer latam",
    "remote full stack developer latam",
    "remote full stack developer latin america",
    "frontend developer spanish market",
    "desarrollador frontend remoto",
    "desarrollador full stack remoto",
    "frontend developer",
    "full stack developer",
    "react developer",
    "spanish speaker",
    "spanish speaking",
    "portuguese and spanish",
    "spanish market",
    "latam",
]

IDIOMAS_EXIGIDOS_INTL = [
    "spanish",
    "espanol",
    "español",
    "portuguese",
    "português",
    "portugues",
    "latam",
    "latin america",
    "america latina",
    "hispanohablante",
    "lusofono",
    "lusófono",
]

TERMOS_POR_CICLO_INTL = 10

LOCATIONS_INTL = [
    "Spain",
    "Portugal",
    "Mexico",
    "Colombia",
    "Argentina",
    "Chile",
]

CIDADES_INTL = ["Remote", "Remoto"]

MERCADOS_REMOTO_ACEITOS_INTL = [
    "Portugal",
    "Espanha",
    "México",
    "Colômbia",
    "Argentina",
    "Chile",
    "Peru",
    "Uruguai",
    "Paraguai",
    "Bolívia",
    "Equador",
    "Venezuela",
    "Costa Rica",
    "Panamá",
    "Guatemala",
    "Honduras",
    "El Salvador",
    "Nicarágua",
    "República Dominicana",
    "Porto Rico",
    "Cuba",
    "Angola",
    "Moçambique",
    "Cabo Verde",
    "LATAM",
]

ATIVAR_EIXO_IBERICO = False

DOMINIOS_INDEED_INTL = {
    "Espanha": "es.indeed.com",
    "Portugal": "pt.indeed.com",
    "México": "mx.indeed.com",
    "Colômbia": "co.indeed.com",
    "Argentina": "ar.indeed.com",
    "Chile": "cl.indeed.com",
}
