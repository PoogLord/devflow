from fastapi import FastAPI #framework หลัก
from fastapi.middleware.cors import CORSMiddleware #ตัวกลางจัดการสิทธิ์การเข้าถึง
from app.config import settings #config ที่เขียนไว้ใน config.py

#ทดสอบว่ารันได้:uvicorn app.main:app --reload
# http://localhost:8000/health
# http://localhost:8000/docs   ← Swagger UI ดู API ได้เลย

app = FastAPI(
    title=settings.APP_NAME, #ชื่อ ไปโชว์ใน Swagger docs (setting)
    debug=settings.DEBUG, #debug ละเอียดขึ้น (setting)
)

# CORS — อนุญาตให้ Nuxt frontend เรียก API ได้ ปัญหาคือ browser จะบล็อก request ที่มาจาก domain อื่นโดย default ดังนั้น
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # อนุญาตเฉพาะ localhost:3000 (Nuxt) เท่านั้น
    allow_credentials=True, # อนุญาตให้ส่ง cookie/token มาด้วยได้
    allow_methods=["*"], # อนุญาตทุก HTTP method (GET, POST, PUT, DELETE)
    allow_headers=["*"], # อนุญาตทุก header
)

# endpoint แรก — ใช้เช็คว่า server ยังทำงานอยู่ไหม ########

@app.get("/health")
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}

#####################################################