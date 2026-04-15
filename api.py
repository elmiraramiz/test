from fastapi import FastAPI

# ۱. ساخت یک نمونه از اپلیکیشن
app = FastAPI()

# ۲. تعریف تابع قدیمی شما
def my_function(name):
    return f"سلام {name}، پردازش انجام شد!"

# ۳. ایجاد یک "مسیر" (Route) برای API
@app.get("/process")
def read_item(username: str = "مهمان"):
    # اینجا تابع قدیمی‌تان را صدا می‌زنید
    result = my_function(username)
    return {"status": "success", "data": result}

@app.get("/")
def home():
    return {"message": "خوش آمدید! این API فعال است."}