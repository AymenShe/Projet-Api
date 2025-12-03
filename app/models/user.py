from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    address: str | None = None
    is_active: bool = True 
    is_superuser: bool = False

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    full_name: str | None = None
    address:str | None = None
    password: str | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
