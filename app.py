from unicodedata import name
from fastapi import FastAPI, Request
import uvicorn
import output

app = FastAPI()

@app.get('/') 
def intialCheck():
    return f"It's working!"

#http://localhost:8080/index?name=launch%20browser
@app.get('/getResponse') 
def getResponse(name : str):
    out = output.resultGeneration(name)
    return {
        "status" : "SUCCESS",
        "response" : out
    }

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')

