# Projeto Criando uma API do Zero

## ![API](https://cdn-icons-png.flaticon.com/24/439/439164.png) O que significa API?

- API significa Application Programming Interface (Interface de Programação de Aplicação). No contexto de APIs, a palavra Aplicação refere-se a qualquer software com uma função distinta. A interface pode ser pensada como um contrato de serviço entre duas aplicações. Esse contrato define como as duas se comunicam usando solicitações e respostas. A documentação de suas respectivas APIs contém informações sobre como os desenvolvedores devem estruturar essas solicitações e respostas.

## ![API REST](https://cdn-icons-png.flaticon.com/24/9610/9610562.png) O que são APIs REST?

- Uma API REST (Representational State Transfer) é um estilo de arquitetura para a criação de serviços web que permite a comunicação entre sistemas via HTTP. Ela se baseia em princípios simples e padrões que facilitam o desenvolvimento, a escalabilidade e a manutenção dos serviços. Aqui estão alguns dos principais conceitos e características de uma API REST:

1. **Recursos (Resources)**: Tudo em uma API REST é considerado um recurso, que é identificado por um URL único. Por exemplo, em uma API de gerenciamento de usuários, um recurso pode ser um usuário específico identificado por /usuarios/1.

2. **Verbos HTTP**: A interação com os recursos é feita usando verbos HTTP, como.
- GET: Para recuperar informações de um recurso.
- POST: Para criar um novo recurso.
- PUT: Para atualizar um recurso existente.
- DELETE: Para deletar um recurso.
- PATCH: Para atualizar parcialmente um recurso.

3. **Representações (Representations)**: Um recurso pode ter várias representações, como JSON, XML, HTML, entre outros. JSON é o formato mais comum usado em APIs REST.

4. **Stateless**: Cada requisição de um cliente para o servidor deve conter todas as informações necessárias para entender e processar o pedido. O servidor não deve armazenar nenhum estado sobre o cliente entre as requisições.

##

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

##

- Link API -> [aqui](https://eng-api-e8wg.onrender.com/docs) | :construction:
- Link Deploy -> [aqui](https://deploy-api-kvp5.onrender.com) | :construction:

## ![CRED](https://cdn-icons-png.flaticon.com/24/7178/7178894.png) Créditos pelo aprendizado e inspiração para criação desse projeto

- [x] Jornada de Dados | Luciano Galvão [youtube](https://www.youtube.com/@lvgalvaofilho).
- [x] Curso -> FastAPI do Zero [link](https://fastapidozero.dunossauro.com/) | Dunossauro [youtube](https://www.youtube.com/@Dunossauro).
