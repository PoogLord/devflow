from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator

#โครงสร้าง Request/Response คุยกับ Client (Nuxt) — บอกว่ารับ/ส่งข้อมูลอะไรบ้าง

#ข้อมูลพื้นฐาน (email, username)
class UserBase(BaseModel):
    email: EmailStr
    username: str

#ใช้ตอน register → รับ password เพิ่ม
class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def password_must_be_strong(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v

#ใช้ตอบกลับ client → ไม่มี password เด็ดขาด
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True #ให้ Pydantic อ่านข้อมูลจาก SQLAlchemy Model object ได้โดยตรง

#ใช้ตอบกลับหลัง login สำเร็จ
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

#ข้อมูลที่ซ่อนอยู่ใน JWT token
class TokenData(BaseModel):
    user_id: Optional[int] = None