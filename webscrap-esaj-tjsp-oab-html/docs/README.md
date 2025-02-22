# WebScrapGabriel

Este projeto realiza **web scraping** para extrair dados de processos judiciais e converte os resultados de **JSON** para **XLSX**.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/WebScrapGabriel.git
   cd WebScrapGabriel
Crie um ambiente virtual (opcional):

sh
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
Instale as dependências:

sh
Copiar
Editar
pip install -r docs/requirements.txt
Uso
Para executar o scraping e a conversão:

sh
Copiar
Editar
python main.py
Os arquivos JSON gerados ficarão em data/json/ e os XLSX em data/xlsx/.

Estrutura do Projeto
bash
Copiar
Editar
📦 WebScrapGabriel
 ┣ 📂 data         # Armazena os arquivos JSON e XLSX
 ┣ 📂 docs         # Documentação e dependências
 ┣ 📂 logs         # Logs de execução
 ┣ 📂 scripts      # Código principal
 ┣ 🐍 main.py      # Arquivo principal
 ┣ 🐳 Dockerfile   # Configuração do Docker
 ┣ 📄 README.md    # Documentação
 ┗ 📄 .gitignore   # Ignora arquivos desnecessários no Git
Docker
Para rodar o projeto via Docker:

sh
Copiar
Editar
docker build -t webscrapgabriel .
docker run --rm -v "$(pwd)/data:/app/data" webscrapgabriel
Licença
Este projeto está sob a Licença MIT.

yaml
Copiar
Editar

---

Agora é só **copiar e colar** no seu `README.md`, sem fragmentação. Pronto!
