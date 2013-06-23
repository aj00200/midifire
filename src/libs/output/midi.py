'''
Manage virtual MIDI output objects.
'''
import rtmidi
import libs.output


class Output(libs.output.Output):
    def __init__(self):
        super().__init__()
        self.midiout = rtmidi.MidiOut()

    def list_devices(self):
        '''
        Get a list of devices which this input can bind to.
        '''
        return self.midiout.get_ports()

    def set_device(self, devicenum):
        '''
        Attach this input to an actual port.
        '''
        self.midiout.open_port(devicenum)

    def process_event(self, event):
        '''
        Process an incoming MIDI event, passing it to self.midiout
        '''
        print('Output: %s' % event.data)
        self.midiout.send_message(event.data)


class VirtualOutput(libs.output.Output):
    '''
    Creates a virtual MIDI output on the system which other programs
    can connect to as if it is a normal controller.
    '''
    def __init__(self):
        super().__init__()
        self.midiout = rtmidi.MidiOut()

    def list_devices(self):
        '''
        List the option of creating a virtual device.
        '''
        return ['New Virtual Output']

    def set_device(self, devicenum):
        '''
        Create a virtual device if devicenum is zero.
        '''
        if devicenum == 0:
            self.midiout.open_virtual_port(name=b'Midifire Virtual Port')

    def process_event(self, event):
        '''
        Process an incoming MIDI event, passing it to self.midiout
        '''
        print('Virtual Output: %s' % event.data)
        self.midiout.send_message(event.data)
