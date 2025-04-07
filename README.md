# Solemne 1 - API de Hora Actual con FastAPI

![Python CI/CD](https://github.com/nach0t/solemne1web/actions/workflows/main.yml/badge.svg)

![Build Status](https://github.com/nach0t/solemne1web/actions/workflows/ci-cd.yml/badge.svg)
![Docker Image](https://img.shields.io/docker/image-size/nach0t/solemne1web/latest)
![License](https://img.shields.io/github/license/nach0t/solemne1web)

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
