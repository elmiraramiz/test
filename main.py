from fastapi import FastAPI
import uvicorn
import threading
import time

# ۱. ساخت شیء API (این چیزی است که رندر به آن نیاز دارد)
app = FastAPI()


# ۲. مسیری که رندر چک می‌کند (Health Check)
@app.get("/")
def read_root():
    return {"status": "ok", "message": "برنامه با موفقیت در حال اجراست"}


# ۳. تابع اصلی شما (همان کدی که قبلاً داشتید)
def your_original_main():
    print("کد اصلی شما شروع شد...")
    while True:
        # اینجا هر کاری که برنامه اصلی‌تان انجام می‌داد را قرار دهید
        # مثلاً: چاپ یک متن، پردازش داده، یا مدیریت ربات
        print("بخش Main در حال فعالیت است...")
        time.sleep(10)


# ۴. بخش جادویی: اجرای همزمان API و Main
if __name__ == "__main__":
    # اجرای تابع اصلی در یک مسیر موازی (Thread)
    threading.Thread(target=your_original_main, daemon=True).start()

    # اجرای وب‌سرور برای پاسخگویی به رندر
    uvicorn.run(app, host="0.0.0.0", port=10000)

from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake #snake=file name , Snake= class name

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()   #snake=object
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.segments[0].distance(food) < 20:
        food.refresh()
        scoreboard.add()
screen.exitonclick()
