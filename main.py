from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()

app.mount('', StaticFiles(directory="svelte/public/", html=True), name="static")