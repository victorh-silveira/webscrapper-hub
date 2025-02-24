import os
import json
import pandas as pd

def flattenCaseData(caseData):
    flattenedData = []

    for case in caseData:
        baseData = {
            "numero": case["numero"],
            "advogado": case["advogado"],
            "tipo": case["tipo"],
            "assunto": case["assunto"],
            "recebidoEm": case["recebidoEm"],
            "vara": case["vara"],
            "pagina": case["pagina"]
        }

        if case["processoFilhos"]:
            for i, child in enumerate(case["processoFilhos"], start=1):
                childData = {
                    f"filho{i}_numero": child["numero"],
                    f"filho{i}_tipo": child["tipo"],
                    f"filho{i}_assunto": child["assunto"],
                    f"filho{i}_recebidoEm": child["recebidoEm"],
                    f"filho{i}_vara": child["vara"],
                    f"filho{i}_pagina": child["pagina"]
                }
                flattenedData.append({**baseData, **childData})
        else:
            flattenedData.append(baseData)

    return flattenedData

def jsonToXLSX(jsonFilePath):
    print("\n=== Conversão de JSON para XLSX ===\n")

    if not os.path.exists(jsonFilePath):
        print(f"Erro: Arquivo {jsonFilePath} não encontrado.\n")
        return

    print(f"Lendo arquivo JSON: {jsonFilePath}...\n")

    with open(jsonFilePath, "r", encoding="utf-8") as file:
        caseData = json.load(file)

    print("Processando dados para conversão...\n")

    flattenedData = flattenCaseData(caseData)
    df = pd.DataFrame(flattenedData)

    xlsxFilePath = jsonFilePath.replace("data/json/", "data/xlsx/").replace(".json", ".xlsx")
    os.makedirs(os.path.dirname(xlsxFilePath), exist_ok=True)

    print(f"Salvando arquivo XLSX em: {xlsxFilePath}...\n")
    df.to_excel(xlsxFilePath, index=False, engine="openpyxl")

    print(f"Conversão concluída com sucesso! Arquivo salvo em:\n{xlsxFilePath}\n")

if __name__ == "__main__":
    print("\n=== Conversor de Processos para XLSX ===\n")
    jsonFileName = input("Digite o nome do arquivo JSON gerado (ex: oab-123456.json): ").strip()

    jsonFilePath = os.path.join("data/json", jsonFileName)

    jsonToXLSX(jsonFilePath)
