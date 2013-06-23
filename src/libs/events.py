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
        self.timing = data[0]