"""
To be launched using: uvicorn api:app --reload
Before trying to launch it, be sure to: pip install fastapi
"""

# FastAPI imports
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Algorithms imports
from pow_simetric import method_pow_simetric
from Taylor_interpolation import Taylor_interpolation
import numpy as np

# FastAPI, files and templates setup
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/stylesheets", StaticFiles(directory="stylesheets"), name="stylesheets")

# Templates responses
@app.get("/", response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/power", response_class=HTMLResponse)
def power(request:Request):
    return templates.TemplateResponse(request=request, name="power.html",
                                      context={"m":"m", "n":"n", "value":"λ", "vector":"v"})
@app.get("/taylor", response_class=HTMLResponse)
def taylor(request:Request):
    return templates.TemplateResponse(request=request, name="taylor.html",
                                      context={"f":"f(x)", "a":"a", "x":"x", "result": "result"})

# Functions responses
@app.get("/taylor/calc")
async def interpolation(request:Request, func:str, a:float, x:float):
    if func in ["sin(x)", "cos(x)", "log(x)", "exp(x)"]:
        f = lambda x: eval(f"np.{func}")
        result = Taylor_interpolation(f, a, x)
    else:
        result = "Error: invalid function"

    return templates.TemplateResponse(request=request, name="taylor.html", 
                                      context={"f":func, "a":a, "x":x, "result": result})

@app.get("/power/calc")
async def eigen(request:Request, m: str, n: int):
    try:
        matrix = np.matrix(eval(m))
    except Exception:
        value, vector = "x"

    # Simmetric matrix validation
    if not ( np.equal(matrix,matrix.T).all() or  matrix.shape[0] == matrix.shape[1] ):
        vector = "x"
        value = vector
    else:
        vector, value = method_pow_simetric(matrix,n)

    return templates.TemplateResponse(request=request, name="power.html",
                                      context={"m":matrix, "n":n, "value":value, "vector":vector})
