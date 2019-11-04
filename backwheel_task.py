import Task
import datetime


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


class Backwheel_Task(Task.Task):


    def __init__(self, deadline, priority):
        super().__init__(deadline, priority)
        self.deadline = deadline
        self.priority = priority


    self.start_time = get_time_ms()

