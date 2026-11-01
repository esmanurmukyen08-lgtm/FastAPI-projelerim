from fastapi import FastAPI

app=FastAPI()

@app.get("/analiz/{sayi}")

def analiz(sayi:int):
    if  sayi<0:
        sayi_durumu="negatif"
    elif sayi>0:
        sayi_durumu="pozitif"
    else:
        sayi_durumu="sıfır"

    if sayi%2==0:
        sayi_turu="çift"
    else:
        sayi_turu="tek"

    return{
        "sayı durumu":sayi_durumu,
        "sayı türü":sayi_turu,
    }
