import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, ScraperWebsiteTool
from crewai import Agent, Task, Crew
from datetime import date

# Carregar variáveis de ambiente
load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Ferramentas
search_tool = SerperDevTool()
scrape_tool = ScraperWebsiteTool()

# Agentes
buscador = Agent(
    role="Buscador de Conteúdo",
    goal="Buscar conteúdo online sobre o tema {tema}",
    backstory=(
        "Você está trabalhando na criação de artigos para o LinkedIn sobre o tema {tema}. "
        "Sua função é buscar informações relevantes na internet, coletá-las e organizá-las. "
        "Esse conteúdo será usado como base pelo redator."
    ),
    tools=[search_tool, scrape_tool],
    verbose=True,
)

redator = Agent(
    role="Redator de Conteúdo",
    goal="Escrever conteúdo para o LinkedIn sobre o tema {tema}",
    backstory=(
        "Você está redigindo um artigo para o LinkedIn sobre o tema {tema}. "
        "Utilize os dados coletados pelo buscador para escrever um texto interessante, divertido e factual. "
        "Você pode dar opiniões, mas deixe claro que são pessoais."
    ),
    tools=[search_tool, scrape_tool],
    verbose=True,
)

editor = Agent(
    role="Editor de Conteúdo",
    goal="Editar o texto do LinkedIn para deixá-lo mais informal",
    backstory=(
        "Você vai receber um texto do redator e editá-lo para o tom de voz do João Lucas (João dos Dados), "
        "que é mais informal, leve e divertido."
    ),
    tools=[search_tool, scrape_tool],
    verbose=True,
)

# Tarefas
buscar = Task(
    description=(
        "1. Priorize as tendências mais recentes, os principais atores e as notícias relevantes sobre o tema {tema}. "
        "2. Identifique o público-alvo, destacando seus interesses e principais dores. "
        "3. Liste tópicos e subtópicos relevantes que podem ser abordados no artigo. "
        "4. Inclua palavras-chave otimizadas para SEO e fontes confiáveis."
    ),
    agent=buscador,
    expected_output=(
        "Um plano com tendências sobre o tema {tema}, palavras-chave de SEO relevantes e as últimas notícias."
    ),
)

redigir = Task(
    description=(
        "1. Utilize os dados coletados para redigir um post atrativo para o LinkedIn sobre o tema {tema}. "
        "2. Insira palavras-chave de SEO de maneira orgânica. "
        "3. Estruture o texto de forma envolvente, finalizando com uma conclusão reflexiva."
    ),
    agent=redator,
    expected_output="Um texto para o LinkedIn sobre o tema {tema}.",
)

editar = Task(
    description=(
        "1. Revise o texto para corrigir erros gramaticais. "
        "2. Adapte o tom de voz para refletir a personalidade de João Lucas (João dos Dados): mais informal, leve e divertido. "
        "3. Verifique se o texto está bem dividido em parágrafos e evita o uso de bullet points."
    ),
    agent=editor,
    expected_output=(
        "Um texto final para o LinkedIn, pronto para publicação, com o tom de voz desejado e formatação adequada."
    ),
)

# Equipe
equipe = Crew(
    agents=[buscador, redator, editor], tasks=[buscar, redigir, editar], verbose=True
)

# Execução
tema = "Nova profissão: Engenheiro de IA"
input_dict = {"tema": tema}

result = equipe.kickoff(inputs=input_dict)

# Exibir resultado em Markdown
markdown_output = f"""
## Resultado Final: Post para o LinkedIn

{result}
"""

print(markdown_output)

# Exportar resultado para arquivo markdown na pasta posts/
today = date.today().isoformat()
os.makedirs("posts", exist_ok=True)
filename = f"posts/result-data-{today}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(markdown_output)

print(f"Resultado exportado para {filename}")
