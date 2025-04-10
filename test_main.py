from fastapi.testclient import TestClient

from main import app
# Importa la instancia de la aplicación FastAPI definida en el archivo main.py.

client = TestClient(app)
# Crea una instancia de TestClient para ejecutar pruebas.


def test_get_time():
    # Define una función de prueba para verificar el endpoint /time.
    response = client.get("/time")
    # Envía una solicitud GET al endpoint /time.
    assert response.status_code == 200
    # Verifica que el código de estado HTTP sea 200 (OK).
    assert "time" in response.json()
    # Verifica que la respuesta contenga la clave "time" en el JSON devuelto.
    
