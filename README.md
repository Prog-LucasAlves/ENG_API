# Projeto Criando uma API do Zero

## ![API](https://cdn-icons-png.flaticon.com/24/439/439164.png) O que significa API?

- API significa Application Programming Interface (Interface de Programação de Aplicação). No contexto de APIs, a palavra Aplicação refere-se a qualquer software com uma função distinta. A interface pode ser pensada como um contrato de serviço entre duas aplicações. Esse contrato define como as duas se comunicam usando solicitações e respostas. A documentação de suas respectivas APIs contém informações sobre como os desenvolvedores devem estruturar essas solicitações e respostas.

## ![API REST](https://cdn-icons-png.flaticon.com/24/9610/9610562.png) O que são APIs REST?

- Uma **API REST** (Representational State Transfer) é um estilo de arquitetura para a criação de serviços web que permite a comunicação entre sistemas via HTTP. Ela se baseia em princípios simples e padrões que facilitam o desenvolvimento, a escalabilidade e a manutenção dos serviços. Aqui estão alguns dos principais conceitos e características de uma API REST:

1. **Recursos (Resources)**: Tudo em uma API REST é considerado um recurso, que é identificado por um URL único. Por exemplo, em uma API de gerenciamento de usuários, um recurso pode ser um usuário específico identificado por /usuarios/1.

2. **Verbos HTTP**: A interação com os recursos é feita usando verbos HTTP, como:
- GET: Para recuperar informações de um recurso.
- POST: Para criar um novo recurso.
- PUT: Para atualizar um recurso existente.
- DELETE: Para deletar um recurso.
- PATCH: Para atualizar parcialmente um recurso.

3. **Representações (Representations)**: Um recurso pode ter várias representações, como JSON, XML, HTML, entre outros. JSON é o formato mais comum usado em APIs REST.

4. **Stateless**: Cada requisição de um cliente para o servidor deve conter todas as informações necessárias para entender e processar o pedido. O servidor não deve armazenar nenhum estado sobre o cliente entre as requisições.

5. **Cacheable**: As respostas devem informar se podem ser armazenadas em cache para otimizar o desempenho.

6. **Uniform Interface**: Um conjunto uniforme de regras e convenções que permite a interação padronizada com a API, facilitando a compreensão e o uso da API por diferentes clientes.

7. **Cliente-Servidor**: A arquitetura REST separa as responsabilidades entre o cliente e o servidor, permitindo que eles evoluam independentemente.

- __Exemplo de Endpoints em uma API REST__

1. Vamos supor que estamos criando uma API para gerenciar uma lista de tarefas:

- [x] GET /tarefas: Retorna uma lista de todas as tarefas.
- [x] GET /tarefas/{id}: Retorna uma tarefa específica.
- [x] POST /tarefas: Cria uma nova tarefa.
- [x] PUT /tarefas/{id}: Atualiza uma tarefa específica.
- [x] DELETE /tarefas/{id}: Deleta uma tarefa específica.

Ao seguir esses princípios e práticas, as APIs REST se tornam fáceis de usar e integráveis com diversas plataformas e linguagens de programação.

![IMAGE](https://github.com/Prog-LucasAlves/ENG_API/blob/main/SRC/image/API_REST.png)

## ![INFO](https://cdn-icons-png.flaticon.com/24/7627/7627546.png) Informações do Projeto

- Para realizar esse projeto utilizarei a biblioteca [FastAPI](https://fastapi.tiangolo.com/).

> [!TIP]
> Como exemplo será criando um api de um modelo de machine learning para realizar predição do aluguel de casas/apartamentos(Com Deploy).

> [!NOTE]
> Estrutura do Projeto

```bash
├───.github
│      └───workflows         # CI
├───SRC
     ├───api                 # Pasta dos arquivos para criar a API
     ├───frontend            # Pasta dos arquivos para criar o dashboard
     ├───model               # Pasta dos arquivos para cirar o modelo
     ├───tests               # Pasta dos arquivos de testes
├───.gitignore               # Arquivo com pastas/arquivos/extensões ignorados pelo git
├───.pre-commit-config.yaml  # Arquivo com as configurações a serem utilizadas no git commit
├───.python-version          # Versão do Python utilizada no projeto
├───.pyproject.toml          # Bibliotecas Python utilizadas no projeto
├───README.md                # Documentação do projeto
├───requirements.txt         # Bibliotecas Python utilizadas no CI -> workflows
```

## ![PROJETO](https://cdn-icons-png.flaticon.com/24/2721/2721286.png) Como Estruturar o Projeto

### Python

- Versão do python utilizada: **3.12.2** | atraves do *pyenv*
- Arguivo .python-version
Ref.: [pyenv](https://github.com/pyenv/pyenv)

### Criando o diretório para o projeto

```bash
mkdir ENG_API
cd ENG_API
```

### Clonando o repositório

```bash
git clone https://github.com/Prog-LucasAlves/ENG_API
```

## Criando ambiente virtual(poetry)

Ref.: [poetry](https://python-poetry.org/)

```bash
poetry shell
```

## Instalando as dependências do projeto

```bash
poetry install
```

## ![LINK](https://cdn-icons-png.flaticon.com/24/2696/2696513.png) Links

- Link API -> [aqui](https://eng-api-e8wg.onrender.com/docs) | :construction:
- Link Deploy -> [aqui](https://deploy-api-kvp5.onrender.com) | :construction:

## ![CRED](https://cdn-icons-png.flaticon.com/24/7178/7178894.png) Créditos pelo Aprendizado e Inspiração para Criação Desse Projeto

- [x] Jornada de Dados | Luciano Galvão [youtube](https://www.youtube.com/@lvgalvaofilho).
- [x] Curso -> FastAPI do Zero [link](https://fastapidozero.dunossauro.com/) | Dunossauro [youtube](https://www.youtube.com/@Dunossauro).
