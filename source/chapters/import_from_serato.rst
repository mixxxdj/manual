.. _import-serato-metadata:

Importing metadata from Serato
*************

.. sectionauthor::
   Ukpai Ugochi <outreachy applicant>

Serato produces DJ softwares used for digital music mixing as well as digital vinyl record
mixing for DVS records. While Serato is neither open source or customizable, It is possible 
to use Mixxx and still have your tracks and cues imported from Serato into Mixxx.

Switching to Mixxx gives you more flexibility in terms of customization. To think that Mixxx is 
absolutely open source (free), should prompt your transition from Serato to Mixxx.
Although switching from Serato to Mixxx is a lot of work, you can import metadata 
from Serato to Mixxx effortlessly.


Import your Serato library in Mixxx
===================================

From Mixxx 2.3, tracks from your Serato library can now be imported into Mixxx library
table.

Tracks can also be loaded into deck without needing to add the music directory
in the preferences. This means that all music that has been added to Serato DJ Pro can now 
be loaded into Mixxx deck with ease.

**Set-up**

Your crates in Serato DJ Pro can also be imported into Mixxx. This feature exhibits Mixxx 
customization, as your favourite music collection are imported and arranged as they were.

**Set-up**

You can also import your Serato library into Mixxx that are in USB drives for a portable 
Serato library.
**Set-up**

Import your Beatgrid and Hotcues
================================

Track cue points are saved in special file tags as well as the track metadata. You can
now import your track cue points and all of it's metadata from Serato to Mixxx.

Once you import your Serato library into Mixxx and load a track for the first time 
from any of the methods above, the positions, labels and colors of your hotcues, other 
metadatas and beatgrid are automatically imported.

If you have already added a track to your Mixxx library before support for reading Serato's hotcues 
was added, you can reimport metadata from Serato via the track context menu.
This action will clear your existing cuepoints in Mixxx if the track has any Serato hotcues.

Decodes may slightly detect different track start and end times for files from different sources, this
could possibly be because of the presence of countless encoders and decoders for MP3 and M4A/AAC.
This problem may cause your cues to be shifted up by a few milliseconds. 
While we are working very hard to mitigate this problem, we have added a way to shift all cues for a 
track at once. With this method, it possible to fix the cue positions if Mixxx fails to determine 
the correct offsets.

Import Loops from Serato
========================

From Mixxx 2.3, saved loops from Serato can be imported. Proper support for importing and restoring 
saved loops from Serato is scheduled for Mixxx 2.4. 

For now, we just import these loops into the Mixxx database and allows using their start position 
as regular hotcues. With this in place, you can start using your loops once Mixxx 2.4 is out and
avoid reimporting track meta data.

Imports not currently supported
===============================

Support for importing track overview waveform image stored in Serato into Mixxx has not been 
provided in Mixxx 2.3. Serato flip macros cannot be imported either because flip does not offer
that kind of functionality yet.

Currently, you cannot write cues from Mixxx into Serato metadata tags. We are working hard to 
implemment support for exporting Serato metadata tags in upcoming Mixxx versions, stay tunned.