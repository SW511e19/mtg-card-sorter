import datetime
import threading


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


class Task(threading.Thread):
    start_time = 0

    def __init__(self, deadline, priority):
        threading.Thread.__init__(self)
        self.deadline = deadline
        self.priority = priority

    def start_task(self):
        self.start_time = get_time_ms
        threading.Thread.start(self)

    def method_time_test(self):
        print("time in ms: ", get_time_ms())
        while True:
            if get_time_ms() >= self.start_time + self.deadline:
                print("deadline over")
                break;
            else:
                time = get_time_ms()
                print("updated time")

def make_task(deadline, priority):
    task = Task(deadline, priority)
    return task