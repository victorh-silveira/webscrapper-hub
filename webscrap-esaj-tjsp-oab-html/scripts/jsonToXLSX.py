import json
import pandas as pd

def flattenCases(data):
    rows = []
    for case in data:
        baseInfo = {
            "numero": case["numero"],
            "advogado": case["advogado"],
            "tipo": case["tipo"],
            "assunto": case["assunto"],
            "recebidoEm": case["recebidoEm"],
            "vara": case["vara"],
            "pagina": case["pagina"],
        }
        
        if not case.get("processoFilhos"):
            rows.append(baseInfo)
        else:
            for child in case["processoFilhos"]:
                childInfo = {
                    "numeroFilho": child["numero"],
                    "tipoFilho": child["tipo"],
                    "assuntoFilho": child["assunto"],
                    "recebidoEmFilho": child["recebidoEm"],
                    "varaFilho": child["vara"],
                    "paginaFilho": child["pagina"],
                }
                rows.append({**baseInfo, **childInfo})
    
    return rows

def convertJsonToXlsx(jsonFile, xlsxFile):
    """
    Convert the extracted case data from JSON to XLSX format.
    """
    with open(jsonFile, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    structuredData = flattenCases(data)
    df = pd.DataFrame(structuredData)
    df.to_excel(xlsxFile, index=False)
    print(f"Conversion complete. Data saved to {xlsxFile}")

jsonFilename = "oab-366.427.json"  # Coloque o nome do arquivo .JSON
xlsxFilename = jsonFilename.replace(".json", ".xlsx")
convertJsonToXlsx(jsonFilename, xlsxFilename)
