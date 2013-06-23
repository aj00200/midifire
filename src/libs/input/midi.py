'''
Manage input from MIDI devices.
'''
import rtmidi
import libs.input
import libs.events


class Input(libs.input.Input):
    def __init__(self):
        self.inputs = {}
        self.outputs = {
            'main': None
        }
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
