from fastapi import APIRouter, HTTPException, Depends
import httpx, os
from dotenv import load_dotenv
from app.core.auth import verifica_token


load_dotenv()
endereco_api = os.getenv('URL')


router = APIRouter(prefix='/api/v1')

parametro_1 = {'people', 'planets','starships'}

@router.get('/busca', status_code=200, summary="Retorna informaçoes detalhadas de planeta, personagens e espaço-naves  do Star Wars")
async def lista_informacao(parametro_1:str, parametro_2:str, token=Depends(verifica_token)):
   
   try:
        
        if parametro_1 not in {'people', 'planets','starships'}:
            raise HTTPException(status_code=400, detail="Parametros validos : people, planets, starships")
        
        async with httpx.AsyncClient() as cliente:
          
          req =  await cliente.get(f"{endereco_api}/{parametro_1}/?search={parametro_2}")
          dados = req.json()
          resultado = dados.get("results", [])
        return resultado
   
   except Exception:
        raise HTTPException(status_code=400)
    
    
