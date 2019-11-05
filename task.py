import datetime
import threading


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


# super class for all task classes
class Task(threading.Thread):
    start_time = 0
    is_running = False

    def __init__(self, deadline, priority):
        threading.Thread.__init__(self)
        self.deadline = deadline
        self.priority = priority

    def start_task(self):
        self.start_time = get_time_ms
        self.is_running = True
        threading.Thread.start(self)

    # TODO add error case
    def update_running_state(self, boolean):
        if boolean is bool:
            self.is_running = boolean

    # temp method for testing deadline time
    def method_time_test(self):
        print("time in ms: ", get_time_ms())
        while True:
            if get_time_ms() >= self.start_time + self.deadline:
                print("deadline over")
                break
            else:
                time = get_time_ms()
                print("updated time")


def make_task(deadline, priority):
    return Task(deadline, priority)