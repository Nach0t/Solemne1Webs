# Solemne1Web



@app.get("/", response_class=HTMLResponse)
async def home():
    """Página principal con un botón para ir a /time."""
    return """
    <html>
        <head>
            <title>FastAPI Time Service</title>
        </head>
        <body style="text-align: center; font-family: Arial, sans-serif;">
            <h1>Bienvenido a FastAPI</h1>
            <p>Haz clic en el botón para obtener la hora actual.</p>
            <a href="/time">
                <button style="padding: 10px 20px; font-size: 16px; cursor: pointer;">Ver Hora</button>
            </a>
        </body>
    </html>
    """
