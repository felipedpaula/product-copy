# Criação de Copy de Marketing com GPT-4

Este programa Python utiliza a API da OpenAI, especificamente o modelo GPT-3.5-turbo, para criar um "copy" de marketing com base nas informações fornecidas pelo usuário.

## Instalação e Configuração
### 1. Dependências:

1. openai: Esta biblioteca permite a comunicação direta com os modelos da OpenAI.
2. os e dotenv: Utilizadas para carregar variáveis de ambiente, especialmente a chave de API da OpenAI.
Para instalar as dependências, execute:
```bash
pip install openai python-dotenv
```

### 2. Configuração da chave API:
Crie um arquivo .env na mesma pasta do seu script. Adicione sua chave de API da OpenAI no arquivo .env da seguinte maneira:
```bash
OPENAI_API_KEY=sua_chave_aqui
```

## Como usar
1. Execute o programa.
2. Insira o Nome do produto quando solicitado.
3. Forneça uma Visão geral do Produto descrevendo suas características, separadas por ponto e vírgula.
4. Adicione quaisquer Observações adicionais sobre o produto.

O programa irá processar as informações fornecidas e, com base nas instruções fornecidas para o modelo, retornará um "copy" de marketing otimizado para o produto inserido.

## Detalhes do Código
- `get_completion` Function: Esta função leva um "prompt" e faz uma requisição para o modelo GPT-3.5-turbo da OpenAI. Retorna a resposta gerada pelo modelo.
- **Instruções para o Modelo:** As instruções para o modelo são projetadas para orientá-lo sobre como criar um copy de marketing eficaz. Isso inclui dicas sobre clareza na escrita, benefícios do produto, linguagem persuasiva, relevância para o público-alvo e vários outros pontos.
- **Entrada do Usuário:** O programa solicita ao usuário detalhes sobre o produto, como o nome, visão geral e observações. Esta entrada é então transmitida ao modelo para criar o copy de marketing.

## Conclusão
Este programa é uma ferramenta poderosa para quem precisa de assistência na criação de textos de marketing. Utilizando a capacidade de compreensão de linguagem natural do modelo GPT-3.5-turbo, ele pode gerar "copies" de marketing eficazes e personalizados com base nas informações do produto fornecidas pelo usuário.


