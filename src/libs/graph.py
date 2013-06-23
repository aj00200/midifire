'''
Base code for creating the connection graph.
'''


class Node():
    '''
    Parent node to all graph elements defining basic actions such as a
    default process_event method which simply forwards the events
    without changing them.
    '''
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

    def process_event(self, event):
        '''
        Process an incoming event. The default action is to simply
        forward the event unless this action is overridden by a
        subclass.
        '''
        for output_channel in self.outputs:
            if isinstance(self.outputs[output_channel], list):
                for output in self.outputs[output_channel]:
                    output.process_event(event)
            elif isinstance(self.outputs[output_channel], Node):
                self.outputs[output_channel].process_event(event)

            # If neither of these conditions are met, there is not a supported
            #  output attached and the message is simply dropped.
