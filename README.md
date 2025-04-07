# Solemne 1 - API de Hora Actual con FastAPI

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

## Cómo ejecutar con Docker

1. Construye la imagen:

   ```bash
   docker build -t solemne1api .
   ```

2. Ejecuta el contenedor:

   ```bash
   docker run -p 8000:8000 solemne1api
   ```

3. Prueba el endpoint en el navegador o con curl:

   ```bash
   http://localhost:8000/time
   ```

   ```bash
   curl http://localhost:8000/time
   ```

---

## Cómo testear la API

Para correr las pruebas unitarias con Pytest:

```bash
poetry run pytest test_main.py
```

---

## CI/CD con GitHub Actions

Cada push a la rama `main` ejecuta automáticamente:

- Instalación de Python 3.12  
- Instalación de dependencias con Poetry  
- Revisión de código con Flake8 y Ruff  
- Ejecución de pruebas con Pytest  
- Construcción de la imagen Docker  
- Login en Docker Hub  
- Publicación de la imagen como `nach0t/solemne1web:latest`  

---

## Imagen en Docker Hub

Puedes usar la imagen directamente desde Docker Hub:

[https://hub.docker.com/r/nach0t/solemne1web](https://hub.docker.com/r/nach0t/solemne1web)

```bash
docker pull nach0t/solemne1web:latest
```
