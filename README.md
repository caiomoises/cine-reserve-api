# 🎬 CineReserve API

API RESTful para gerenciamento de cinema, permitindo:

* Cadastro e autenticação de usuários
* Listagem de filmes e sessões
* Visualização de assentos em tempo real
* Reserva temporária de assentos (Redis)
* Compra de ingressos
* Consulta de tickets do usuário

---

# 🚀 Tecnologias utilizadas

* Python 3.12
* Django
* Django REST Framework
* PostgreSQL (ou SQLite para dev)
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

## 5️⃣ Rodar migrações

```
python manage.py migrate
```

---

## 6️⃣ Criar superusuário

```
python manage.py createsuperuser
```

---

## 7️⃣ Rodar o servidor

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

### Listar sessões de um filme

```
GET /api/sessions/?movie_id=1
```

---

## 🪑 3. Seat Map (assentos)

### Ver status dos assentos

```
GET /api/sessions/{session_id}/seats/
```

### Resposta

```json
[
  {
    "seat_id": 1,
    "number": "A1",
    "status": "available"
  },
  {
    "seat_id": 2,
    "number": "A2",
    "status": "reserved"
  },
  {
    "seat_id": 3,
    "number": "A3",
    "status": "purchased"
  }
]
```

---

# 🔒 Status dos assentos

| Status    | Descrição                         |
| --------- | --------------------------------- |
| available | livre                             |
| reserved  | reservado temporariamente (Redis) |
| purchased | comprado (DB)                     |

---

## 🧠 Como funciona

* Redis controla reservas temporárias (10 minutos)
* Banco controla compras definitivas

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

### Possíveis respostas

✔ Sucesso:

```json
{
  "message": "Seat reserved successfully"
}
```

❌ Já reservado:

```json
{
  "error": "Seat already reserved"
}
```

❌ Já comprado:

```json
{
  "error": "Seat already purchased"
}
```

---

# 🔍 Debug Redis

## Ver assentos reservados

```
redis-cli
```

```
keys seat_lock:*
```

---

## Ver quem reservou

```
get seat_lock:1:10
```

---

## Tempo restante

```
ttl seat_lock:1:10
```

---

# 🎫 5. Checkout (gerar ticket)

(Se implementado)

```
POST /api/checkout/
```

* Converte reserva em compra
* Remove lock do Redis
* Cria Ticket no banco

---

# 👤 6. Meus Tickets

```
GET /api/my-tickets/
```

---

# 🧪 Testes

Rodar testes:

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

✔ Autenticação JWT
✔ CRUD de filmes
✔ Sessões de cinema
✔ Seat Map em tempo real
✔ Lock de assentos com Redis
✔ Prevenção de concorrência
✔ Reserva com timeout
✔ Geração de tickets

---

# 🚀 Possíveis melhorias

* Expiração automática com Celery
* Rate limiting
* Cache de sessões populares
* CI/CD com GitHub Actions
* Logs estruturados
* Monitoramento

---

# 🧠 Conceitos aplicados

* RESTful API
* Controle de concorrência distribuída
* Cache com Redis
* Separação de responsabilidades
* Arquitetura escalável

---

# 📌 Autor

Desenvolvido por Caio Moisés 🚀
