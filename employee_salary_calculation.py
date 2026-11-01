from fastapi import FastAPI

app=FastAPI()

@app.get("/maas/{maas}/{puan}")

def personel_maas(puan:int,maas:int):
    if puan>=80:
        maas=maas+(maas*0.20)
        zam_oranı=maas*0.20
    else:
        maas=maas+(maas*0.10)
        zam_oranı=maas*0.10
    return{
        "maas":maas,
        "zam oranı":zam_oranı,
    }
