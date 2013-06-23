import libs.graph


class Modifier(libs.graph.Node):
    '''
    Parent modifier class for all modifier code in Midifire.
    '''
    def __init__(self):
        self.inputs = {}
        self.outputs = {}


class MIDIModifier(Modifier):
    '''
    A parent class for modifiers which work on MIDI signals.
    '''
    pass
