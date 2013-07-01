'''
Limit inputs to minimum/maximum ranges.
'''
import libs.events
import libs.modifiers


class BasicLimit(libs.modifiers.Modifier):
    minimum = 10
    maximum = 120

    def process_event(self, event):
        if len(event.data) < 3:
            super().process_event(event)
            return

        val = event.data[2]
        newev = None

        if val > self.maximum:
            val = self.maximum
            new = (event.data[0], event.data[1], val)
            newev = libs.events.MIDIEvent((new, event.timing))
        elif val < self.minimum:
            val = self.minimum
            new = (event.data[0], event.data[1], val)
            newev = libs.events.MIDIEvent((new, event.timing))

        if newev:
            super().process_event(newev)
        else:
            super().process_event(event)
