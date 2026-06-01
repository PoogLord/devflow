from pydantic import BaseModel
from datetime import datetime
from typing import Optional

#ข้อมูลพื้นฐาน (title, description)
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None

#ใช้ตอนสร้าง project ใหม่
#ใช้ pass เพราะไม่ต้องเพิ่มอะไร
#มี title, description พอแล้ว
class ProjectCreate(ProjectBase):
    pass

#ใช้ตอนแก้ไข project
#title Optional เพราะอาจแก้แค่ description
class ProjectUpdate(ProjectBase):
    title: Optional[str] = None

#ส่งกลับ client
#มี id, owner_id, timestamp เพิ่มมา
class ProjectResponse(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True