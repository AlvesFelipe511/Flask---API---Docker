# 📦 API Flask com PostgreSQL e Docker

Este projeto é uma API RESTful simples desenvolvida com **Flask** (Python), utilizando **SQLAlchemy** como ORM e persistência de dados em **PostgreSQL**, tudo containerizado via **Docker** e orquestrado com **Docker Compose**.

---

## 🚀 Funcionalidades

- Inserção de usuários (`POST /users`)
- Listagem de usuários (`GET /users`)
- Integração com banco de dados PostgreSQL
- Isolamento completo do ambiente com Docker
- Espera ativa para inicialização do banco usando `wait-for-it.sh`

---

## 🧰 Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- Docker & Docker Compose
- wait-for-it.sh
- Postman (para testes)
