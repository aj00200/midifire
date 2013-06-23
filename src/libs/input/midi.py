'''
Manage input from MIDI devices.
'''
import rtmidi
import libs.input
import libs.events


class Input(libs.input.Input):
    def __init__(self):
        super().__init__()
        self.midiin = rtmidi.MidiIn()

    def callback(self, event, unknown):
        '''
        Callback for rtmidi.MidiIn events.
        '''
        event = libs.events.MIDIEvent(event)
        print('Input: %s' % event.data)

        # Forward the event to outputs
        self.process_event(event)

    def list_devices(self):
        '''
        Get a list of devices which this input can bind to.
        '''
        return self.midiin.get_ports()

    def set_device(self, devicenum):
        '''
        Attach this input to an actual port.
        '''
        self.midiin.open_port(devicenum)
        self.midiin.set_callback(self.callback)


class VirtualInput(libs.input.Input):
    '''
    Creates a virtual MIDI input on the system which other programs
    can connect to as if it is a normal controller.
    '''
    def __init__(self):
        super().__init__()
        self.midiin = rtmidi.MidiIn()

    def callback(self, event, unknown):
        '''
        Callback for rtmidi.MidiIn events.
        '''
        event = libs.events.MIDIEvent(event)
        print('Virtual Input: %s' % event.data)

        # Forward the event to outputs
        self.process_event(event)

    def list_devices(self):
        '''
        List the option of creating a virtual input device.
        '''
        return ['New Virtual Input']

    def set_device(self, devicenum):
        '''
        Create a virtual device if devicenum is zero.
        '''
        if devicenum == 0:
            self.midiin.open_virtual_port(name=b'Midifire Virtual Port')
            self.midiin.set_callback(self.callback)
