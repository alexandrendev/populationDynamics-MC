# Usando uma imagem base do Python
FROM python:3.12.3-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o código-fonte para dentro do container
COPY ./src/rafikov /app

# Copiando o arquivo requirements.txt
COPY requirements.txt /app/

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Definindo o comando para rodar a aplicação
CMD ["python3", "main.py"]

