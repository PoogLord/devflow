from pydantic_settings import BaseSettings
from typing import Optional

#ค่า config จาก .env เช่น DB URL, JWT secret

class Settings(BaseSettings):
    # App
    APP_NAME: str = "DevFlow" #ชื่อ  app
    DEBUG: bool = False #error message แบบละเอียด

    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/devflow" #db ถาวร User:postgres Pass:password DB:devflow

    # Redis
    REDIS_URL: str = "redis://localhost:6379" #in-memory db ชั่วคราว

    # JWT
    JWT_SECRET: str = "your-secret-key-change-in-production" #Secret_key ใช้ decrypt
    JWT_ALGORITHM: str = "HS256" # อัลกอริทึม encrypt/decrypt
    JWT_EXPIRE_MINUTES: int = 30 # เวลาหมดอายุ token

    # AI
    ANTHROPIC_API_KEY: Optional[str] = None #API key สำหรับเรียก Claude AI — Optional เพราะถ้ายังไม่มี key app ยังรันได้ปกติ

    class Config:
        env_file = ".env" #pydantic อ่านค่าจากไฟล์ .env — ค่าใน .env จะ override ค่า default ข้างบนทั้งหมด


settings = Settings()