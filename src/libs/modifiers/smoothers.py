'''
Smooth the incomming MIDI data, removing random jitters and fast
changes. These modifiers should be configurable to work over a
specified time period.
'''
import libs.events
import libs.modifiers


class SimpleSmoother(libs.modifiers.Modifier):
    '''
    A modifier which averages the last five inputs.
    '''
    def __init__(self):
        super().__init__()
        self.memory = {}

    def process_event(self, event):
        '''
        Check self.memory to see if an event of this type has already
        occurred. If it has, average the previous inputs and move on.
        If not, create a new entry for it and move on.
        '''
        if len(event.data) != 3:
            self.process_event(event)

        if event.data[0] in self.memory:
            if event.data[1] in self.memory[event.data[0]]:
                self.memory[event.data[0]][event.data[1]].append(event.data[2])
                if len(self.memory[event.data[0]][event.data[1]]) > 5:
                    self.memory[event.data[0]][event.data[1]].pop(0)

                value_sum = 0
                total_values = 0
                for value in self.memory[event.data[0]][event.data[1]]:
                    value_sum += value
                    total_values += 1
                new = (event.data[0], event.data[1], value_sum / total_values)
                modevent = libs.events.MIDIEvent((new, event.timing))
                super().process_event(modevent)  # Pass the modified event

            else:
                self.memory[event.data[0]][event.data[1]] = [event.data[2]]
                super().process_event(event)  # Pass unmodified event

        else:
            self.memory[event.data[0]] = {event.data[1]: [event.data[2]]}
            super().process_event(event)  # Pass unmodified event
