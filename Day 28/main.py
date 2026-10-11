from tkinter import *
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
    global reps
    window.after_cancel(timer)
    Timer_label.config(text="Timer")
    text.config(text=check)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    counter = 0
    if reps % 8 == 0:
        counter = long_break_sec
        Timer_label.config(text = "Break",fg = RED)
    elif reps % 2 == 0:
        counter = short_break_sec
        Timer_label.config(text="Break", fg=PINK)
    else:
        counter = work_sec
        Timer_label.config(text="Work", fg=GREEN)

    count_down(counter)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = int(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(int(reps/2)):
                 mark += "✔"
        text.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady = 50,bg = YELLOW)

# def demo(demo,a,b,c):
#     print(demo)
#     print(a)
#     print(b)
#     print(c)
#
#
# window.after(1000,demo,"Hello",3,5,8)

Timer_label = Label(text = "Timer",font = ("Courier",36,"bold"),fg = GREEN,bg = YELLOW,highlightthickness=0)
Timer_label.grid(row = 0,column = 1)

canvas = Canvas(width = 200, height = 224,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image( 100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text = "00:00",fill = "White",font = ("Courier",35,"bold"))
canvas.grid(row = 1,column = 1)



start = Button(text = "Start",font = ("Courier",11,"bold"),command = start_timer)
start.grid(row = 2,column = 0)

reset = Button(text = "Reset",font = ("Courier",11,"bold"),command=reset_timer)
reset.grid(row = 2,column = 2)

check = ""
text = Label(text = check, fg = GREEN,bg = YELLOW,highlightthickness=0)
text.grid(row = 3,column = 1)

window.mainloop()
