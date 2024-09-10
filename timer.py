"""
This script is for analyzing the execution time of programs
"""
from threading import Timer

class TimerExecution:
    def __init__(self):
        self.time = 0
        self.timer = None

    def callback_timer(self):
        self.time += 1
        self.start_timer()  # Restart the timer to call the callback repeatedly

    def start_timer(self):
        self.timer = Timer(0.001, self.callback_timer)  # Set interval to 1 ms
        self.timer.start()

    def stop_timer(self):
        self.timer.cancel()
        return print(f"Executed in {self.time} ms")