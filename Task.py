import datetime


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


class Task:
    start = get_time_ms()
    deadline = 0
    priority = 0

    def __init__(self, start, deadline, priority):
        self.start = start
        self.deadline = deadline
        self.priority = priority

    def get_start(self):
        return self.start

    def get_deadline(self):
        return self.deadline

    def get_priority(self):
        return self.priority



    print("time in ms: ", get_time_ms())

    while True:
        if get_time_ms() >= start + deadline:
            print("deadline over")
            break;
        else:
            time = get_time_ms()
            print("updated time")