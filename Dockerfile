# Imagem base oficial do Python
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código-fonte da aplicação
COPY . .

# Expõe a porta 5000 utilizada pelo Flask
EXPOSE 5000

# Executa a aplicação web da calculadora
CMD ["python", "app.py"]
