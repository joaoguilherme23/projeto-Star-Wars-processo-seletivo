# Star Wars API (FastAPI + GCP Cloud Run)

API simples em **FastAPI** que consome a **SWAPI** (Star Wars API) e permite buscar informações de **personagens (people)**, **planetas (planets)** e **naves (starships)** usando filtro (`search`).

## Documentação (Swagger)
A documentação interativa da API está disponível em:

https://star-wars-274743836550.southamerica-east1.run.app/docs

## Base URL
https://star-wars-274743836550.southamerica-east1.run.app

## Autenticação (API Key)
As rotas são protegidas por **API Key** via header:

- Header: `X-API-Key: <seu_token>`

> O token é validado comparando com a variável de ambiente configurada no serviço (ex.: `API_KEY` ou `API_TOKEN`).

## Endpoint

### `GET /api/v1/busca`
Busca com filtro em `people`, `planets` ou `starships` usando o parâmetro `search` da SWAPI.

**Query params**
- `parametro_1` (string): `people` | `planets` | `starships`
- `parametro_2` (string): termo de busca (ex.: `luke`, `tatooine`, `falcon`)




**TOKEN PARA TESTE**
eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTc2OTc4NjQ1NywiaWF0IjoxNzY5Nzg2NDU3fQ.AoxBM6-1-_KSB8No4bc0idfSEKy4cT-njmyC01W09uM
