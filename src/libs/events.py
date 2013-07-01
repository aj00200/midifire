'''
Events which can be passed though the connection graph.
'''


class Event():
    '''
    Base event class.
    '''
    pass


class MIDIEvent(Event):
    '''
    MIDI Event
    '''
    def __init__(self, data):
        self.data = data[0]
        self.timing = data[1]


class TimeEvent(Event):
    '''
    An event sent on a regular schedule.
    '''
    def __init__(self, delay):
        '''
        @param delay: the delay schedule (time between each event
        '''
        self.delay = delay