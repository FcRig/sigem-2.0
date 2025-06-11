from fastapi import APIRouter, Depends, HTTPException

users = {}

router = APIRouter()

@router.post('/register')
def register(username: str, password: str):
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[username] = password
    return {"message": "registered"}

@router.post('/login')
def login(username: str, password: str):
    if users.get(username) != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": username}
