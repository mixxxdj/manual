This mapping allows using the VESTAX VCI-380 controller with Mixxx DJ software.
I would appreciate any feedback, suggestions for changes or improvement.

# Where to get Mixxx
Download and install Mixxx DJ sofware from [Mixx website](https://mixxx.org/)   
If you want to use Stems feature, be sure to get [Beta version 2.6](https://mixxx.org/download/#beta). Current stable version 2.5.1 doesn't have the Stems feature yet. 

# How to install the mapping
- Copy the 2 files `Vestax_VCI-380.midi.xml` and `Vestax-VCI-380-scripts.js` to the "Controllers" folder of Mixxx:

|OS|Folder location|
|---|---|
|GNU/Linux| `/home/<username>/.mixxx/controllers` |
|OS X| `/Users/<username>/Library/Containers/org.mixxx.mixxx/Data/Library/Application Support/Mixxx/controllers` |
|Windows| `C:\Users\<username>\AppData\local\Mixxx\controllers` |

- Restart Mixx
- Go to settings / controllers, find your controller and assign the mapping to it.

If it's correctly set up, all the controller lights will quickly flash on Mixxx startup.

# How to use the controller with this mapping

## Mixer functions

Main knobs and sliders work straightforward.  
Hold <kbd>SHIFT</kbd> while turning EQ knobs (<kbd>HIGH</kbd>/<kbd>MID</kbd>/<kbd>LOW</kbd>) for EQ kill mode  
Hold <kbd>SHIFT</kbd> while moving the crossfader to control output balance  

## Wheels
You can turn the wheels with our without touching the sensitive metallic part.  
Get sure that the sensibility is correctly set with <kbd>TOUCH SENSOR ADJ</kbd> knobs on the front panel: the wheels must turn red when touched, and only then. If not, the tracks will refuse to play if Mixxx thinks that a platter is touched!  
The LED rings are simulating a vinyl record spin.

|Action|Effect|
|---|---|
|Touch and turn wheels|scratching|
|Touch and turn wheels with <kbd>SHIFT</kbd>|scratching at 10X speed|
|Turn wheels without touching|temporary rate adjustments (jog)|
|Turn wheels without touching and with <kbd>SHIFT</kbd>|beatjump|
|Turn wheels with <kbd>JOG SCROLL</kbd>|library scrolling|  

## <kbd>SYNC</kbd> / <kbd>CUE</kbd> / <kbd>>||</kbd>

|Key|Function|
|---|---|
|<kbd>>/\|\|</kbd>|Play/pause|
|<kbd>SHIFT</kbd>+<kbd>>/\|\|</kbd>|Soft start / brake|
|<kbd>CUE</kbd>|go to cue point|
|<kbd>SHIFT</kbd> + <kbd>CUE</kbd>|set the cue point|
|<kbd>SYNC</kbd>|blinks on each beat. Press to adjust beatgrid position.|
|<kbd>SHIFT</kbd>+<kbd>SYNC</kbd>|activates auto-sync|
|<kbd>VINYL</kbd>|toggles slip mode|


## "Tempo" sliders (pitch)

The sliders adjust pitch  
|Action|Effect|
|---|---|
|<kbd>SHIFT</kbd> + move slider|reset speed to 1X|  
|<kbd>SHIFT</kbd> + <kbd>RANGE</kbd>|toggle keylock|  
|<kbd>RANGE</kbd>|toggle quantization|

While the pitch is different from zero, the red PAD FX LED will light up as a reminder that the deck is pitched 

## Navigation area

### Library

|Action|Effect|
|---|---|
|<kbd>SCROLL</kbd> turn|move up/down|
|<kbd>BACK</kbd> and <kbd>FWD</kbd>|move left/right|
|Left <kbd>PAD FX</kbd> turn|move up/down (equivalent to turning SCROLL)|
|<kbd>SHIFT</kbd> + Left <kbd>PAD FX</kbd> turn|page up/down|
|Right <kbd>PAD FX</kbd> turn|move left/right|
|<kbd>SHIFT</kbd> + Right <kbd>PAD FX</kbd> turn|adjust waveform zoom|
|<kbd>SHIFT</kbd> + <kbd>PAD FX</kbd> push|clone other deck|
|<kbd>AREA</kbd> or any <kbd>PAD FX</kbd> push|Default action|
|<kbd>SCROLL</kbd> push|change focus zone (<kbd>TAB</kbd>)|
|<kbd>SORT</kbd>|Sort according to active column|
|<kbd>JOGSCROLL</kbd>+<kbd>LOAD A</kbd> / <kbd>LOAD B</kbd>|Load selected track into deck A or B|
|<kbd>VIEW</kbd>|Load and play selected track on preview deck. Push again to stop.|

### End-of-track alerts

When a track is playing with less than 30 seconds remaining, the library LEDs will blink.  
For deck 1: <kbd>AREA</kbd> and <kbd>BACK</kbd>  
For deck 2: <kbd>SORT</kbd> and <kbd>FWD</kbd>  

## Quick Effects

For both decks:  
|Action|Effect|
|---|---|
|<kbd>FX SELECT</kbd> turn|Select a quick effect preset|  
|<kbd>FX SELECT</kbd> push|Reset quick effect preset selection|  
|<kbd>FX ON/OFF</kbd>|Toggle quick effect ON/OFF|
|<kbd>FX DEPTH</kbd> turn|adjust the effect parameter ("superknob")|

## Performance pads and strips

They work in different modes, according to the selection buttons on the top of the controller.
My modes are not always related to the names they bear on the controller :

The left strip is used in any mode for needle drop (quick navigate) on the preview deck
To do a needle drop on the main decks, touch the strip with <kbd>SHIFT</kbd>

### <kbd>HOT CUE</kbd> mode: HOTCUES
8 hot cues available, one per pad. The pads will light up when their hotcue is set.  
the colors of the lights will approximate the colors defined for the hot cues.  
- push a lighted pad to play the hotcue
- push a blank pad to set a new hotcue to the current position.
- push <kbd>SHIFT</kbd> + lighted pad to clear a hotcue
- loop hotcues: the pad will turn green when the loop is active, push to disable loop

### <kbd>SLICER</kbd> mode : BEAT GRID tools
The 8 pads will illuminate in sequence following the beat grid. To reset the sequence to beat 1, push the <kbd>SLICER</kbd> button again.
- Push a button of higher row: BPM tap. Tap it in rhythm to adjust the calculated BPM of the track  
- Push a button of lower row: align beatgrid. Tap it to align the beatgrid bars to the current position.    

### <kbd>AUTO LOOP</kbd>: loop mode
The green buttons on the left control loop activation.  
- upper (button 1): creates or disables a loop (beatloop_activate)  
- lower (button 5): reactivates existing loop (reloop_toggle)  

The yellow buttons control beatloop size
- left (button 3): halves the size
- right (button 4): doubles the size

The white buttons control the loop position  
- left (button 7): move left  
- right (button 8): move right  

### <kbd>ROLL</kbd>: Stems mode
If the loaded track has stems, the pads will light up in vertical pairs with the corresponding stem colors  
Stems 1 to 4, left to right  
- Push the lower button to mute/unmute the stem  
- Maintain the upper button (it will turn white) for FX control. While the button is pressed:  
   - the quick effect buttons (FX Depth, FX select and FX on/off) apply to the selected stem instead of the whole track. (see: quick effects)  
   - the parameter strip sets the individual volume of the selected stem  

### <kbd>SAMPLER</kbd> mode (<kbd>SHIFT</kbd> + <kbd>HOT CUE</kbd>)
In Sampler mode, each pad is controlling one of the samplers.  
They are mapped so the pads are organized in the same layout as the 8 samplers on mixxx default skin.  
|Color|Meaning|Pad action|<kbd>SHIFT</kbd> + pad action|
|---|---|---|---|
|OFF|no track loaded|load selected track| |
|green|a track is loaded|play|eject|
|yellow|playing|restart|stop|

