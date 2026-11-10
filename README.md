# FastAPI - Parte 1: Questão 1

Aplicação desenvolvida em **FastAPI** estruturada para fins acadêmicos, integrando endpoints de alta performance com validação de dados via Pydantic.

## Tecnologias Utilizadas
* Python 3.10+
* FastAPI
* Uvicorn

## Como Executar

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows (PowerShell):
   .\venv\Scripts\Activate

    Instale as dependências:
    Bash

    pip install fastapi uvicorn

    Execute o servidor de desenvolvimento:
    Bash

    uvicorn main:app --reload

    Acesse a documentação interativa (Swagger UI) no navegador:

        http://127.0.0.1:8000/docs
