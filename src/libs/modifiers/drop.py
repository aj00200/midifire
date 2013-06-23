'''
Drop specific commands from a MIDI device. This might be useful if
software or hardware bugs cause a particular signal to have an
unexpected result (as the foot-pedals on some keyboard do).
'''
import libs.modifiers


class DropAll(libs.modifiers.Modifier):
    def process_event(self, event):
        '''
        Drop all incomming events instead of passing them on to other
        nodes in the graph.
        '''
        pass
