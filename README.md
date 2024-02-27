
# Chatbot de uma base de dados

Este projeto se concentra na criação de um Chatbot com base em um Catálogo de Dados ou Bases de dados. 

Seu propósito será responder a perguntas e consultas dos usuários relacionadas aos dados contidos no banco, simplificando e acelerando o processo de busca de informações, eliminando a necessidade de realizar pesquisas demoradas. 


## Requisitos:
1. Ter alguma dessas versões de **Python** instaladas: versions: `3.7`, `3.8`,` 3.9` and `3.10.`

&nbsp;

OBS: `Python 3.10` é apenas aceito para versões `3.4.x` e acima, além disso, a instalação do Rasa pela Apple Silicon com Python `3.10` não é aceito em `3.4` mas poderá ser utilizado começando na versão `3.5.x`.

2. Ter WSL 2 instalada


## Como rodar o código na sua máquina:
Instalar a última versão do pip:
```
sudo apt install python3-venv
```
Criar um ambiente virtual na sua máquina:
```
python3 -m venv ./venv
```
Ativar o ambiente virtual:
```
source ./venv/bin/activate
```
Instalar Rasa Open Source:
```
python -m pip install --upgrade pip rasa
 ```
Iniciar Rasa:
```
rasa init
```
 ```
Para conversar com o chatbot, envie o seguinte comando no terminal:
```
rasa shell
```
Abra um terminal simultâneo e inicie o servidor de ações:
```
rasa run actions
```

No terminal do Rasa Shell vai ser possível interagir com o chatbot e perguntar sobre o banco de dados.
