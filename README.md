# lattice_app

**lattice_app** es una **admin application modular** diseñada como base reusable para proyectos de **analítica avanzada, data platforms y aplicaciones internas**.  
El proyecto sigue una arquitectura desacoplada **Frontend + Backend**, está completamente **dockerizado** y preparado para escalar con **autenticación, RBAC y microservicios**.

---

## 🧱 Arquitectura General

- **Frontend**: React + TypeScript (Vite), servido con Nginx
- **Backend**: FastAPI (Python), arquitectura modular
- **Infraestructura**: Docker + Docker Compose
- **Autenticación**: Keycloak (OIDC)
- **Objetivo**: servir como **plantilla base** para admin apps modernas y productos de datos

```
lattice_app/
├── backend/        # FastAPI backend
├── frontend/       # React admin UI
├── infra/          # Docker Compose e infraestructura
└── docs/           # Documentación de arquitectura
```

---

## 📦 Stack Tecnológico

### Backend
- Python 3.11
- FastAPI
- Uvicorn
- Poetry (gestión de dependencias)
- Arquitectura modular por dominios

### Frontend
- React 18
- TypeScript
- Vite
- Nginx (producción)

### Infraestructura
- Docker
- Docker Compose

### Autenticación
- Keycloak 25.x
- OpenID Connect (OIDC)
- JWT

---

## 🗂️ Estructura del Proyecto

### Backend

```
backend/
├── app/
│   ├── core/
│   │   ├── config/
│   │   ├── security/
│   │   ├── rbac/
│   │   ├── audit/
│   │   └── api.py
│   ├── modules/
│   │   └── health/
│   │       ├── router.py
│   │       └── __init__.py
│   ├── integrations/
│   ├── main.py
│   └── __init__.py
├── pyproject.toml
├── poetry.lock
└── Dockerfile
```

### Frontend

```
frontend/
├── admin-ui/
│   ├── src/
│   │   ├── auth/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── services/
│   │   └── main.tsx
│   ├── index.html
│   ├── package.json
│   └── Dockerfile
```

### Infraestructura

```
infra/
├── docker-compose.yml
└── keycloak/
    └── realm-dev.json
```

---

## 🚀 Levantar el Proyecto Localmente

### Requisitos
- Docker
- Docker Compose

### Ejecución

Desde la raíz del proyecto:

```bash
docker compose -f infra/docker-compose.yml up --build
```

---

## 🌐 Servicios Disponibles

| Servicio  | URL                           | Descripción                    |
|-----------|-------------------------------|--------------------------------|
| Frontend  | http://localhost:3000         | Admin UI (React)               |
| Backend   | http://localhost:8000/health  | API FastAPI (health check)     |
| Keycloak  | http://localhost:8080/admin   | Consola de administración IAM  |

Respuesta esperada del backend:

```json
{"status":"ok"}
```

---

## 🔐 Autenticación y Autorización (Keycloak)

El proyecto cuenta con una **base de autenticación centralizada** utilizando **Keycloak** en modo desarrollo, preparada para integrarse con el frontend (React) y el backend (FastAPI) mediante **OpenID Connect (OIDC)** y tokens JWT.

### 📌 Características

- Keycloak dockerizado como parte del stack
- Arranque en modo desarrollo (`start-dev`)
- Realm dedicado: `lattice`
- Importación automática del realm al iniciar
- Soporte HTTP para entorno local
- Base para login, SSO y RBAC

### 🗂️ Realm de desarrollo

El realm `lattice` se importa automáticamente desde:

```
infra/keycloak/realm-dev.json
```

Configuración destacada:

- `sslRequired = NONE` (solo desarrollo)
- Roles iniciales:
  - `admin`
  - `viewer`

Esto permite un entorno **reproducible e idempotente**.

### 🔑 Acceso al Admin Console

```text
URL:      http://localhost:8080/admin
Usuario:  admin
Password: admin
```

> ⚠️ Credenciales solo para desarrollo local.

### 🧭 Uso previsto

Keycloak será utilizado para:

- Autenticación del frontend vía OIDC (Authorization Code + PKCE)
- Emisión de JWT
- Validación de tokens en FastAPI
- Implementación de RBAC basado en roles del realm

---

## 🧠 Principios de Diseño

- **Desacoplado**: Frontend y Backend independientes
- **Modular**: backend organizado por dominios (`modules`)
- **Escalable**: preparado para auth, RBAC, auditoría y microservicios
- **Reutilizable**: base común para múltiples proyectos
- **Infra-ready**: dockerizado y listo para CI/CD

---

## 🔐 Roadmap

- Autenticación centralizada con Keycloak (OIDC) ✅
- Integración JWT FastAPI ↔ Keycloak ⏳
- RBAC (roles y permisos) ⏳
- Layout admin base (sidebar + header)
- Persistencia (PostgreSQL)
- Auditoría y trazabilidad
- Observabilidad y métricas
- CI/CD y despliegue en entornos productivos

---

## 📄 Documentación

- Arquitectura general: `docs/architecture.md`
- Autenticación y seguridad: en progreso

---

## 🧩 Convención de Commits (recomendada)

```text
feat: nueva funcionalidad
fix: corrección de bug
chore: tareas de mantenimiento
docs: documentación
refactor: refactorización sin cambio funcional
```

---

## 👤 Autor

**Lattice**  
Base para soluciones de ingeniería, analítica avanzada y productos de datos.
