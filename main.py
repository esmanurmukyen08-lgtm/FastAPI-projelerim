from fastapi import FastAPI

app=FastAPI()

@app.get("/yas/{yas}")

def yas_sorgulama(yas:int):
    if yas>=18:
        return{"output":"reşit"}
    else:
        return{"output":"reşit değil"}
