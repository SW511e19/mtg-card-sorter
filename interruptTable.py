import datetime


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


class InterruptTable:
    task_lst = []

    def __init__(self):
        pass

    def add_task(self, _task):
        task_tuple = (_task, _task.deadline, _task.priority)
        self.task_lst.append(task_tuple)
        self.sort_task_lst()

    # insertion sort modified for task priority and tuples
    def sort_task_lst(self):
        for i in range(1, len(self.task_lst)):
            task_priority = self.task_lst[i][2]
            j = i - 1
            while j >= 0 and task_priority < self.task_lst[j][2]:
                temp = self.task_lst[j + 1]
                self.task_lst[j + 1] = self.task_lst[j]
                self.task_lst[j] = temp
                j = j - 1


def create_interrupt_table():
    return InterruptTable()