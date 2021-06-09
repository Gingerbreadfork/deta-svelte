from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get('/')
def home():
    return FileResponse('svelte/public/index.html')

# Place After All Other Routes
app.mount('/', StaticFiles(directory="svelte/public/"), name="static")
