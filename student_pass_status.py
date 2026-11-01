from fastapi import FastAPI

app=FastAPI()

@app.get("/ogrenci/{vize}/{final}")

def geçme_durumu(vize:int,final:int):
    ortalama=vize*0.40+final*0.60
    if ortalama>=50:
        return{"ortalama":ortalama,
            "sonuç":"geçti"}
    else:
        return {"ortalama":ortalama,
            "sonuç": "kaldı"}
