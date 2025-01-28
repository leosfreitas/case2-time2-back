from fastapi import APIRouter, Response

router = APIRouter()

@router.post("/admin/auth/logout")
def admin_logout(response: Response):
    response.delete_cookie(key="admin_auth_token", domain="localhost")
    return {"status": "success", "message": "Logout realizado com sucesso"}
