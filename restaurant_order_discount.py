from fastapi import FastAPI

app=FastAPI()

@app.get("/restorant")
def indirim(adet:int,fiyat:int):
    toplam_tutar=adet*fiyat
    if toplam_tutar>500:
        toplam_tutar=toplam_tutar-(toplam_tutar*0.15)
        return toplam_tutar
    else:
        return{"output":"indirim uygulanmayacak"}
