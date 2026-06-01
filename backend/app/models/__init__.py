#มี __init__.py แล้ว import สั้นลงเหลือแค่ from app.models import User, Project, Task

from app.models.user import Base, User
from app.models.project import Project
from app.models.task import Task

__all__ = ["Base", "User", "Project", "Task"]