"""
Módulo de API FastAPI para geração de texto utilizando o modelo GPT-2 da Hugging Face.
Desenvolvido para atender aos requisitos de testes práticos de desenvolvimento de aplicações com LLMs.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Inicializo a aplicação FastAPI definindo metadados básicos
app = FastAPI(
    title="API de Geração de Texto com GPT-2",
    description="Serviço FastAPI para continuação de texto utilizando transformers da Hugging Face.",
    version="1.0.0"
)

# Carrego o pipeline de geração de texto com o modelo GPT-2 pré-treinado
# Faço o carregamento na inicialização para evitar latência excessiva a cada requisição
try:
    gerador_texto = pipeline("text-generation", model="gpt2")
except Exception as erro:
    raise RuntimeError(f"Erro ao carregar o modelo GPT-2: {str(erro)}")

# Defino o esquema de dados de entrada utilizando Pydantic para validação do JSON
class RequisicaoTexto(BaseModel):
    prompt: str
    max_length: int = 50  # Comprimento máximo padrão para a geração
    num_return_sequences: int = 1

@app.post("/gerar-texto", summary="Gera continuação de texto a partir de um prompt")
def gerar_texto(dados: RequisicaoTexto):
    """
    Recebo uma frase de entrada via JSON, executo o pipeline do GPT-2
    e retorno o texto gerado formatado em JSON.
    """
    try:
        # Valido se a entrada não está vazia
        if not dados.prompt.strip():
            raise HTTPException(status_code=400, detail="O prompt de entrada não pode estar vazio.")
        
        # Executo a geração de texto utilizando o modelo carregado
        resultados = gerador_texto(
            dados.prompt,
            max_length=dados.max_length,
            num_return_sequences=dados.num_return_sequences,
            no_repeat_ngram_size=2,
            truncation=True
        )
        
        # Extraio o texto gerado da estrutura de retorno do pipeline
        texto_gerado = resultados[0]["generated_text"]
        
        # Retorno o resultado estruturado
        return {
            "prompt_original": dados.prompt,
            "texto_gerado": texto_gerado
        }
        
    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro interno no processamento: {str(erro)}")

