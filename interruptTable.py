import datetime
import Task


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


class InterruptTable:
    lst = []

    tuple = (Task, 5000, 42, get_time_ms())
    lst.append(tuple)
