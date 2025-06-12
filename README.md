<div align="center">

  <h1>Pixel Lab</h1>

  <p>
    Processamento de Imagens
  </p>

<p>
  <a href="https://github.com/feliperodighero/hotel-reservations/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/feliperodighero/hotel-reservations" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/feliperodighero/hotel-reservations" alt="last update" />
  </a>
  <a href="https://github.com/feliperodighero/hotel-reservations/network/members">
    <img src="https://img.shields.io/github/forks/feliperodighero/hotel-reservations" alt="forks" />
  </a>
  <a href="https://github.com/feliperodighero/hotel-reservations/stargazers">
    <img src="https://img.shields.io/github/stars/feliperodighero/hotel-reservations" alt="stars" />
  </a>
  <a href="https://github.com/feliperodighero/hotel-reservations/issues/">
    <img src="https://img.shields.io/github/issues/feliperodighero/hotel-reservations" alt="open issues" />
  </a>
  <a href="https://github.com/feliperodighero/hotel-reservations/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/feliperodighero/hotel-reservations.svg" alt="license" />
  </a>
</p>
</div>
<br />

## ✨ Sobre o Projeto

Plataforma interativa desenvolvida com Python e Streamlit para aplicar filtros e transformações em imagens, implementados do zero, sem uso de bibliotecas de alto nível como OpenCV. Todos os algoritmos foram criados manualmente, com base nas fórmulas matemáticas que regem cada filtro, permitindo uma compreensão profunda dos processos de manipulação de imagens.

## 🛠 Tecnologias Utilizadas

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=for-the-badge" alt="Streamlit" />
</p>

![Captura de tela](https://github.com/user-attachments/assets/32447927-0201-4088-9339-1fd3b45e6a54)

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.12 >
- UV

### Clonar o Projeto

`git clone https://github.com/feliperodighero/pixel-lab.git`

### Instalar Depedências

````
pip install uv  # Instalar o UV (gerenciador de pacotes)
uv venv     # Cria o ambiente virtual
uv sync     # Instala as dependências listadas no pyproject.toml
uv run streamlit run src/main.py    # Roda o projeto
````

## Estrutura do Projeto

```
├── README.md          <- Resumo sobre o projeto
│
├── .gitignore         <- Lista de arquivos não enviados ao repositório
|
├── pyproject.toml   <- Lista de dependências do projeto
│
├── uv.lock   <- Histórico das dependências do projeto
|
└── src   <- Código principal do projeto
    │
    ├── components
    │   ├── __init__.py              <- Arquivo para encurtar os imports
    │   ├── image_download.py        <- Lógica para download da imagem final
    │   └── image_display.py         <- Display das duas imagens de entrada
    |   └── images_upload.py         <- Lógica para upload das duas imagens de entrada
    |   └── operations_apply.py      <- Código para aplicar e manipular as operações
    |   └── operations_select.py     <- Lógica para gerenciar a seleção dos filtros
    |
    ├── operations
    │   ├── components
    │       ├── arithmetic           <- Filtros aritméticos
    │       ├── enchance             <- Filtros de realce
    │       └── invert               <- Lógica para inverter a posição da imagem
    |       └── logical              <- Filtros de operações lógicas (AND, NOT, etc)
    |       └── morphological        <- Filtros morfológicos
    |       └── spacial_domanin      <- Filtros de dominío espacial
    │
    ├── utils
    │   ├── histogram.py <- Lógica para plotar o gráfico do histograma
    │
    └── main.py     <- Código principal, que consome toda a lógica
```
