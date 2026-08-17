import os
from dotenv import load_dotenv

load_dotenv()

# Cargo forte: título que só existe mesmo em vaga de front-end/fullstack, sem
# possibilidade real de ser outra área.
KEYWORDS_CARGO_FORTE = [
    "Desenvolvedor Frontend",
    "Desenvolvedor Front-end",
    "Desenvolvedor Full Stack",
    "Desenvolvedor Fullstack",
    "Desenvolvedor React",
    "Desenvolvedor Next.js",
    "Engenheiro Frontend",
    "Frontend Engineer",
    "Full Stack Engineer",
    "Fullstack Engineer",
    "React Engineer",
    "Next.js Engineer",
]

# Cargo ambíguo: título que também é usado em vaga sem nada a ver com
# front-end/fullstack (ex: "Developer" e "Engineer" existem em backend,
# mobile, dados...). Só conta como match se o título TAMBÉM tiver um
# QUALIFICADORES_STACK junto.
KEYWORDS_CARGO_AMBIGUO = [
    "Engineer",
    "Developer",
    "Software Developer",
    "Frontend Developer",
    "Front-end Developer",
    "Full Stack Developer",
    "Fullstack Developer",
    "React Developer",
    "Web Developer",
]

# Termo que precisa aparecer junto no título quando o cargo é ambíguo, pra
# confirmar que é vaga de front-end/fullstack e não de outra área qualquer.
QUALIFICADORES_STACK = [
    "frontend",
    "front-end",
    "front end",
    "fullstack",
    "full stack",
    "full-stack",
    "react",
    "next.js",
    "nextjs",
    "typescript",
    "javascript",
    "vue",
    "angular",
    "node.js",
    "nodejs",
    "tailwind",
]

# Ferramenta que aparece como núcleo do título ("Desenvolvedor React").
# Só conta como match se o título TAMBÉM tiver uma palavra de cargo — espelho
# da regra de KEYWORDS_CARGO_AMBIGUO: lá o cargo é ambíguo e pede stack, aqui
# a ferramenta é ambígua e pede cargo.
FERRAMENTAS_TITULO = [
    "React",
    "Next.js",
    "Vue",
    "Angular",
    "TypeScript",
]

# Palavra de cargo que confirma que a vaga de ferramenta é de desenvolvimento.
QUALIFICADORES_CARGO = [
    "desenvolvedor",
    "developer",
    "engenheiro",
    "engineer",
    "frontend",
    "front-end",
    "full stack",
    "fullstack",
]

KEYWORDS = KEYWORDS_CARGO_FORTE + KEYWORDS_CARGO_AMBIGUO

# Termos de busca enviados a cada site. Ficam separados das KEYWORDS de
# propósito: TERMOS_BUSCA é a rede ampla (o que é pesquisado em cada site,
# incluindo termos de ferramenta/stack pra achar vaga com título atípico),
# enquanto KEYWORDS é o filtro final e só olha o título da vaga já
# encontrada. Um termo de ferramenta (ex: "react") só resulta em notificação
# se o TÍTULO da vaga também bater com uma keyword de cargo.
TERMOS_CARGO_EXTRA = [
    "frontend",
    "front-end",
    "full stack",
    "fullstack",
    "react",
    "next.js",
    "typescript",
    "javascript",
    "vue",
    "angular",
    "node.js",
    "tailwind",
]

TERMOS_CARGO = sorted(set(k.lower() for k in KEYWORDS) | set(TERMOS_CARGO_EXTRA))

TERMOS_FERRAMENTA = [
    "react",
    "next.js",
    "typescript",
    "javascript",
    "vue",
    "angular",
    "tailwind",
    "node.js",
]

TERMOS_BUSCA = TERMOS_CARGO + TERMOS_FERRAMENTA

TERMOS_POR_CICLO = 10

CIDADES = [
    "Remoto",
    "Campina Grande",
    "João Pessoa",
    "Recife",
    "Natal",
    "Maceió",
    "Jaboatão",
    "Aracaju",
    "Teresina",
    "São Luís",
    "Petrolina",
    "Caruaru",
]

CIDADES_EUROPA_IBERICA = [
    "Portugal",
    "Lisboa",
    "Porto",
    "Braga",
    "Espanha",
    "España",
    "Spain",
    "Madrid",
    "Barcelona",
    "Valencia",
]

ATIVAR_EIXO_IBERICO_BR = False

LOCATIONS_LINKEDIN = ["Brasil"]

LOCATIONS_LINKEDIN_REMOTO_APENAS = [
    "Argentina",
    "Chile",
    "México",
    "Colômbia",
    "Espanha",
    "Portugal",
]

MERCADOS_REMOTO_ACEITOS = [
    "Brasil",
    "LATAM",
    "Argentina",
    "Chile",
    "México",
    "Colômbia",
    "Portugal",
    "Espanha",
]

INTERVALO_MINUTOS = int(os.getenv("INTERVALO_MINUTOS", 180))

LIMIAR_DIGEST_IMEDIATO = 7

DIGEST_HORA_UTC = 0

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "jobs.db")
