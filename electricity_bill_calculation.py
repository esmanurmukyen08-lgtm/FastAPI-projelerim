from fastapi import FastAPI

app=FastAPI()

@app.get("/fatura")
def fatura(tuketim:int):
    if tuketim<=100:
        toplam=tuketim*2
    else:
        toplam=100*2+(tuketim-100)*3

        return{"toplam fatura":toplam}
