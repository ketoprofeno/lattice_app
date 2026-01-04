# lattice_app

**lattice_app** es una **admin application modular** diseñada como base reusable para proyectos de **analítica avanzada, data platforms y aplicaciones internas**.  
El proyecto sigue una arquitectura desacoplada **Frontend + Backend**, con separación clara entre **entorno de desarrollo (DEV)** y **entorno productivo (PROD)**, preparada para escalar con **autenticación, RBAC y microservicios**.

---

## 🧱 Arquitectura General

- **Frontend (DEV)**: React + TypeScript (Vite Dev Server)
- **Frontend (PROD)**: Build estático servido por Nginx
- **Backend**: FastAPI (Python), arquitectura modular
- **Infraestructura**: Docker + Docker Compose
- **Autenticación**: Keycloak (OIDC)
- **Objetivo**: servir como **plantilla base profesional** para admin apps modernas y productos de datos

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
- Arquitectura modular por dominios
- Middleware de auditoría
- Preparado para RBAC y validación JWT

### Frontend
- React 18
- TypeScript
- Vite (DEV)
- Tailwind CSS
- Preparado para shadcn/ui
- Nginx (PROD)

### Infraestructura
- Docker
- Docker Compose
- Separación DEV / PROD

### Autenticación
- Keycloak 25.x
- OpenID Connect (Authorization Code + PKCE)
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
│   │   ├── middleware/
│   │   └── logging/
│   ├── modules/
│   ├── integrations/
│   ├── main.py
│   └── __init__.py
├── pyproject.toml
└── Dockerfile
```

### Frontend

```
frontend/
├── admin-ui/
│   ├── src/
│   │   ├── auth/
│   │   ├── layouts/
│   │   ├── routes/
│   │   ├── pages/
│   │   └── main.tsx
│   ├── tailwind.config.js
│   ├── vite.config.ts
│   └── Dockerfile
├── Dockerfile.dev
└── nginx.conf
```

### Infraestructura

```
infra/
├── docker-compose.yml
└── keycloak/
    └── realm-dev.json
```

---

## 🚀 Entornos de Ejecución

### 🧪 Desarrollo (DEV)

- Frontend corre con **Vite** (hot reload)
- Backend corre en FastAPI
- Keycloak dockerizado
- Comunicación vía proxy `/api`

Servicios DEV:

| Servicio  | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend  | http://localhost:8000 |
| Keycloak | http://localhost:8080 |

El frontend consume el backend usando rutas relativas:

```
/api/*
```

Esto evita hardcodear URLs y permite transición limpia a PROD.

---

### 🏭 Producción (PROD)

- Frontend compilado (`npm run build`)
- Servido por **Nginx**
- Backend desacoplado
- Variables de entorno controlan endpoints reales

No se requieren cambios estructurales en el código para pasar de DEV a PROD.

---

## 🔐 Autenticación y Autorización

### Autenticación (Auth)

- Gestionada por **Keycloak**
- Login vía OIDC + PKCE
- Token JWT compartido entre frontend y backend
- Endpoint `/api/me` retorna identidad del usuario autenticado

### Autorización (AuthZ)

- **Frontend**:
  - `ProtectedRoute` protege navegación y UX
  - Basado en roles (`admin`, `viewer`)
- **Backend**:
  - Validación de roles se implementará en endpoints sensibles
  - Separación clara entre identidad y permisos

> 📌 En etapa actual, la autorización backend se considera **deuda técnica controlada**, permitiendo avanzar en UI sin bloquear desarrollo.

---

## 🔐 Keycloak (DEV)

Realm importado automáticamente desde:

```
infra/keycloak/realm-dev.json
```

Configuración:
- Realm: `lattice`
- Roles: `admin`, `viewer`
- Usuario dev creado automáticamente
- HTTP habilitado solo en DEV

Acceso consola:

```
http://localhost:8080/admin
user: admin
pass: admin
```

---

## 🧠 Principios de Diseño

- Separación DEV / PROD clara
- Frontend y backend desacoplados
- Auth y AuthZ correctamente diferenciados
- Modularidad y escalabilidad
- Preparado para CI/CD y despliegues productivos

---

## 🛣️ Roadmap

- Autenticación OIDC completa ✅
- Admin UI base (layout + navegación) ✅
- RBAC backend ⏳
- Persistencia (PostgreSQL)
- Auditoría avanzada
- Observabilidad
- CI/CD
- Despliegue productivo

---

## 👤 Autor

**Lattice**  
Base profesional para soluciones de ingeniería, analítica avanzada y productos de datos.
