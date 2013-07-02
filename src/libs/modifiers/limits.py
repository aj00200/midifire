'''
Limit inputs to minimum/maximum ranges.
'''
import time
import libs.events
import libs.modifiers


class BasicLimit(libs.modifiers.Modifier):
    minimum = 10
    maximum = 120

    def process_event(self, event):
        if len(event.data) < 3:
            super().process_event(event)
            return

        val = event.data[2]
        newev = None

        if val > self.maximum:
            val = self.maximum
            new = (event.data[0], event.data[1], val)
            newev = libs.events.MIDIEvent((new, event.timing))
        elif val < self.minimum:
            val = self.minimum
            new = (event.data[0], event.data[1], val)
            newev = libs.events.MIDIEvent((new, event.timing))

        if newev:
            super().process_event(newev)
        else:
            super().process_event(event)


class SpeedLimiter(libs.modifiers.Modifier):
    '''
    Limit the speed at which a control is changed.
    Note: this might need some work to function with analog controls
    '''
    max_speed = 2  # Maximum unit change per second

    def __init__(self):
        super().__init__()
        self.memory = {}

    def process_event(self, event):
        if len(event.data) < 3:
            super().process_event(event)
            return

        now = time.time()

        # TODO: review if the first dict is necessary given the MIDI protocol
        newev = (now, event.data[2])
        if event.data[0] in self.memory:
            if event.data[1] in self.memory[event.data[0]]:
                lastev = self.memory[event.data[0]][event.data[1]]
                dt = now - lastev[0]
                print('dt  : %s' % dt)
                dvdt = (event.data[2] - lastev[1]) / dt
                print('dvdt: %s' % dvdt)
                if abs(dvdt) > self.max_speed:
                    if dvdt > 0:
                        val = lastev[1] + self.max_speed * dt
                    else:
                        val = lastev[1] - self.max_speed * dt
                    new = (event.data[0], event.data[1], val)
                    event = libs.events.MIDIEvent((new, event.timing))

                self.memory[event.data[0]][event.data[1]] = newev
                super().process_event(event)

            else:
                self.memory[event.data[0]][event.data[1]] = newev
                super().process_event(event)

        else:
            self.memory[event.data[0]] = {event.data[1]: newev}
            super().process_event(event)
