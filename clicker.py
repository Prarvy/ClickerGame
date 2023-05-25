# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: Clicker Game
# Version: 1.0: Base version by author
import random
import tkinter as tk


class Clicker:
    # Initialize the game parameters
    def __init__(self, _window):
        self.window = _window
        self.numbers = None
        self.sorted_numbers = None
        self.timer_label = None
        self.timer_start = True
        self.timer_value = 0
        self.font_style = ('Arial Bold', 25)
        self.timer_font = ('Arial', 18)
        self.initialize_board()

    # Start and display the game board
    def initialize_board(self):
        self.numbers = random.sample(range(1, 1000), 25)
        self.sorted_numbers = sorted(self.numbers)

        for i in range(25):
            button = tk.Button(self.window, text=self.numbers[i], width=4, height=1, state=tk.NORMAL,
                               font=self.font_style, fg='dark green', borderwidth=10, activebackground='red',
                               activeforeground='white')
            button.grid(row=i % 5, column=i // 5)
            button.bind('<Button-1>', self.button_click)
        self.timer_label = tk.Label(self.window, text='TIMER will start automatically.', height=2, font=self.timer_font)
        self.timer_label.grid(row=6, column=0, columnspan=5)

    # Verify the moves and update the game board
    def button_click(self, event):
        click_event = event.widget
        if self.timer_start:
            self.timer_start = False
            self.timer()
        if int(click_event['text']) == self.sorted_numbers[0]:
            click_event.configure(text='X')
            click_event.configure(state=tk.DISABLED)
            del self.sorted_numbers[0]

    # Display timer
    def timer(self):
        self.timer_label.configure(text='Timer: ' + str(self.timer_value) + ' Seconds')
        if len(self.sorted_numbers) > 0:
            self.timer_value += 1
            self.window.after(1000, self.timer)
        else:
            self.timer_label.configure(text='You have completed the game in '+str(self.timer_value) + ' Seconds')


if __name__ == "__main__":
    window = tk.Tk()
    window.title('C L I C K E R')
    window.config(borderwidth=20)
    window.config(background='#f2f2f2')
    window.iconbitmap(window, default="clicker.ico")
    clicker = Clicker(window)
    window.mainloop()
