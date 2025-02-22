import os
import json
import requests
from bs4 import BeautifulSoup

def extractTotalPages(htmlContent):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    pageNumbers = []
    
    # Encontrar os números de página
    paginationLinks = soup.find_all('a', class_='paginacao')
    for link in paginationLinks:
        if link.text.strip().isdigit():
            pageNumbers.append(int(link.text.strip()))
    
    maxPage = max(pageNumbers) if pageNumbers else 1
    
    return maxPage

def hasNextPage(htmlContent):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    nextButton = soup.find('a', class_='unj-pagination__next')
    return nextButton is not None

def extractCaseInfo(htmlContent, session, baseUrl, cookies, pageNumber):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    cases = []
    
    caseBlocks = soup.find_all('div', class_='home__lista-de-processos')
    
    for block in caseBlocks:
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
        "dadosConsulta.valorConsulta": "71.812",
        "cdForo": "-1",
        "cdProcessoMaster": processCode,
        "cdForoProcesso": court,
        "conversationId": ""
    }
    response = session.get(f"{baseUrl}/cpopg/obterProcessosFilhos.do", params=childParams, cookies=cookies)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        childBlocks = soup.find_all('div', class_='home__lista-de-processos')
        for block in childBlocks:
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
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def fetchPage(session, url, params, cookies):
    response = session.get(url, params=params, cookies=cookies)
    print(f"Fetching {response.url} - Status Code: {response.status_code}")
    return response.text

def main():
    baseUrl = "https://esaj.tjsp.jus.br"
    searchEndpoint = "/cpopg/search.do"
    paginationEndpoint = "/cpopg/trocarPagina.do"
    searchParams = {
        "conversationId": "",
        "cbPesquisa": "NUMOAB",
        "dadosConsulta.valorConsulta": "71.812",  # Campo variável para trocar o número da OAB
        "cdForo": "-1"
    }
    
    session = requests.Session()
    
    # Realizar a pesquisa inicial
    searchHtml = fetchPage(session, f"{baseUrl}{searchEndpoint}", searchParams, {})
    totalPages = extractTotalPages(searchHtml)
    print(f"Total pages found initially: {totalPages}")
    allCases = extractCaseInfo(searchHtml, session, baseUrl, session.cookies.get_dict(), 1)
    cookies = session.cookies.get_dict()
    
    # Iterar até que não haja mais a opção de próxima página
    page = 2
    while True:
        print(f"Fetching page {page}")
        paginationParams = {
            "paginaConsulta": str(page),
            "conversationId": "",
            "cbPesquisa": "NUMOAB",
            "dadosConsulta.valorConsulta": "71.812",  # Campo variável para trocar o número da OAB
            "cdForo": "-1"
        }
        
        pageHtml = fetchPage(session, f"{baseUrl}{paginationEndpoint}", paginationParams, cookies)
        cases = extractCaseInfo(pageHtml, session, baseUrl, cookies, page)
        allCases.extend(cases)
        
        if not hasNextPage(pageHtml):
            break
        
        page += 1
    
    oabNumber = searchParams["dadosConsulta.valorConsulta"]
    outputFilename = f"oab-{oabNumber}.json"
    
    saveToJson(allCases, outputFilename)
    print(f"Extraction complete. Data saved to {outputFilename}")

if __name__ == "__main__":
    main()
