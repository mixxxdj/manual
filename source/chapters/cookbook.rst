.. include:: /shortcuts.rstext

.. _cookbook:

Cookbook (Examples)
*******************

The Cookbook is here to give Mixxx users examples to work off of. The recipes both cover common or interesting use cases, and progressively explain more complex detail. This chapter moves beyond simple introductory examples and demonstrates concepts that will help users create awesome music, as well as the approach to achieving this.
Each recipe will focus on one specific aspect of Mixxx, combining different features in interesting ways to fully explore its niche.

Deck Cloning
============

When deck cloning (also called "instant doubles" in some other DJ software) is activated, the currently loaded song, playback state, pitch adjustment, and any playing loop will be cloned from one deck to another. This opens up a number of creative mixing possibilities, some of which we will explore below.

.. image:: ../_static/deckclone.gif
    :align: center

How to use deck cloning
-----------------------
Deck cloning can be triggered several different ways:

* Double press the :guilabel:`Load` button on your controller, mixer, or keyboard (this can be disabled in the Decks page of the preferences)
* Invoke the :guilabel:`CloneFromDeck` control in a controller mapping (see the complete :ref:`Mixxx controls table <advanced-mixxxcontrols>`)
* Drag and drop a track from one deck to another in the UI

Any of these actions will result in the currently loaded track being loaded on the target deck at the current play position and pitch setting. If the track is playing on the source deck, it will play from the same exact position on the target deck.

What you can do with deck cloning
---------------------------------

Playing with a single turntable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In a typical DJ setup, you have two decks and a mixer, but with the deck clone feature, it's possible to play with a single deck. You can :term:`cue point <cue>`, beatmatch, and mix in the next track on a single deck. Once the track is mixed in, swap it to another channel using the deck clone feature, freeing up your single deck for the next track. This is useful if you are building out a DVS setup, but you only have one turntable so far or if you need to play with a minimal setup. For example, you may not have enough space for two decks or you might want to reduce the amount of gear you have to lug around. Finally, this method can be used as a backup way to keep playing if one of your turntables malfunctions.

Beat juggling
~~~~~~~~~~~~~
Beat juggling is a technique in which a DJ creates various loops and patterns by playing the same track on two decks. In its simplest, four or eight bars of a track are played on one deck (typically a drum-only break), while on the other deck, the same track is cued up to the start of the same section. When the desired section ends on the first deck, the second deck is started and the :ref:`crossfader <interface-crossfader>` is switched to play that deck. This process can be repeated as many times as desired, back and forth between the two decks, playing a tidy drum loop.

Historically, this technique required two copies of the same record, but using the deck clone feature, the currently playing track can quickly be cued on a second deck in the right spot at the correct tempo. In modern times, with digital DJ setups, many beat jugging techniques can be done on a single deck using loops and hotcues. Still, when done using traditional methods, beat juggling is creative and impressive.

Put your best hand forward
~~~~~~~~~~~~~~~~~~~~~~~~~~
Often, DJs and turntablists can only perform certain complex scratches with one hand or the other. The deck clone feature makes it easy to quickly swap which deck a song is playing on, enabling a performer to use whichever hand they prefer for scratching.

Doubles, follows and chases
~~~~~~~~~~~~~~~~~~~~~~~~~~~
In this technique, the same track is played on two decks, but on the second deck, the track is played 1/2 a beat ahead or behind. The crossfader is used to strategically switch between the two decks, creating a delay effect. This can be executed using a deck clone followed by a beat jump of 1/2 a beat on the second track (or manually nudging the track so it ends up half a beat ahead or behind).

Preview current track
~~~~~~~~~~~~~~~~~~~~~
While playing a track, sometimes it can be useful to preview an upcoming section of the song. This can be done by cloning the track that is playing to the another deck, seeking ahead, and listening via the cue output in your headphones.

.. warning:: If the crossfader or deck fader currently allows hearing decks from both sides, cloning a playing deck
            will raise the main volume considerably, which may not be expected or desired.
