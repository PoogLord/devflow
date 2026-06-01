from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.models.user import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) #เชื่อมกับ users.id (project นี้เป็นของ user ไหน)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    owner = relationship("User", backref="projects") #ดึงข้อมูล user เจ้าของได้เลย
    tasks = relationship("Task", backref="project", cascade="all, delete-orphan") # 1 Project มีหลาย task ถ้าลบ project จะลบ tasks ในนั้นทั้งหมดด้วย