# Midifire
Midifire is a virtual MIDI device which reads data from your already existing MIDI devices and then filters or modifies the incomming MIDI data before sending it out on the virtual device. This approach allows Midifire to take a real-time approach to enhancing your controllers. For example, you could combine two controllers so that they appear as one controller, allowing you to work around limitations on the number of controllers in other software. Or, you could use outside data sources such as your keyboard or a custom-built Arduino device to modify the way your controller functions.


## Goals
Midifire allows just about any type of modification you can think of. Here is a list of ideas we want to make functional out of the box:

* Rate-limiting knobs/sliders to use exponential growth/decay functions
* Allow for certain sequences to be recorded and replayed on a loop
* Smooth shaky input from touch-surface controllers
* Switch between relative and absolute control
* Allow for some controls to be dropped (for example, some bugs exist which cause keyboard pedals to be interpreted as musical notes)
* GUI interface to provide additional options such as graphical control of the MIDI inputs and outputs as well as the applied modifiers.

## Hacking
Would you like to hack on Midifire? Please clone our repository and hack away! Midifire is licensed under the GNU GPL v3 or (at your option) any later version. If you have any questions, please feel free to contact <midifire@aj00200.org>.