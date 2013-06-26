import libs.graph


class Map(libs.graph.Node):
    '''
    Parent class for all maps. Map objects are responsible for taking
    input and separating it into human-readable control-names for
    specific controllers. For example, it would take in input from a
    normal MIDI input and then separate it into different outputs for
    each EQ slider, button, etc.

    Maps should generally be made on a per-controller basis or generic
    maps could be created for devices which all work similarly (and
    potentially overridden to handle minor quirks in their behavior).
    '''
    def __init__(self):
        super().__init__()
        self.inputs['main'] = None
