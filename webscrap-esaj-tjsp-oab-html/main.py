import os
from scripts.webScraper import runScraper
from scripts.jsonToXlsx import convertJsonToXlsx

# Definir os diretórios de entrada e saída
JSON_DIR = "data/json"
XLSX_DIR = "data/xlsx"

def main():
    # Criar diretórios se não existirem
    os.makedirs(JSON_DIR, exist_ok=True)
    os.makedirs(XLSX_DIR, exist_ok=True)

    print("Iniciando o web scraping...")
    runScraper()  # Executa o web scraper e gera arquivos JSON na pasta data/json
    print("Web scraping concluído.")

    print("Convertendo arquivos JSON para XLSX...")
    for json_file in os.listdir(JSON_DIR):
        if json_file.endswith(".json"):
            json_path = os.path.join(JSON_DIR, json_file)
            xlsx_filename = json_file.replace(".json", ".xlsx")
            xlsx_path = os.path.join(XLSX_DIR, xlsx_filename)
            convertJsonToXlsx(json_path, xlsx_path)

    print("Conversão concluída. Todos os arquivos XLSX foram gerados.")

if __name__ == "__main__":
    main()
