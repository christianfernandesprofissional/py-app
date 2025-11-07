from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>Hello FastAPI</title>
        </head>
        <body>
            <h1>Hello Beautiful World 🌎</h1>
            <p>Esta é uma página HTML servida pelo FastAPI.</p>
        </body>
    </html>
    """
    return html_content
