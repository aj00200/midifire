'''
Map for Stanton controllers such as the SCS3d
'''
import libs.maps


class SCS3d(libs.maps.Map):
    def __init__(self):
        super().__init__()
        self.outputs = {
            'gain': [],
            'pitch': [],
            'vinyl_ring': [],
            'vinyl_middle': [],
            'buttons': {
                'fx': [],
                'loop': [],
                'vinyl': [],
                'eq': [],
                'trig': [],
                'deck': [],
                'topleft': [],
                'topright': [],
                'bottomleft': [],
                'bottomright': [],
                'play': [],
                'cue': [],
                'sync': [],
                'tap': []
            }
        }

    def process_event(self, event):
        if event.data[0] == 176:  # Variable controls
            if event.data[1] == 1 or event.data[1] == 2:  # Vinyl middle
                self._forward_event(self.outputs['vinyl_middle'], event)
            elif event.data[1] == 3 or event.data[1] == 4:  # Ptich slider
                self._forward_event(self.outputs['pitch'], event)
            elif event.data[1] == 7 or event.data[1] == 8:  # Gain slider
                self._forward_event(self.outputs['gain'], event)
            elif event.data[1] == 98 or event.data[1] == 99:  # Vinyl ring
                self._forward_event(self.outputs['vinyl_ring'], event)

        elif event.data[0] == 144 or event.data[0] == 128:  # Press/release
            if event.data[1] == 1:  # Vinyl middle
                self._forward_event(self.outputs['vinyl_middle'], event)
            elif event.data[1] == 32:  # Fx button
                self._forward_event(self.outputs['buttons']['fx'], event)
            elif event.data[1] == 34:  # Loop button
                self._forward_event(self.outputs['buttons']['loop'], event)
            elif event.data[1] == 36:  # Vinyl button
                self._forward_event(self.outputs['buttons']['vinyl'], event)
            elif event.data[1] == 38:  # Eq button
                self._forward_event(self.outputs['buttons']['eq'], event)
            elif event.data[1] == 40:  # Trig button
                self._forward_event(self.outputs['buttons']['trig'], event)
            elif event.data[1] == 42:  # Deck button:
                self._forward_event(self.outputs['buttons']['deck'], event)
            elif event.data[1] == 98:  # Vinyl ring
                self._forward_event(self.outputs['vinyl_ring'], event)

    def _forward_event(self, outputs, event):
        for output in outputs:
            output.process_event(event)
