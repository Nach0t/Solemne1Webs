# Solemne 1 - API de Hora Actual con FastAPI

![Python CI/CD](https://github.com/nach0t/solemne1web/actions/workflows/main.yml/badge.svg) 
## Descripción

Este proyecto consiste en una API sencilla desarrollada con **FastAPI** que expone un endpoint `/time` para entregar la fecha y hora actual en formato JSON.

El objetivo es poner en práctica el uso de contenedores **Docker** y flujos de trabajo de **CI/CD** mediante **GitHub Actions**, automatizando la construcción, pruebas y despliegue de la aplicación.

---

## Tecnologías Utilizadas

- Python 3.12  
- FastAPI  
- Uvicorn  
- Poetry  
- Pytest  
- Docker  
- GitHub Actions (CI/CD)  
- Flake8 y Ruff (linting)  

---


## 📦 Docker Hub

| Métrica         | Badge |
|-----------------|--------|
| 🔗 Link         | [![Docker Hub](https://img.shields.io/badge/Docker--Hub-nach0t%2Fsolemne1web-blue?style=for-the-badge&logo=docker)](https://hub.docker.com/r/nach0t/solemne1web) |
| 🔄 Build Auto   | [![Automated Build](https://img.shields.io/docker/automated/nach0t/solemne1web?style=for-the-badge)](https://hub.docker.com/r/nach0t/solemne1web) |
| 📥 Pulls        | ![Docker Pulls](https://img.shields.io/docker/pulls/nach0t/solemne1web?style=for-the-badge) |
| 📦 Tamaño Imagen | ![Image Size](https://img.shields.io/docker/image-size/nach0t/solemne1web/latest?style=for-the-badge) |


## Instrucciones para ejecutar localmente

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Nach0t/Solemne1Webs.git
   cd Solemne1Webs
   ```

2. Instala Poetry (si no lo tienes):

   ```bash
   pip install poetry
   ```

3. Instala las dependencias del proyecto:

   ```bash
   poetry install
   ```

4. Ejecuta la aplicación localmente:

   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

5. Abre en el navegador o usa curl para probar el endpoint:

   ```bash
   http://127.0.0.1:8000/time
   ```

   ```bash
   curl http://127.0.0.1:8000/time
   ```

---
