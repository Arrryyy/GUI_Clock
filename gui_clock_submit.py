##Author: Aryan Jain (Matriculation: 22107593)
##File Description: This file contains a GUI implementation for a clock, with features for starting and stopping a timer,
##setting a countdown timer, and selecting the location of the timer file.
##Usage: Run the file using a Python interpreter, and the clock GUI will appear on the screen. The current time, day of week,
##and date will be displayed in a readable and nicely formatted way. The GUI contains buttons for starting and stopping a timer,
##selecting the location of the timer file, and setting a countdown timer. The timer file is created or updated as needed,
##and stores information about the start time, end time, and duration of each timer. The countdown timer can be used
##simultaneously with the regular timer.
##Libraries and Modules used: filedialog, messagebox, sys, time, datetime

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import sys
import time
import datetime

timer_is_running = False
curr_start_time = '00:00:00'
curr_end_time = '00:00:00'

class Gui_Clock():
    def toggle_start_stop(self):
        global count
        global curr_start_time
        global curr_end_time
        
        if self.start_stop_button["text"] == "Start":
            count = 0
            self.start_stop_button.configure(text="Stop", bg="red")
            self.timer()
            curr_start_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(12312312)
            print(curr_start_time)
            self.start_label.configure(text=f"Start Time: {curr_start_time} End Time: {curr_end_time}")
        else:
            count = 1
            self.start_stop_button.configure(text="Start", bg="green")
            curr_end_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.start_stop_button.config(text='Start')
            self.start_label.configure(text=f"Start Time: {curr_start_time} End Time: {curr_end_time}")
    def open_dialogue(self):
        self.file_path=fd.askopenfilename()
        self.entry_path.delete(0,"end")
        self.entry_path.insert(0,self.file_path)

    def timer(self):
        if not hasattr(self, 'remaining_time'):
            self.remaining_time = int(self.t.get().replace(':', ''))
        
        self.remaining_time += 1
        
        hrs, mins, secs = self.remaining_time // 10000, (self.remaining_time // 100) % 100, self.remaining_time % 100
        hrs_str = str(hrs).rjust(2, '0')
        mins_str = str(mins).rjust(2, '0')
        secs_str = str(secs).rjust(2, '0')
        self.d = f"{hrs_str}:{mins_str}:{secs_str}"
        self.t.set(self.d)
        
        self.root.after(1000, self.timer)

    def update_clock(self):
        now = datetime.datetime.now()
        day = now.strftime("%A")
        date = now.strftime("%B %d, %Y")
        time_str = now.strftime("%I:%M:%S %p")
        self.label.configure(text=day, font=("Courier 23 bold"),fg="green")
        self.label.place(x=175, y=90)
        self.date_label.configure(text=date, font=("Courier 30 bold"), fg="black")
        self.date_label.place(x=100, y=130)
        self.time_label.configure(text=time_str, font=("Courier 40 bold"), bg="#ADD8E6", padx=10)
        self.time_label.place(x=60, y=0)
        self.time_label.configure(highlightbackground="black", highlightthickness=2, bd=0)
        self.time_label.update()

        self.root.after(1000, self.update_clock)


    def start_countdown(self):
        hours_str = self.hours_entry.get()
        minutes_str = self.minutes_entry.get()
        seconds_str = self.seconds_entry.get()

        try:
            hours = int(hours_str)
            minutes = int(minutes_str)
            seconds = int(seconds_str)
            duration = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        except ValueError:
            messagebox.showerror("Error", "Invalid duration format. Please use HH:MM:SS format.Input in each field, only numerals.")
            return

        countdown_duration = duration
        countdown_duration_str = str(countdown_duration)

        countdown_label = Label(self.root, text=countdown_duration_str, font=("Courier 40 bold"))
        countdown_label.place(x=145, y=200)
        
        while countdown_duration.total_seconds() > 0:
            countdown_duration -= datetime.timedelta(seconds=1)
            countdown_duration_str = str(countdown_duration)
            countdown_label.configure(text=countdown_duration_str)
            countdown_label.update()
            self.root.after(1000)
        messagebox.showinfo("Countdown", "Time Over")
    def __init__(self):
        self.root=Tk()
        self.root.title("GUI Clock")
        self.root.geometry("500x600")
        self.t = StringVar()
        self.t.set("00:00:00")
    # Add the "Set Time Countdown" button    
        self.start_button = Button(self.root, text="Set Time Countdown", relief="raised", borderwidth=3,command=self.start_countdown)
        self.start_button.place(x=190, y=450)
        
        self.start_stop_button = Button(self.root, text="Start", font=("Courier 20 bold"), bg='green', command=self.toggle_start_stop)
        self.start_stop_button.place(x=197,y=340)

        self.label = Label(self.root,text="",font=("Courier 40 bold"))
        self.label.place(x=100,y=200)
        
        self.time_label = Label(self.root, font=("Courier 40 bold"))
        self.time_label.place(x=150, y=280)
        
        self.date_label = Label(self.root, font=("Courier 20 bold"))
        self.date_label.place(x=100, y=150)
        
        #The entry field, for the hours
        self.hours_entry = Entry(self.root, width=10)
        self.hours_entry.place(x=130, y=520)

        self.hours_label = Label(self.root, text=":", font=("Courier 10 bold"))
        self.hours_label.place(x=200, y=515)
        
        #The Entry field, for the minutes
        self.minutes_entry = Entry(self.root, width=10)
        self.minutes_entry.place(x=220, y=520)

        self.minutes_label = Label(self.root, text=":", font=("Courier 10 bold"))
        self.minutes_label.place(x=290, y=515)

        #The Entry field, for the seconds
        self.seconds_entry = Entry(self.root, width=10)
        self.seconds_entry.place(x=310, y=520)

        print("start time", curr_start_time)
        self.start_label = Label(self.root, text=f"Start Time: {curr_start_time} End Time: {curr_end_time} ", font=("Courier 12 bold"))
        self.start_label.place(x=50, y=300)
        self.entry_path=Entry(self.root,width=50)
        self.entry_path.pack()
        self.entry_path.place(x=100,y=400)
        self.button_open=Button(self.root, text="Open File",command=self.open_dialogue)
        self.button_open.pack()
        self.button_open.place(x=100,y=430)
        # self.start_stop_button.configure(command=self.toggle_start_stop)
        self.update_clock()
        self.root.mainloop()
    
a = Gui_Clock()

