from fastapi import FastAPI
from starlette.responses import RedirectResponse
from .import models, schemas
from .Conexion import SessionLocal, engine

from fastapi.params import Depends

from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/fibo/{indice}')
def get_fibonacci(indice:int):

    # primeros dos digitos
    n1, n2 = 0, 1
    count = 0

    print("Serie Fibonacci:")
    while count < 11:
        print(n1)
        nth = n1 + n2
        # actualizacions
        n1 = n2
        n2 = nth
        count += 1
        
    #nterms = int(input("Ingresa numero de Indice: "))

    def fibonacci(n):
        if n <= 0:
            return "Incorrecto..."
        data = [0, 1]
        if n > 2:
            for i in range(2, n):
                data.append(data[i-1] + data[i-2])
        return 'Numero de la serie:' + str(data[n-1])
    
    # Llamada a funcion
    if indice >= 11:
         print("Numero debe ser menor de 10...")
    else:
         print(fibonacci(indice + 1))
        
    return {fibonacci(indice + 1)}


