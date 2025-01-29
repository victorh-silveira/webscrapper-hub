import requests
import base64
import json
import os
from typing import List, Dict, Optional

BASE_URL = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36"
}
PAGE_SIZE = 120
TOTAL_PAGES = 25


def encodeToBase64(pageNumber: int, pageSize: int = PAGE_SIZE) -> str:
    payload = json.dumps({
        "language": "pt-br",
        "pageNumber": pageNumber,
        "pageSize": pageSize
    })
    return base64.b64encode(payload.encode()).decode()


def fetchPageData(pageNumber: int) -> Optional[List[Dict[str, str]]]:
    url = f"{BASE_URL}{encodeToBase64(pageNumber)}"
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        return [{"companyName": item["companyName"]} for item in data.get("results", [])]

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar página {pageNumber}: {e}")
        return None


def saveToFile(data: List[Dict[str, str]], jsonFileName: str, txtFileName: str):
    try:
        with open(jsonFileName, "w", encoding="utf-8") as jsonFile:
            json.dump(data, jsonFile, indent=4, ensure_ascii=False)

        with open(txtFileName, "w", encoding="utf-8") as txtFile:
            for empresa in data:
                txtFile.write(empresa["companyName"] + "\n")

        print(f"\nDados salvos em '{jsonFileName}' e '{txtFileName}'.")

    except IOError as e:
        print(f"Erro ao salvar arquivos: {e}")


def main():
    empresas = []
    
    for page in range(1, TOTAL_PAGES + 1):
        pageData = fetchPageData(page)
        if pageData:
            empresas.extend(pageData)
            os.system('clear')
            print(f"Página {page} coletada com sucesso!")

    if empresas:
        saveToFile(empresas, "empresasListadas.json", "empresasListadas.txt")
    else:
        print("Nenhum dado foi coletado.")


if __name__ == "__main__":
    main()
