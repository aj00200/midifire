import libs.graph


class Output(libs.graph.Node):
    '''
    Parent output class.
    '''
    def __init__(self):
        self.inputs = {
            'main': None
        }
        self.outputs = {}

    def list_devices(self):
        '''
        List all supported devices which this output can work with.
        '''
        return []

    def set_device(self, devicenum):
        '''
        Set the device based on the index of the desired element in the
        list_devices() list.
        '''
        pass

    def process_event(self, event):
        '''
        Process an incoming event.
        '''
        pass
