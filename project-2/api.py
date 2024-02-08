from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/stylesheets", StaticFiles(directory="stylesheets"), name="stylesheets")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/power", response_class=HTMLResponse)
def power(request:Request):
    return templates.TemplateResponse(request=request, name="power.html")
@app.get("/taylor", response_class=HTMLResponse)
def taylor(request: Request):
    return templates.TemplateResponse(request=request, name="taylor.html")