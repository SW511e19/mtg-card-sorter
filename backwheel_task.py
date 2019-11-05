import threading
import datetime
import task


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


# Used to control the card-deck wheel
class BackwheelTask(task.Task):

    def __init__(self, deadline, priority):
        super().__init__(deadline, priority)

    def start_task(self):
        self.start_time = get_time_ms
        threading.Thread.start(self)


def create_backwheel_task(deadline, priority):
    return BackwheelTask(deadline, priority)