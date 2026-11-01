from fastapi import FastAPI

app=FastAPI()

@app.get("/topla/{sayı1}/{sayı2}")

def topla(sayi1:int,sayi2:int):
    return{"sonuç":sayi1 + sayi2}
