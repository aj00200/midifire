'''
Merge different signals together, running them though the same
modifiers and sending them to the same output. This might be useful if
separate MIDI devices are expected to interact. For example, one device
might have a switch which can be configured to enable or disable a
second device.
'''
import libs.modifiers


class SimpleMerge(libs.modifiers.Modifier):
    '''
    Merge multiple event streams into one.
    '''
    def __init__(self):
        self.inputs = {
            'merge': []
        }
        self.outputs = {
            'main': None
        }
