# WebScrapGabriel

Este projeto realiza **web scraping** para extrair dados de processos judiciais e converte os arquivos **JSON** resultantes para **XLSX**.

---

## 📌 Índice
- [Descrição](#descrição)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Execução](#execução)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Docker](#docker)
- [Licença](#licença)

---

## 📌 Descrição

O projeto acessa um site jurídico, coleta dados sobre processos e armazena os resultados no formato **JSON**. Em seguida, converte os arquivos JSON em planilhas **XLSX** para melhor visualização e análise dos dados.

---

## 📌 Tecnologias Utilizadas

- **Python 3.10**
- **BeautifulSoup4** (para scraping de HTML)
- **Requests** (para requisições HTTP)
- **Pandas** (para manipulação de dados)
- **OpenPyXL** (para conversão de JSON para XLSX)
- **Docker** (opcional para ambiente isolado)

---

## 📌 Pré-requisitos

Antes de rodar o projeto, certifique-se de ter instalado:

- **Python 3.10+**
- **Pip** (gerenciador de pacotes do Python)
- **Docker** (caso queira rodar o projeto em container)

---

## 📌 Instalação

### **Clone o repositório**
```sh
git clone https://github.com/seu-usuario/WebScrapGabriel.git
cd WebScrapGabriel
Crie um ambiente virtual (opcional, mas recomendado)
sh
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
Instale as dependências
sh
Copiar
Editar
pip install -r docs/requirements.txt
📌 Execução
Executando diretamente no Python
Após instalar as dependências, basta rodar:

sh
Copiar
Editar
python main.py
O programa fará:

Web scraping e salvará os dados JSON em data/json/.
Conversão automática dos JSONs para XLSX em data/xlsx/.
📌 Estrutura do Projeto
graphql
Copiar
Editar
📦 WebScrapGabriel
 ┣ 📂 data               # Armazena os arquivos de saída
 ┃ ┣ 📂 json             # Arquivos JSON gerados pelo scraper
 ┃ ┣ 📂 xlsx             # Arquivos XLSX convertidos do JSON
 ┣ 📂 docs               # Documentação e dependências
 ┣ 📂 logs               # Logs de execução e erros
 ┣ 📂 scripts            # Scripts principais do projeto
 ┃ ┣ 🐍 webScraper.py    # Código de scraping
 ┃ ┣ 🐍 jsonToXlsx.py    # Conversão de JSON para XLSX
 ┃ ┣ 🐍 config.py        # Configurações globais
 ┣ 🐍 main.py            # Arquivo principal para rodar o pipeline
 ┣ 🐳 Dockerfile         # Arquivo para rodar o projeto via Docker
 ┣ 📄 README.md          # Documentação do projeto
 ┣ 📄 .gitignore         # Ignora arquivos desnecessários no Git
📌 Docker
Caso queira rodar o projeto via Docker, siga os passos:

1. Construir a imagem
sh
Copiar
Editar
docker build -t webscrapgabriel .
2. Rodar o container
sh
Copiar
Editar
docker run --rm -v "$(pwd)/data:/app/data" webscrapgabriel
Isso executará o scraper e salvará os arquivos JSON e XLSX na pasta data/.

📌 Licença
Este projeto está sob a Licença MIT. Você pode usá-lo e modificá-lo livremente.

yaml
Copiar
Editar

---

### **📌 Como usar**
1. **Copie** o conteúdo acima.
2. **Cole no seu `README.md` no VSCode`.**
3. **Salve e envie para o GitHub**:

```sh
git add README.md
git commit -m "Adicionando README.md formatado"
git push origin main
