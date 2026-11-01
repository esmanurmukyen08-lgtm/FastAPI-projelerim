from fastapi import FastAPI

app=FastAPI()

@app.get("/kitap{kitap_sayisi}/{gun}")

def toplam_ceza(kitap_sayisi:int,gun:int):
    toplam_ceza=(kitap_sayisi*gun)*2
    if toplam_ceza>=50:
        ceza_turu="yüksek ceza"
    else:
        ceza_turu = "normal ceza"

    return{
        "toplam ceza":toplam_ceza,
        "ceza türü":ceza_turu
    }
