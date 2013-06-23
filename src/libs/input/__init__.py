import libs.graph


class Input(libs.graph.Node):
    '''
    Parent input class.
    '''
    def __init__(self):
        self.inputs = {}
        self.outputs = {
            'main': None
        }

    def list_devices(self):
        '''
        List all supported devices which this input can use as sources.
        '''
        return []

    def set_device(self, devicenum):
        '''
        Set the device based on the index of the desired element in the
        list_devices() list.
        '''
        pass
