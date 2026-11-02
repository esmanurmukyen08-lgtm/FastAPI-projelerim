from fastapi import FastAPI

app=FastAPI()

@app.get("/alan")

def alan_hesaplama(kısa:int,uzun:int):
    alan=kısa*uzun
    return alan
