from repositories.graphic_repository import GraphicRepository
from .get_graphic_use_case import GetGraphic1UseCase, GetGraphic2UseCase, GetGraphic3UseCase, GetGraphic4UseCase
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

get_graphic_1 = GetGraphic1UseCase(GraphicRepository())

get_graphic_2 = GetGraphic2UseCase(GraphicRepository())

get_graphic_3 = GetGraphic3UseCase(GraphicRepository())

get_graphic_4 = GetGraphic4UseCase(GraphicRepository())

@router.get("/user/get-graphic-1", dependencies=[Depends(validade_user_auth_token)])
def get_graphic(response:Response, request:Request):
    return get_graphic_1.execute(response, request)

@router.get("/user/get-graphic-2", dependencies=[Depends(validade_user_auth_token)])
def get_graphic(response:Response, request:Request):
    return get_graphic_2.execute(response, request)

@router.get("/user/get-graphic-3", dependencies=[Depends(validade_user_auth_token)])
def get_graphic(response:Response, request:Request):
    return get_graphic_3.execute(response, request)

@router.get("/user/get-graphic-4", dependencies=[Depends(validade_user_auth_token)])
def get_graphic(response:Response, request:Request):
    return get_graphic_4.execute(response, request)