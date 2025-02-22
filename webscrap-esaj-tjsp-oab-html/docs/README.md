Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # WebScrapGabriel  Este projeto realiza **web scraping** para extrair dados de processos judiciais e converte os resultados de **JSON** para **XLSX**.  ## Instalação  1. Clone o repositório:     ```sh     git clone https://github.com/seu-usuario/WebScrapGabriel.git     cd WebScrapGabriel   `

1.  shCopiarEditarpython -m venv venvsource venv/bin/activate # Linux/macOSvenv\\Scripts\\activate # Windows
    
2.  shCopiarEditarpip install -r docs/requirements.txt
    

Uso
---

Para executar o scraping e a conversão:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   shCopiarEditarpython main.py   `

Os arquivos JSON gerados ficarão em data/json/ e os XLSX em data/xlsx/.

Estrutura do Projeto
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopiarEditar📦 WebScrapGabriel   ┣ 📂 data         # Armazena os arquivos JSON e XLSX   ┣ 📂 docs         # Documentação e dependências   ┣ 📂 logs         # Logs de execução   ┣ 📂 scripts      # Código principal   ┣ 🐍 main.py      # Arquivo principal   ┣ 🐳 Dockerfile   # Configuração do Docker   ┣ 📄 README.md    # Documentação   ┗ 📄 .gitignore   # Ignora arquivos desnecessários no Git   `

Docker
------

Para rodar o projeto via Docker:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   shCopiarEditardocker build -t webscrapgabriel .  docker run --rm -v "$(pwd)/data:/app/data" webscrapgabriel   `

Licença
-------

Este projeto está sob a **Licença MIT**.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   yamlCopiarEditar  ---  Agora é só **copiar e colar** no seu `README.md`, sem fragmentação. Pronto!   ``
