# Sound

Works fine with recent ALSA versions (tested on Ubuntu 11.10). However
Mixxx can't deal with the 24 bit and the 192kHz sampling rate. To make
it work and to be able to use all the four channels of the soundcard you
need the following **.asoundrc** file.

In Mixx you can select "channel12" for output 1 and 2 and "channel34"
for output 3 and 4. Just remember to put the hardware switch for the
headphones on the front of the device to the right channels.

    # Makes the subdevices aka channel 1&2 and 3&4 available for alsa applications
    pcm_slave.sl12 {
        pcm "hw:AudioKontrol1,0,0"
        format S24_3BE
        channels 2
        rate 192000
    }

    pcm.channel12 {
        type plug
        slave sl12
    }

    pcm_slave.sl34 {
        pcm "hw:AudioKontrol1,0,1"
        format S24_3BE
        channels 2
        rate 192000
    }

    pcm.channel34 {
        type plug
        slave sl34
    }

    # create a virtual four-channel device with two sound devices:
    # This is in fact two interleaved stereo streams in
    # different memory locations, so JACK will complain that it
    # cannot get mmap-based access. see below.
    pcm.multi {
            type multi;
            slaves.a.pcm "hw:AudioKontrol1,0,0";
            slaves.a.channels 2;
            slaves.b.pcm "hw:AudioKontrol1,0,1";
            slaves.b.channels 2;
            bindings.0.slave a;
            bindings.0.channel 0;
            bindings.1.slave a;
            bindings.1.channel 1;
            bindings.2.slave b;
            bindings.2.channel 0;
            bindings.3.slave b;
            bindings.3.channel 1;
    }

    # JACK will be unhappy if there is no mixer to talk to, so we set
    # this to the usb card.
    ctl.multi {
            type hw;
            card AudioKontrol1;
    }

    # This creates a 4 channel interleaved pcm stream based on
    # the multi device. JACK will work with this one.
    pcm.ttable {
            type route;
            slave.pcm "multi";
            slave.channels 4;
            ttable.0.0 1;
            ttable.1.1 1;
            ttable.2.2 1;
            ttable.3.3 1;
    }
    # see above.
    ctl.ttable {
            type hw;
            card AudioKontrol1;
    }

# Hardware controls (buttons, wheel and LEDs)

## Controls

### As MIDI device

The hardware buttons can be easily used as a MIDI device and therefore
used to control Mixxx in a convenient and flexible way with the
**nicontrol** tool I've written. The tool automatically deactivates the
XInput device and maps all inputs to MIDI inputs in realtime while
controlling the LEDs to show which buttons were pressed (like the
original Windows tool of Native Instruments does). You can find an early
version of the tool on the [nicontrol
website](http://ralf-oechsner.de/opensource/page/nicontrol). An Ubuntu
package and a new version with additional features will be released
soon.

### Manually

The hardware buttons and the wheel do output linux input events and
therefore can be accessed through one of the /dev/input/event\* files.
The left button sends an 'a' key event, the middle button an 'b' key
event and the right button an 'c' key event. The wheel seems to control
the mouse (which can be very annoying) and can be accessed as a joystick
through one of the /dev/input/js\* files. To avoid sending annoying
keyboard and mouse events the controls can be deactivated with:

    xinput set-prop "Audio Kontrol 1" "Device Enabled" 0

and activated again with:

    xinput set-prop "Audio Kontrol 1" "Device Enabled" 1

## LEDs

You can manually turn on and of all the LEDs of the device with
**amixer**. You can see all the available controls that the device has
with:

    amixer -c AudioKontrol1 controls

Which should output something like:

    numid=1,iface=HWDEP,name='LED left'
    numid=2,iface=HWDEP,name='LED middle'
    numid=3,iface=HWDEP,name='LED right'
    numid=4,iface=HWDEP,name='LED ring'

You can then turn on for example the ring LED with:

    amixer -c AudioKontrol1 cset numid=4 1

and turn it of with:

    amixer -c AudioKontrol1 cset numid=4 0
