FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r docs/requirements.txt

CMD ["python", "scripts/main.py"]

# Para construir a imagem:
# docker build -t webScrapTJSP.
#
# Para rodar o container:
# docker run --rm -v "$(pwd)/data:/app/data" webscrapgabriel
