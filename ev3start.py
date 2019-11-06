import backwheel_task
import ev3_task
import frontwheel_task
import interruptTable
import pi_task
import piston_task

bwt = backwheel_task.create_backwheel_task(1000, 4)
fwt = frontwheel_task.create_frontwheel_task(2000, 2)
pt = piston_task.create_piston_task(3000, 3)
evt = ev3_task.create_ev3_task(4000, 5)
pit = pi_task.create_pi_task(5000, 1)

table = interruptTable.create_interrupt_table()

table.add_task(bwt)
table.add_task(fwt)
table.add_task(pt)
table.add_task(evt)
table.add_task(pit)

print(table.task_lst[0])
test = table.task_lst[0][0]
print(test)
print(test.deadline)

print(bwt)
print(bwt.deadline)