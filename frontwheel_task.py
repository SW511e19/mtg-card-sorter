import threading
import datetime
import Task


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


# Used to control the single-card wheel
class FrontwheelTask(Task.Task):

    def __init__(self, deadline, priority):
        super().__init__(deadline, priority)

    def start_task(self):
        self.start_time = get_time_ms
        threading.Thread.start(self)


def create_frontwheel_task(deadline, priority):
    return FrontwheelTask(deadline, priority)