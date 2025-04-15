# API de Receitas

Esta API permite criar, atualizar, listar, obter e deletar **ingredientes** e **receitas**. Além disso, a API permite associar **ingredientes a receitas** e realiza a validação para garantir que ingredientes existentes sejam usados corretamente.

## 📦 Tecnologias Utilizadas

- **Flask**: Framework web para criar a API.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interação com o banco de dados.
- **SQLite**: Banco de dados local (sem necessidade de configuração de servidor).
- **Postman / cURL**: Para testar os endpoints.

## 🚀 Acessando a API

A API está hospedada em uma máquina na nuvem e pode ser acessada pelo seguinte **IP**:

**Endereço da API**: `http://68.183.113.155:5000`

## 📋 Estrutura do Projeto

- **`app.py`**: Inicializa a aplicação Flask, configura o banco de dados e as rotas.
- **`config.py`**: Contém as configurações do banco de dados.
- **`models.py`**: Define os modelos de dados (ingredientes e receitas).
- **`api.py`**: Define as rotas da API, como criação, leitura, atualização e exclusão de receitas e ingredientes.

## 🚀 Instruções de Instalação

### Passo 1: Clonar o Repositório

git clone https://github.com/TagFernandes/API-receita.git
cd API-receita


## Passo 2: Criar um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências:

`python -m venv venv` 

Ative o ambiente virtual:

-   No **Windows**:
    
    `venv\Scripts\activate` 
    
-   No **Linux/macOS**:
    
    `source venv/bin/activate` 
    

## Passo 3: Instalar Dependências

`pip install -r requirements.txt` 

## Passo 4: Rodar o Servidor

Para rodar o servidor Flask:

`python app.py` 

A API estará disponível em:  
👉 **`http://68.183.113.155:5000`**

## 🌍 Endpoints da API

## **1. Criar Ingrediente**

#### Método: `POST`

**Endpoint**: `/ingredientes`

-   **Body** (exemplo de dados):

`{  "nome":  "Farinha de Trigo",  "unidade":  "gramas"  }` 

-   **Resposta**:

`{  "id":  1  }` 

## **2. Listar Ingredientes**

#### Método: `GET`

**Endpoint**: `/ingredientes`

-   **Query String (opcional)**: `?nome=<nome_do_ingrediente>`
    
-   **Exemplo**: `/ingredientes?nome=farinha`
    
-   **Resposta** (quando busca por nome):

`[  {  "id":  1,  "nome":  "Farinha de Trigo",  "unidade":  "gramas"  }  ]` 

## **3. Obter Ingrediente Específico**

#### Método: `GET`

**Endpoint**: `/ingredientes/<id>`

-   **Exemplo**: `/ingredientes/1`
    
-   **Resposta**:

`{  "id":  1,  "nome":  "Farinha de Trigo",  "unidade":  "gramas"  }` 

## **4. Atualizar Ingrediente**

#### Método: `PUT`

**Endpoint**: `/ingredientes/<id>`

-   **Body** (exemplo de dados):

`{  "nome":  "Açúcar",  "unidade":  "gramas"  }` 

-   **Resposta**:

`{  "mensagem":  "Ingrediente atualizado"  }` 

## **5. Deletar Ingrediente**

#### Método: `DELETE`

**Endpoint**: `/ingredientes/<id>`

-   **Exemplo**: `/ingredientes/1`
    
-   **Resposta (quando ingrediente é deletado com sucesso)**:

`{  "mensagem":  "Ingrediente deletado com sucesso."  }` 

-   **Resposta (quando o ingrediente não pode ser deletado devido a associações)**:


`{  "erro":  "Ingredientes não cadastrados",  "ingredientes_nao_encontrados":  [2,  4]  }` 

## **6. Criar Receita**

#### Método: `POST`

**Endpoint**: `/receitas`

-   **Body** (exemplo de dados):

`{  "nome":  "Bolo de Chocolate",  "modo_preparo":  "Misture todos os ingredientes, coloque em uma forma untada e leve ao forno por 40 minutos.",  "ingredientes":  [  {  "id":  1,  "quantidade":  200  },  // exemplo: 200 gramas de farinha  {  "id":  2,  "quantidade":  100  },  // exemplo: 100 gramas de açúcar  {  "id":  3,  "quantidade":  2  }  // exemplo: 2 ovos  ]  }` 

-   **Resposta**:

`{  "id":  1  }` 

## **7. Listar Receitas**

#### Método: `GET`

**Endpoint**: `/receitas`

-   **Query String (opcional)**: `?nome=<nome_da_receita>`
    
-   **Exemplo**: `/receitas?nome=bolo`
    
-   **Resposta**:

`[  {  "id":  1,  "nome":  "Bolo de Chocolate",  "modo_preparo":  "Misture todos os ingredientes...",  "ingredientes":  [  {"ingrediente_id":  1,  "quantidade":  200},  {"ingrediente_id":  2,  "quantidade":  100}  ]  }  ]` 

## **8. Obter Receita Específica**

#### Método: `GET`

**Endpoint**: `/receitas/<id>`

-   **Exemplo**: `/receitas/1`
    
-   **Resposta**:
    

`{  "id":  1,  "nome":  "Bolo de Chocolate",  "modo_preparo":  "Misture todos os ingredientes...",  "ingredientes":  [  {"ingrediente_id":  1,  "quantidade":  200},  {"ingrediente_id":  2,  "quantidade":  100}  ]  }` 

## **9. Atualizar Receita**

#### Método: `PUT`

**Endpoint**: `/receitas/<id>`

-   **Body** (exemplo de dados):

`{  "nome":  "Bolo de Laranja",  "modo_preparo":  "Misture os ingredientes e leve ao forno por 35 minutos.",  "ingredientes":  [  {  "id":  1,  "quantidade":  150  },  {  "id":  2,  "quantidade":  100  }  ]  }` 

-   **Resposta**:

`{  "mensagem":  "Receita atualizada com sucesso"  }` 

## **10. Deletar Receita**

#### Método: `DELETE`

**Endpoint**: `/receitas/<id>`

-   **Exemplo**: `/receitas/1`
    
-   **Resposta**:

`{  "mensagem":  "Receita deletada com sucesso."  }` 

----------

## 🧑‍💻 **Como Rodar a API**

1.  **Clone o repositório**:
    
    `git clone https://github.com/TagFernandes/API-receita.git cd API-receita` 
    
2.  **Crie e ative um ambiente virtual**:
    
    `python -m venv venv source venv/bin/activate # Linux/macOS venv\Scripts\activate # Windows` 
    
3.  **Instale as dependências**:
    
    `pip install -r requirements.txt` 
    
4.  **Rodar o servidor**:
    
    `python app.py` 
    

A API estará disponível em `http://68.183.113.155:5000`.

----------

## 💡 **Considerações Finais**

-   **SQLite** é usado como banco de dados para este projeto, então o banco será armazenado no arquivo `db.sqlite3`.
    
-   Todos os endpoints `GET` que podem buscar por **nome** utilizam a query string `?nome=<nome>`.
    
-   Para interagir com a API, você pode usar ferramentas como **Postman** ou **cURL**.