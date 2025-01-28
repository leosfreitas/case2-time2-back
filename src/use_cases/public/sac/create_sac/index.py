from repositories.sac_repository import SacRepository
from .create_sac_dto import CreateSacDTO
from .create_sac_use_case import CreateSacUseCase   
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_sac_use_case = CreateSacUseCase(SacRepository())

@router.post("/sac/create")
def create_sac(create_finance_dto:CreateSacDTO, response:Response, request:Request):
    return create_sac_use_case.execute(create_finance_dto, response, request)