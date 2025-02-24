import os
import json
import pandas as pd

def saveJson(data, filePath):
    os.makedirs(os.path.dirname(filePath), exist_ok=True)

    with open(filePath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"\nSON salvo com sucesso em: {filePath}\n")

def loadJson(filePath):
    if not os.path.exists(filePath):
        print(f"\nErro: Arquivo {filePath} não encontrado.\n")
        return None

    with open(filePath, "r", encoding="utf-8") as f:
        print(f"\nCarregando JSON: {filePath}...\n")
        return json.load(f)

def saveXLSX(dataFrame, filePath):
    os.makedirs(os.path.dirname(filePath), exist_ok=True)

    dataFrame.to_excel(filePath, index=False, engine="openpyxl")

    print(f"\nXLSX salvo com sucesso em: {filePath}\n")
