#test deploy

# 🚀 Flask + Redis + Nginx (Docker + CI/CD)

## 📌 Description
Pet-проект, в котором я реализовал многосервисное веб-приложение и автоматизировал его сборку и запуск.

Основная цель — отработать базовые практики DevOps: контейнеризацию, взаимодействие сервисов и настройку CI/CD.

---

## ⚙️ Stack
- Python (Flask)
- Redis
- Nginx (reverse proxy)
- Docker / Docker Compose
- GitHub Actions

---

## 🧱 Architecture

Проект состоит из нескольких сервисов:

- Flask — backend-приложение  
- Redis — используется как хранилище  
- Nginx — проксирует входящие запросы  
- Docker Compose — объединяет сервисы в единую систему  

---

## 🚀 Run locally

```bash
docker-compose up --build
