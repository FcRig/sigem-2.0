from fastapi import APIRouter, Depends

router = APIRouter()

@router.post('/login')
def login(username: str, password: str):
    # TODO: implement authentication
    return {"token": "dummy"}
