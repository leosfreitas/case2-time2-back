from fastapi import APIRouter, Response
from use_cases.public.sac.get_sac.get_sac_use_case import GetAllSacsUseCase
from repositories.sac_repository import SacRepository

router = APIRouter()

get_all_sacs_use_case = GetAllSacsUseCase(SacRepository())

@router.get("/sacs/get")
def get_all_sacs(response: Response):
    return get_all_sacs_use_case.execute(response)
