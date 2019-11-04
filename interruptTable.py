import datetime
import Task


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


class InterruptTable:
    task_lst = []
    task = Task.make_task(5000, 42)

    tuple = (task, task.deadline, task.priority)
    task_lst.append(tuple)

    def add_task(self, task):
        self.task_lst.append(task)