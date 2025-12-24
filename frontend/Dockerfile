# -------- Build stage --------
FROM node:20-alpine AS build

WORKDIR /app

# 👉 Build args para Vite (se inyectan en import.meta.env)
ARG VITE_API_URL
ARG VITE_OIDC_URL
ARG VITE_OIDC_REALM
ARG VITE_OIDC_CLIENT_ID

ENV VITE_API_URL=$VITE_API_URL
ENV VITE_OIDC_URL=$VITE_OIDC_URL
ENV VITE_OIDC_REALM=$VITE_OIDC_REALM
ENV VITE_OIDC_CLIENT_ID=$VITE_OIDC_CLIENT_ID

# Copiamos solo el frontend real
COPY admin-ui/package*.json ./
RUN npm install

COPY admin-ui/ .
RUN npm run build

# -------- Runtime stage --------
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
