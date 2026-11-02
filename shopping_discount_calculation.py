from fastapi import FastAPI

app=FastAPI()

@app.get("/alısveris")

def indirim_hesaplama(fiyat:int,adet:int):
    toplam_tutar=fiyat*adet

    if toplam_tutar>1000:
        return{"output":"indirim kazandınız"}
    else:
        return {"output": "indirim kazanamadınız"}
