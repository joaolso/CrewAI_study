# 🤖 LinkedIn Post Crew

Este projeto automatiza a criação de posts para o LinkedIn com uso de agentes inteligentes da biblioteca [CrewAI](https://docs.crewai.com/), em conjunto com ferramentas de busca e scraping. O objetivo é gerar conteúdos atualizados, personalizados e com tom informal para a persona João Lucas (João dos Dados).

## ✨ Visão Geral

O fluxo da aplicação é dividido em três agentes principais:

1. **Buscador de Conteúdo**: coleta tendências, notícias recentes e dados relevantes sobre o tema.
2. **Redator de Conteúdo**: cria um texto informativo, divertido e com boas práticas de SEO.
3. **Editor de Conteúdo**: ajusta o texto para o tom de voz de João Lucas — leve, informal e descontraído.

## 🛠️ Tecnologias Utilizadas

- Python
- [CrewAI](https://pypi.org/project/crewai/)
- [crewAI-tools](https://pypi.org/project/crewai-tools/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Serper API (para busca de informações)
- ScraperWebsiteTool (para extração de conteúdo)

## 📁 Estrutura do Script

- Carregamento de chaves de API com `dotenv`
- Definição de três agentes com responsabilidades distintas
- Criação de três tarefas encadeadas com base em um tema
- Execução do fluxo de trabalho completo com o tema definido
- Exportação do resultado final em **formato Markdown** na pasta `posts/`

## ⚙️ Pré-requisitos

- Python 3.10 ou superior
- Arquivo `.env` com suas chaves de API:
  ```
  OPENAI_API_KEY=your_openai_key
  SERPER_API_KEY=your_serper_key
  ```

## 🚀 Como Executar

1. Instale as dependências:
   ```bash
   pip install crewai crewai-tools python-dotenv
   ```

2. Defina o tema no próprio script:
   ```python
   tema = "Nova profissão: Engenheiro de IA"
   ```

3. Execute o script:
   ```bash
   python linkedin_post_crew.py
   ```

4. O conteúdo gerado será:
   - Impresso no terminal em formato Markdown
   - Salvo automaticamente no arquivo:
     ```
     posts/result-data-YYYY-MM-DD.md
     ```

## ✏️ Personalização

Você pode adaptar os papéis dos agentes, suas tarefas e o estilo da persona final (João dos Dados). Basta alterar os campos `role`, `goal`, `backstory` e `description` das `Task`.

## 📄 Licença

MIT © João dos Dados
