from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.task import TaskStatus, TaskPriority

# ข้อมูลพื้นฐาน
# status  default = TODO
# priority default = MEDIUM
# due_date optional = ไม่มี deadline ก็ได้
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: Optional[datetime] = None

# ใช้ตอนสร้าง task
# ต้องระบุ project_id ว่าอยู่ใน project ไหน
class TaskCreate(TaskBase):
    project_id: int

# ใช้ตอนแก้ไข task
# ทุก field เป็น Optional หมด
class TaskUpdate(TaskBase):
    title: Optional[str] = None
    project_id: Optional[int] = None

# ส่งกลับ client
# มี id, owner_id, timestamp เพิ่มมา
class TaskResponse(TaskBase):
    id: int
    project_id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True