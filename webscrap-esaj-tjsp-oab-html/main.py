import subprocess
import os

def runWebScrap():
    print("\n=== Iniciando Web Scraping dos processos... ===\n")
    subprocess.run(["python3", "scripts/webScrap.py"], check=True)

def runJsonToXLSX(jsonFileName):
    print(f"\n=== Convertendo {jsonFileName} para XLSX... ===\n")
    subprocess.run(["python3", "scripts/jsonToXLSX.py"], input=jsonFileName.encode(), check=True)

def getLatestFile(directory, prefix, extension):
    files = [f for f in os.listdir(directory) if f.startswith(prefix) and f.endswith(extension)]
    if not files:
        return None
    return max(files, key=lambda f: os.path.getctime(os.path.join(directory, f)))

def askUserForNewQuery():
    response = input("\nDeseja realizar outra consulta? (s/n): ").strip().lower()
    return response == "s"

def main():
    print("\n=== Sistema de Web Scraping do TJSP ===\n")

    while True:
        jsonFile = getLatestFile("data/json", "oab-", ".json")
        xlsxFile = getLatestFile("data/xlsx", "oab-", ".xlsx")

        if jsonFile or xlsxFile:
            print("\nArquivos anteriores detectados:")
            if jsonFile:
                print(f" - Último JSON encontrado: {jsonFile}")
            if xlsxFile:
                print(f" - Último XLSX encontrado: {xlsxFile}")
            
            if not askUserForNewQuery():
                print("\nEncerrando o programa.\n")
                return

        runWebScrap()

        jsonFile = getLatestFile("data/json", "oab-", ".json")
        if jsonFile:
            runJsonToXLSX(jsonFile)

        if not askUserForNewQuery():
            print("\nEncerrando o programa.\n")
            return

if __name__ == "__main__":
    main()
