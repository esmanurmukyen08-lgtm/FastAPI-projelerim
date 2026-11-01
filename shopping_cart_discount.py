from fastapi import FastAPI

app=FastAPI()

@app.get("/alısveriş")

def indirim(fiyat:int,adet:int):
    toplam_tutar=fiyat * adet
    if toplam_tutar >=1000:
        toplam_tutar=toplam_tutar-(toplam_tutar*0.10)
    return{"son fiyat":toplam_tutar}
