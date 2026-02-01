from fastapi import Header, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

def verifica_token(x_api_key:str | None = Header(default=None)):
    if x_api_key is None:
        raise HTTPException(status_code=401, detail="Token não informado")
    if  x_api_key != api_key:
        raise HTTPException(status_code=401, detail="Token não autorizado")
