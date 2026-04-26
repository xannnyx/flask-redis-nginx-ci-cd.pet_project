#test deploy

🚀 Flask + Redis + Nginx CI/CD Project


📌 Description

Многосервисное веб-приложение, развернутое с использованием Docker и автоматизированного CI/CD пайплайна


⚙️ Stack

* Python (Flask)
* Redis
* Nginx (reverse proxy)
* Docker / Docker Compose
* GitHub Actions (CI/CD)


🧱 Architecture

* Flask — backend
* Redis — кэш
* Nginx — прокси
* Docker Compose — оркестрация


🚀 Run locally
* docker-compose up --build


🔄 CI/CD

* автоматическая сборка Docker-образа
* запуск пайплайна при push
* проверка работоспособности


🧠 What I learned

* работа с multi-container архитектурой
* настройка взаимодействия сервисов
* контейнеризация приложений
* базовая автоматизация CI/CD
