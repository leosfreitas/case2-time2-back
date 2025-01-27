from fastapi import APIRouter, Response

router = APIRouter()

@router.post("/user/auth/logout")
def user_logout(response: Response):
    response.delete_cookie(key="user_auth_token", domain="localhost")
    return {"status": "success", "message": "Logout realizado com sucesso"}
