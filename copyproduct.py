import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key  = os.getenv('OPENAI_API_KEY')

# Função da requisição para o modelo da OpenAI
def get_completion(prompt, model="gpt-3.5-turbo"): 
    messages = msg
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

# Dados do texto a ser corrigido
nome_produto = str(input("Nome do produto: "))
overview = str(input("Visão geral do Produto \
(caracteŕisticas separadas por ;): "))
observacoes = str(input("Observações: "))

# Prompt de instrução para criação do COPY
prompt_system = f"""
    Sua tarefa é criar um copy de marketing de um produto \
    qualquer. Será passado pelo usuário o NOME do produto, \
    uma VISÃO GERAL do produto que vai conter todas as \
    características do produto separadas por ponto e vírgula. \
    Antes de criar o copy, veja todas as características \
    necessárias para a criação e certifique-se de transmitir \
    o máximo de todas as caracterísitcas:
    - Clareza na escrita, sem termos de difícil compreensão;
    - Benefícios (Como o produto pode melhorar a vida do consumidor?) \
    - Linguagem persuasiva;
    - Avaliações do produto para passar credibilidade; \
    - Relevante para o público alvo;
    - Original. É importante que o copy seja único e se destaque da \
    concorrência;
    - Conexão emocional com o público-alvo;
    - Criar curiosidade no público-alvo;
    - Valor vs Preço;
    - Segurança da compra.
"""

# Prompt do Usuário
prompt_user = f"""
    Nome do produto: {nome_produto}
    Visão geral: {overview}
    Observações: {observacoes}
"""

# Estrutura da mensagem para o modelo
msg = [
    {   
        "role": "system",
        "content": prompt_system
    },
    {
        "role": "user",
        "content": prompt_user
    }
]

# Envia a requisição e guarda em 'response'
response = get_completion(msg)

# Etrega a resposta
print(response)
