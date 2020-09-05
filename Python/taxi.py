
import collections
import queue
Event = collections.namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time=0):
    """每次改变状态时创建事件，把控制权让给仿真器"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')

    # 出租车进程结束 ➐


def compute_duration(string):
    cas = {
        'leave garage': 3,
        'pick up passenger': 1,
        'drop off passenger': 2,
        'going home': 4
    }
    return cas[string]


class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """排定并显示事件，直到时间结束"""
        # 排定各辆出租车的第一个事件
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
            # 这个仿真系统的主循环
        sim_time = 0
        while sim_time < end_time:

            if self.events.empty():

                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * ' ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


taxis = {0: taxi_process(ident=0, trips=23, start_time=0),
         1: taxi_process(ident=1, trips=4, start_time=5),
         2: taxi_process(ident=2, trips=6, start_time=10)}
sim = Simulator(taxis)
sim.run(1000)
