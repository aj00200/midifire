#! /usr/bin/env python3
'''
Midifire: Real-time MIDI input modification.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
'''
print('''
             [[[  Midifire
                      Realtime MIDI modification
             ]]]
''')
import argparse

VERSION = 'v0.0.0b0pre'

parser = argparse.ArgumentParser()
parser.add_argument('--license', action='store_true',
                    help='Display the Midifire license and exit')
parser.add_argument('--version', '-V', action='store_true',
                    help='Display Midifire\'s version and exit')
args = parser.parse_args()

if args.license:
    print('Midifire is licensed under the GNU GPL v3 or (at your option),')
    print('any later version. For a copy of the license, please see the')
    print('LICENSE file included with this software')
    exit()

if args.version:
    print('Midifire ', VERSION)
    exit()

if __name__ == '__main__':
    import libs.input.midi
    import libs.output.midi

    # Connect to input device
    print('[*] Creating graph from device to a virtual port')
    print('[*] Creating MIDI input device')
    indev = libs.input.midi.Input()
    print('[*] Possible ports for input:')
    print(indev.list_devices())
    indevnum = input(' Enter device number: ')
    indev.set_device(int(indevnum))

    # Create null virtual input
    virtin = libs.input.midi.VirtualInput()
    virtin.set_device(0)

    # Create virtual output device
    print('[*] Creating MIDI output device')
    virtout = libs.output.midi.VirtualOutput()
    virtout.set_device(0)

    # Link input device to virtual output device
    indev.outputs['main'] = virtout

    # Enter wait loop
    print('[*] Setup complete')
    print('    Entering wait loop')
    import time
    while True:
        time.sleep(1)
