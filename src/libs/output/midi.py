'''
Manage virtual MIDI output objects.
'''
import rtmidi
import libs.output


class Output(libs.output.Output):
    def __init__(self):
        self.inputs = {
            'main': None
        }
        self.outputs = {}
        self.midiout = rtmidi.MidiOut()

    def callback(self, event):
        '''
        Callback for rtmidi.MidiIn events.
        '''

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
        Process an incomming MIDI event, passing it to self.midiout
        '''
        print('Output: %s' % event.data)
        self.midiout.send_message(event.data)
