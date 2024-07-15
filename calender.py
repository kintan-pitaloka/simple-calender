import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar")

        # Get current year and month
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        # Create a frame for the calendar
        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack()

        # Create a label to display the current month and year
        self.month_year_label = ttk.Label(self.root, text="", font=("Helvetica", 16))
        self.month_year_label.pack(pady=10)

        # Create buttons to navigate between months
        self.prev_button = ttk.Button(self.root, text="Previous", command=self.show_prev_month)
        self.prev_button.pack(side="left", padx=20)
        self.next_button = ttk.Button(self.root, text="Next", command=self.show_next_month)
        self.next_button.pack(side="right", padx=20)

        # Display the current month
        self.show_month(self.current_year, self.current_month)

    def show_month(self, year, month):
        # Clear the calendar frame
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # Update the month/year label
        self.month_year_label.config(text=f"{calendar.month_name[month]} {year}")

        # Get the calendar for the specified month and year
        cal = calendar.monthcalendar(year, month)

        # Create labels for the days of the week
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in days:
            ttk.Label(self.calendar_frame, text=day, font=("Arial", 12)).grid(row=0, column=days.index(day))

        # Create labels for the days of the month
        for week in range(len(cal)):
            for day in range(len(cal[week])):
                day_num = cal[week][day]
                if day_num != 0:
                    ttk.Label(self.calendar_frame, text=str(day_num), font=("Arial", 12)).grid(row=week + 1, column=day)

    def show_prev_month(self):
        # Navigate to the previous month
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.show_month(self.current_year, self.current_month)

    def show_next_month(self):
        # Navigate to the next month
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.show_month(self.current_year, self.current_month)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
