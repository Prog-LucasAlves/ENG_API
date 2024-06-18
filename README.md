# Projeto Criando uma API do Zero

## ![API](https://cdn-icons-png.flaticon.com/24/439/439164.png) O que significa API?

- API significa Application Programming Interface (Interface de Programação de Aplicação). No contexto de APIs, a palavra Aplicação refere-se a qualquer software com uma função distinta. A interface pode ser pensada como um contrato de serviço entre duas aplicações. Esse contrato define como as duas se comunicam usando solicitações e respostas. A documentação de suas respectivas APIs contém informações sobre como os desenvolvedores devem estruturar essas solicitações e respostas.

## ![API REST](https://cdn-icons-png.flaticon.com/24/9610/9610562.png) O que são APIs REST?

- REST significa Transferência Representacional de Estado. REST define um conjunto de funções como GET, PUT, DELETE e assim por diante, que os clientes podem usar para acessar os dados do servidor. Clientes e servidores trocam dados usando HTTP.

A principal característica da API REST é a ausência de estado. A ausência de estado significa que os servidores não salvam dados do cliente entre as solicitações. As solicitações do cliente ao servidor são semelhantes aos URLs que você digita no navegador para visitar um site. A resposta do servidor corresponde a dados simples, sem a renderização gráfica típica de uma página da Web.

##

- Para realizar esse projeto utilizarei a biblioteca [FastAPI](https://fastapi.tiangolo.com/).

- Como exemplo será criando um api de um modelo de machine learnig(Com Deploy).

> [!NOTE]
> Estrutura do Projeto

```bash
├───.github
│      └───workflows         # CI
├───SRC
     ├───api                 # Pasta dos arquivos para criar a API
     ├───frontend            # Pasta dos arquivos para criar o dashboard
     ├───model               # Pasta dos arquivos para cirar o modelo
├───.gitignore               # Arquivo com pastas/arquivos/extensões ignorados pelo git
├───.pre-commit-config.yaml  # Arquivo com as configurações a serem utilizadas no git commit
├───.python-version          # Versão utilizada no projeto
```

##

- Link para API -> [aqui](https://eng-api-e8wg.onrender.com/docs) | :construction:

## ![CRED](https://cdn-icons-png.flaticon.com/24/7178/7178894.png) Créditos pelo aprendizado e inspiração para criação de simplório projeto

- [x] Jornada de Dados | Luciano Galvão [youtube](https://www.youtube.com/@lvgalvaofilho).
- [x] Curso -> FastAPI do Zero [link](https://fastapidozero.dunossauro.com/) | Dunossauro [youtube](https://www.youtube.com/@Dunossauro).
