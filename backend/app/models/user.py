from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) #primary key, auto increment
    email = Column(String, unique=True, index=True, nullable=False) #unique, ใช้ login
    username = Column(String, unique=True, index=True, nullable=False) #unique, แสดงในแอป
    hashed_password = Column(String, nullable=False) #เก็บ password ที่ hash แล้ว ไม่เก็บ plain text
    is_active = Column(Boolean, default=True) #ปิด/เปิด account โดยไม่ต้องลบ
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) #วันที่สร้าง
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) #วันที่แก้ไขล่าสุด