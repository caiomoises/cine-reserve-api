# 🎬 CineReserve API

API RESTful para gerenciamento de cinema, permitindo:

* Cadastro e autenticação de usuários
* Listagem de filmes e sessões
* Visualização de assentos em tempo real
* Reserva temporária de assentos com controle de concorrência (Redis)
* Compra de ingressos
* Consulta de tickets do usuário

---

# 🚀 Tecnologias utilizadas

* Python 3.12
* Django
* Django REST Framework
* PostgreSQL (ou SQLite para desenvolvimento)
* Redis (controle de concorrência)
* JWT (autenticação)
* Poetry (gerenciamento de dependências)
* Docker (opcional)

---

# 📂 Estrutura do projeto

```
cine-reserve-api/
│
├── cine/
│   ├── admin/
│   ├── migrations/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── viewsets/
│   └── urls.py
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── services/
│       ├── redis_client.py
│       └── seat_lock.py
│
├── manage.py
├── pyproject.toml
├── insomnia_collection.json
└── README.md
```

---

# ⚙️ Configuração do ambiente

## 1️⃣ Clonar o projeto

```
git clone <repo-url>
cd cine-reserve-api
```

---

## 2️⃣ Instalar Poetry

```
sudo apt install python3-poetry
```

---

## 3️⃣ Instalar dependências

```
poetry install
```

---

## 4️⃣ Ativar ambiente virtual

```
poetry shell
```

---

## 5️⃣ Criar arquivo `.env`

```
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=cine
DB_USER=cine
DB_PASSWORD=cine
DB_HOST=localhost
DB_PORT=5432

REDIS_URL=redis://localhost:6379/0
```

---

## 6️⃣ Rodar migrações

```
python manage.py migrate
```

---

## 7️⃣ Criar superusuário

```
python manage.py createsuperuser
```

---

## 8️⃣ Rodar o servidor

```
python manage.py runserver
```

---

# 🔴 Configurar Redis

## Instalar

```
sudo apt install redis-server
```

## Iniciar

```
sudo service redis-server start
```

## Testar

```
redis-cli ping
```

Resposta esperada:

```
PONG
```

---

# 🔐 Autenticação (JWT)

## Obter token

```
POST /api/token/
```

### Body

```json
{
  "username": "admin",
  "password": "123456"
}
```

### Resposta

```json
{
  "access": "TOKEN_AQUI"
}
```

---

## Usar token

Header obrigatório:

```
Authorization: Bearer SEU_TOKEN
```

---

# 🔄 Fluxo da aplicação

1. Usuário realiza login (JWT)
2. Lista filmes disponíveis
3. Seleciona uma sessão
4. Visualiza assentos disponíveis (Seat Map)
5. Reserva um assento (lock no Redis)
6. Realiza checkout
7. Ticket é gerado
8. Consulta tickets em "My Tickets"

---

# ⚠️ Regras de negócio

* Um assento não pode ser reservado por mais de um usuário simultaneamente
* Reservas possuem tempo de expiração (TTL no Redis)
* Apenas o usuário que reservou pode finalizar o checkout
* Um assento comprado não pode ser reservado novamente

---

# 🧠 Decisões técnicas

* Redis utilizado para controle de concorrência em tempo real
* Locks distribuídos evitam conflito de reservas
* Separação entre dados temporários (Redis) e persistentes (PostgreSQL)
* JWT para autenticação stateless
* Arquitetura modular separando regras de negócio em services

---

# 📡 Endpoints

---

## 🎬 1. Filmes

### Criar filme

```
POST /api/movies/
```

```json
{
  "title": "Interestelar",
  "description": "Viagem espacial",
  "duration": 169,
  "release_date": "2014-11-07"
}
```

---

### Listar filmes

```
GET /api/movies/
```

---

## 🎟️ 2. Sessões

```
GET /api/sessions/?movie_id=1
```

---

## 🪑 3. Seat Map

```
GET /api/sessions/{session_id}/seats/
```

```json
[
  { "seat_id": 1, "number": "A1", "status": "available" },
  { "seat_id": 2, "number": "A2", "status": "reserved" },
  { "seat_id": 3, "number": "A3", "status": "purchased" }
]
```

---

## 🎯 4. Reservar assento

```
POST /api/reserve-seat/
```

```json
{
  "session_id": 1,
  "seat_id": 10
}
```

---

## 🎫 5. Checkout

```
POST /api/checkout/
```

* Converte reserva em compra
* Remove lock do Redis
* Gera ticket

---

## 👤 6. My Tickets

```
GET /api/my-tickets/
```

---

# 🔒 Status dos assentos

| Status    | Descrição                 |
| --------- | ------------------------- |
| available | Livre                     |
| reserved  | Reservado (Redis)         |
| purchased | Comprado (Banco de dados) |

---

# 🔍 Debug Redis

```
redis-cli
keys seat_lock:*
get seat_lock:1:10
ttl seat_lock:1:10
```

---

# 🧪 Testes com Insomnia

O projeto inclui uma collection para facilitar os testes.

## 📂 Arquivo

```
insomnia_collection.json
```

## 🚀 Como usar

1. Abra o Insomnia
2. Clique em "Import"
3. Selecione o arquivo
4. Execute as requisições na ordem:

* Login
* Movies
* Reservation
* Seat Map
* Checkout
* My Tickets

---

# 🧪 Testes automatizados

```
python manage.py test
```

---

# 🐳 Docker (opcional)

```
docker-compose up --build
```

---

# 🔥 Funcionalidades implementadas

* Autenticação JWT
* CRUD de filmes
* Sessões de cinema
* Seat Map em tempo real
* Lock de assentos com Redis
* Prevenção de concorrência
* Reserva com timeout
* Checkout e geração de tickets

---

# 🚀 Melhorias futuras

* Expiração automática com Celery
* Reserva de múltiplos assentos
* Rate limiting
* Cache de sessões populares
* CI/CD com GitHub Actions
* Deploy em cloud (AWS, Railway)

---

# 🧠 Conceitos aplicados

* RESTful API
* Controle de concorrência distribuída
* Cache com Redis
* Arquitetura escalável
* Separação de responsabilidades

---

# 📌 Autor

Desenvolvido por Caio Moisés 🚀
