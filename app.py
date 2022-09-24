from unicodedata import name
from fastapi import FastAPI
import uvicorn
import output

app = FastAPI()

@app.get('/') 
def helloWorld():
    return f"hello It's working!"

@app.get('/index') 
def helloWorld(name : str):
    out = output.resultGeneration(name)
    return f"{out}!"


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')

