import os
import json
import requests
from bs4 import BeautifulSoup

def extractTotalPages(htmlContent):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    pageNumbers = [int(link.text.strip()) for link in soup.find_all('a', class_='paginacao') if link.text.strip().isdigit()]
    return max(pageNumbers) if pageNumbers else 1

def hasNextPage(htmlContent):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    return soup.find('a', class_='unj-pagination__next') is not None

def extractCaseInfo(htmlContent, session, baseUrl, cookies, pageNumber):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    cases = []

    for block in soup.find_all('div', class_='home__lista-de-processos'):
        caseNumberTag = block.find('a', class_='linkProcesso')
        lawyerTag = block.find('div', class_='unj-base-alt nomeParte')
        caseTypeTag = block.find('div', class_='classeProcesso')
        subjectTag = block.find('div', class_='assuntoPrincipalProcesso')
        receivedDateTag = block.find('div', class_='dataLocalDistribuicaoProcesso')

        if caseNumberTag and receivedDateTag:
            caseNumber = caseNumberTag.text.strip()
            processCode = caseNumberTag['href'].split('processo.codigo=')[1].split('&')[0]
            lawyer = lawyerTag.text.strip() if lawyerTag else "Não Informado"
            caseType = caseTypeTag.text.strip() if caseTypeTag else "Não Informado"
            subject = subjectTag.text.strip() if subjectTag else "Não Informado"
            receivedInfo = receivedDateTag.text.strip().split(" - ")
            receivedDate = receivedInfo[0]
            court = receivedInfo[1] if len(receivedInfo) > 1 else "Não Informado"

            caseInfo = {
                "numero": caseNumber,
                "advogado": lawyer,
                "tipo": caseType,
                "assunto": subject,
                "recebidoEm": receivedDate,
                "vara": court,
                "pagina": pageNumber,
                "processoFilhos": extractChildCases(session, baseUrl, cookies, processCode, court, pageNumber)
            }
            cases.append(caseInfo)

    return cases

def extractChildCases(session, baseUrl, cookies, processCode, court, pageNumber):
    childCases = []
    childParams = {
        "paginaConsulta": str(pageNumber),
        "cbPesquisa": "NUMOAB",
        "dadosConsulta.valorConsulta": numberOAB,
        "cdForo": "-1",
        "cdProcessoMaster": processCode,
        "cdForoProcesso": court,
        "conversationId": ""
    }
    response = session.get(f"{baseUrl}/cpopg/obterProcessosFilhos.do", params=childParams, cookies=cookies)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for block in soup.find_all('div', class_='home__lista-de-processos'):
            childNumberTag = block.find('a', class_='linkProcesso')
            childCaseTypeTag = block.find('div', class_='classeProcesso')
            childSubjectTag = block.find('div', class_='assuntoPrincipalProcesso')
            childReceivedDateTag = block.find('div', class_='dataLocalDistribuicaoProcesso')

            if childNumberTag and childReceivedDateTag:
                childNumber = childNumberTag.text.strip()
                childCaseType = childCaseTypeTag.text.strip() if childCaseTypeTag else "Não Informado"
                childSubject = childSubjectTag.text.strip() if childSubjectTag else "Não Informado"
                childReceivedInfo = childReceivedDateTag.text.strip().split(" - ")
                childReceivedDate = childReceivedInfo[0]
                childCourt = childReceivedInfo[1] if len(childReceivedInfo) > 1 else "Não Informado"

                childCaseInfo = {
                    "numero": childNumber,
                    "tipo": childCaseType,
                    "assunto": childSubject,
                    "recebidoEm": childReceivedDate,
                    "vara": childCourt,
                    "pagina": pageNumber
                }
                childCases.append(childCaseInfo)

    return childCases

def saveToJson(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def fetchPage(session, url, params, cookies):
    response = session.get(url, params=params, cookies=cookies)
    print(f"Buscando página: {response.url} - Status Code: {response.status_code}\n")
    return response.text

def main():
    global numberOAB
    print("\n=== Consulta de Processos no TJSP ===\n")
    
    numberOAB = input("Digite o número da OAB (apenas números): ").strip()
    print("\nIniciando busca de processos...\n")

    baseUrl = "https://esaj.tjsp.jus.br"
    searchEndpoint = "/cpopg/search.do"
    paginationEndpoint = "/cpopg/trocarPagina.do"
    
    searchParams = {
        "conversationId": "",
        "cbPesquisa": "NUMOAB",
        "dadosConsulta.valorConsulta": numberOAB,
        "cdForo": "-1"
    }

    session = requests.Session()
    searchHtml = fetchPage(session, f"{baseUrl}{searchEndpoint}", searchParams, {})
    
    totalPages = extractTotalPages(searchHtml)
    print(f"Total de páginas encontradas: {totalPages}\n")

    allCases = extractCaseInfo(searchHtml, session, baseUrl, session.cookies.get_dict(), 1)
    cookies = session.cookies.get_dict()

    page = 2
    while True:
        print(f"\nBuscando página {page}...\n")
        
        paginationParams = {
            "paginaConsulta": str(page),
            "conversationId": "",
            "cbPesquisa": "NUMOAB",
            "dadosConsulta.valorConsulta": numberOAB,
            "cdForo": "-1"
        }

        pageHtml = fetchPage(session, f"{baseUrl}{paginationEndpoint}", paginationParams, cookies)
        cases = extractCaseInfo(pageHtml, session, baseUrl, cookies, page)
        allCases.extend(cases)

        if not hasNextPage(pageHtml):
            break

        page += 1

    outputFilename = f"data/json/oab-{numberOAB}.json"
    saveToJson(allCases, outputFilename)

    print(f"\nExtração concluída! Arquivo salvo em: {outputFilename}\n")

if __name__ == "__main__":
    main()
