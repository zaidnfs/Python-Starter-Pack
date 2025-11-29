from tkinter import *
import  math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CLOCK = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(CLOCK)
    timer.config(text="Timer", fg=GREEN)
    checkmark.config(text="", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=PINK)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=GREEN)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global CLOCK
        CLOCK = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += "✔️"
        checkmark.config(text=marks)
        if work_session == 4:
            reset_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

#Lable
timer = Label(text="Timer", highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
timer.grid(row=0, column=1)

#Button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

#Checkmark
symbol = "✔"
checkmark= Label(highlightthickness=0, bg=YELLOW, fg=GREEN)
checkmark.grid(row=3, column=1)
window.mainloop()