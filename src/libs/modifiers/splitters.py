'''
Split incoming events in various ways.
'''
import libs.modifiers


class Copy(libs.modifiers.Modifier):
    def __init__(self):
        self.inputs = {
            'main': None
        }
        self.outputs = {
            'copy': []
        }
