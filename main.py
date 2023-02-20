import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARKER_GREEN = "#45634c"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def raise_window(wind):
    wind.state('normal')
    wind.attributes('-topmost', True)


# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
    global reps
    reps = 0
    window.after_cancel(id=timer)
    timer_title.config(text="Timer", bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    window.config(bg=YELLOW)
    canvas.config(bg=YELLOW)
    button_start.config(bg=GREEN, relief="groove", fg=DARKER_GREEN)
    button_reset.config(bg=GREEN, relief="groove", fg=DARKER_GREEN)
    check_mark.config(bg=YELLOW)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_title.config(text="Long break", fg=GREEN, bg=YELLOW)
        window.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        button_start.config(bg=YELLOW, fg=YELLOW)
        button_reset.config(bg=YELLOW, fg=YELLOW)
        check_mark.config(bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_title.config(text="Break", fg=PINK, bg=YELLOW)
        window.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        button_start.config(bg=YELLOW, fg=YELLOW)
        button_reset.config(bg=YELLOW, fg=YELLOW)
        check_mark.config(bg=YELLOW)
        count_down(short_break_sec)
    else:
        timer_title.config(text="Work", fg=RED, bg=PINK)
        window.config(bg=PINK)
        canvas.config(bg=PINK)
        button_start.config(bg=PINK, fg=PINK, relief="flat")
        button_reset.config(bg=RED, fg="black")
        check_mark.config(bg=PINK)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    time_min = math.floor(count / 60)
    time_sec = count % 60
    if time_sec < 10:
        time_sec = f"0{time_sec}"
    canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        raise_window(window)
        start_timer()
        check = "✔"
        if reps % 2 == 0:
            check_mark.config(text=check * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, count_down, )

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato/tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# buttons
button_start = tkinter.Button(text="Start", bg=GREEN, relief="groove", font=(FONT_NAME, 10), fg=DARKER_GREEN,
                              command=start_timer)  # command
button_start.grid(column=0, row=2)
button_reset = tkinter.Button(text="Reset", bg=GREEN, relief="groove", font=(FONT_NAME, 10), fg=DARKER_GREEN,
                              command=time_reset)  # command
button_reset.grid(column=2, row=2)

# labels
timer_title = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), highlightthickness=0, bg=YELLOW, fg=GREEN)
timer_title.grid(column=1, row=0)

# check marks
check_mark = tkinter.Label(font=(FONT_NAME, 15), highlightthickness=0, bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()
