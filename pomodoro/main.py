from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_COUNTDWN = ("Courier", 25, "bold")
FONT_EXTRA = "Montserrat"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
num_of_reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    gui.after_cancel(timer)
    canvas.itemconfig(the_timer, text="00:00")
    status_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global num_of_reps
    num_of_reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global num_of_reps
    num_of_reps += 1
    # checking which session is it
    if num_of_reps == 8:
        status_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif num_of_reps % 2 == 0:
        status_label.config(text="Short Break", fg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        status_label.config(text="Working...")
        count_down(WORK_MIN * 60)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_in_mins = math.floor(count / 60)
    count_in_sec = count % 60

    if count_in_sec == 0:
        count_in_sec = "00"
    elif count_in_sec < 10:
        count_in_sec = f"0{count_in_sec}"

    canvas.itemconfig(the_timer, text=f"{count_in_mins}:{count_in_sec}")
    if count > 0:
        global timer
        timer = gui.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(num_of_reps / 2)):
            mark += "✅"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
gui = Tk()
gui.config(padx=100, pady=50, background=PINK)
gui.title("Pomodoro 🍅 Timer")

# setting up a canvas for the background image
canvas = Canvas(width=200, height=224, background=PINK, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
the_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT_COUNTDWN)
canvas.grid(row=1, column=1)

# Status label setup
status_label = Label(text="Timer", fg=GREEN, bg=PINK, font=(FONT_EXTRA, 30, "normal"))
status_label.grid(row=0, column=1)

check_mark = Label(bg=PINK)
check_mark.grid(row=4, column=1)

# Start AND Reset buttons
start_btn = Button(text='Start', bg=PINK, font=(FONT_EXTRA, 20, "bold"), highlightbackground=PINK, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text='Reset', bg=PINK, font=(FONT_EXTRA, 20, "bold"), highlightbackground=PINK, command=reset_timer)
reset_btn.grid(row=2, column=2)

# Operations corner










gui.mainloop()