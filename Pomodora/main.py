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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="-00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(fg="red")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(fg="pink")
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks +="✓"
            label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
# Window

window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

#Label

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "normal"), bg=YELLOW)
label.grid(column=1, row=0)

#Canvas Or Image

canvas = Canvas(width=300, height=330, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(145, 150, image=tomato_img)
timer_text = canvas.create_text(150, 180, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)


# Start Button

start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=2)

# Reset Button

rest_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
rest_btn.grid(column=2, row=2)

#check Mark

check_mark = Label( fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

#Mainloop
window.mainloop()