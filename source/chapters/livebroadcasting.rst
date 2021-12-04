.. include:: /shortcuts.rstext

.. _live-broadcasting:

Live Broadcasting - Start your own Internet radio
*************************************************

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

Live Broadcasting in Mixxx allow you to stream your mix over the Internet to
listeners around the world.

.. seealso:: The :ref:`microphones` chapter has detailed instructions for
             including input from microphones in your broadcasted mixes.

Streaming Servers
=================

**Remote streaming server**
  Mixxx allows you to feed your audio stream directly to
  :term:`Shoutcast <shoutcast>` and :term:`Icecast <icecast>` streaming servers.
  Depending on the number of listeners, streaming audio requires a significant
  amount of bandwidth. Streaming servers provide the required bandwidth and
  broadcast the stream to your listeners. A popular free streaming service is
  `Caster.fm <http://www.caster.fm>`_. A review of several free and paid stream
  hosts is available at
  `broadcastingworld.net <http://www.broadcastingworld.com/reviews/category-stream-hosting>`_.

  .. digraph:: remote_streaming
     :caption: Mixxx as client-side streaming source broadcasting to an
               remote streaming server
     :alt: Mixxx as client-side streaming source broadcasting to an
           remote streaming server

     rankdir=LR;
     size="6,6";
     StreamingServer [shape = rectangle, style=filled, fillcolor=gainsboro];
     Router [shape = box, style=dashed] ;
     node [shape = box];
     Mixxx -> Router [ label = "Lan" ];
     Router -> StreamingServer [ label = "Internet" ];
     StreamingServer -> Listener1 [ dir=left, label = "Internet" ];
     StreamingServer -> Listener2 [ dir=left, label = "Internet" ];
     StreamingServer -> Listener3 [ dir=left, label = "Internet" ];

**Local streaming server**
  For experienced users, it may be interesting to set up your own local streaming
  server. This turns your personal computer into a radio station and listeners
  connect directly to your server. Mixxx as a streaming source does not need to
  run on the same computer as your streaming server. However, professional
  stations often run the streaming source on the same computer as the streaming
  server for stability and reliability reasons. Keep in mind that if want to
  stream audio to a significant number of listeners, you'll need enough
  bandwidth. Read the
  `Shoutcast documentation <http://wiki.winamp.com/wiki/SHOUTcast_Getting_Started_Guide>`_
  or
  `Icecast documentation <http://www.icecast.org/docs/>`_ for server setup
  instructions.

  .. digraph:: local_streaming
     :caption: Mixxx as client-side streaming source broadcasting to an
               local streaming server
     :alt: Mixxx as client-side streaming source broadcasting to an
           remote streaming server

     rankdir=LR;
     size="5.5,6";
     Router [shape = box, style=dashed] ;
     StreamingServer [shape = rectangle, style=filled, fillcolor=gainsboro];
     node [shape = box];
     Mixxx -> StreamingServer [ label = "" ];
     StreamingServer -> Router [ dir=left, label = "Lan" ];
     Router -> Listener1 [ dir=left, label = "Internet" ];
     Router -> Listener2 [ dir=left, label = "Internet" ];
     Router -> Listener3 [ dir=left, label = "Internet" ];

Configuring Mixxx
=================

Start by supplying Mixxx with all information needed to establish a connection
to the streaming server:

* Open :menuselection:`Preferences --> Live Broadcasting`.
* Insert the settings following the descriptions in the
  :ref:`live-broadcasting-preferences`
* Click :guilabel:`OK`
* Go to :menuselection:`Options --> Enable Live Broadcasting` or use
  the :ref:`appendix-shortcuts` to start broadcasting.

.. _live-broadcasting-preferences:

.. figure:: ../_static/Mixxx-200-Preferences-Livebroadcasting.png
   :align: center
   :width: 75%
   :figwidth: 100%
   :alt: Mixxx preferences - Setting up live broadcasting
   :figclass: pretty-figures

   Mixxx preferences - Setting up live broadcasting

Server Connection
-----------------

* **Type**: Select the type of streaming server you want to connect with.
  :term:`Shoutcast 1<shoutcast>`, :term:`Icecast 1 <icecast>`, and
  :term:`Icecast 2<icecast>` servers are supported.

  Mixxx works with Shoutcast 2 using the Shoutcast 1 protocol if you provide a
  stream name in :menuselection:`Preferences --> Live Broadcasting -->
  Stream Settings`. If you don't provide a stream name, Shoutcast 2 rejects the
  connection (where Shoutcast 1 would accept this case).
* **Host**: You can enter the host as either a host name or an IP address.
* **Login**: As provided by your streaming server provider. Without this, you
  will not connect successfully to the server. The default login for
  *Icecast* is ``source`` while the default login for Shoutcast is ``admin``.
* **Mount**: A mount point is a unique name identifying a particular stream.
  For *Shoutcast* it is not necessary to specify a mount point. The setting must
  not be blank if you are using *Icecast*. Try the default ``/mount`` or
  ``/live``. If you haven't been given a specific mount point you can usually
  make one up. It always begins with a ``/`` (slash) followed by a text without
  any special characters in it.
* **Port**: As provided by your streaming server provider. Most servers use the
  default port 8000.
* **Password**: As provided by your streaming server provider, unless you run
  your own radio server. It is required to establish the connection to the
  server and to start the broadcast.

.. warning:: Do not enter a :term:`URL` as the host! ``http://example.com:8000``
             does not work. Use ``example.com`` in the :guilabel:`Host` field
             and ``8000`` in the :guilabel:`Port` field instead.

Stream Settings
---------------

* **Public stream**: If enabled, this option adds your radio station to the
  Shoutcast/Icecast directory.
* **Enable UTF-8 metadata**: If enabled, this option fixes broken accented and
  foreign language symbols in :term:`metadata`, assuming the streaming provider
  has configured the server to support UTF-8 metadata.
* **Dynamically update Ogg Vorbis metadata**: Due to flaws in some streaming
  clients, updating Ogg Vorbis metadata dynamically can cause listener glitches
  and disconnections. Check this box to update the metadata anyway. Some players
  that listeners can use have bugs that can cause audio glitches or
  disconnections when the Ogg Vorbis metadata is updated dynamically. If this is
  not a problem, you can enable this checkbox.
* **Stream name**: So, what's the name of your show?
* **Website**: The website you would like your listeners to visit.
* **Description**: Enter your DJ name and a short tagline.
* **Genre**: List the main genres you play. This attracts search hits on stream
  directories. Genre must not be blank.

Encoding
--------

* **Bitrate**: Selecting a :term:`bitrate` of 128 or 160 :term:`kbps` is common
  and provides sufficient quality to your listeners. Higher bitrates will use a
  larger chunk in your Internet connection bandwidth to stream and for your
  listeners to receive the stream.
* **Format**: Mixxx supports streaming to Icecast servers either in :term:`MP3`
  or :term:`Ogg Vorbis` format, streaming to Shoutcast servers is supported in
  :term:`MP3` format.

Metadata
--------

Shoutcast metadata format
^^^^^^^^^^^^^^^^^^^^^^^^^

  This allows to set custom metadata formats for the Shoutcast title field.
  Previously only ``artist - title`` was allowed. For example if you were
  broadcasting as part of a station, you could add the station's name or the
  presenter's name in the title: ``MyStation | $artist - $title``.
  Or if you were doing a live mix with several artists, you could have:
  ``Live mix by MyName - currently playing: $artist``. Or even if you wanted a
  very unusual format: ``Hey, I like $artist, here is $title by $artist``.

  The changes **do not** affect the case for the combination of OGG/Icecast2.

Custom metadata
^^^^^^^^^^^^^^^

 By default, Mixxx broadcasts artist and title information of the files that you
 play to your listeners. You can disable this feature and use your own custom
 metadata.

* **Enable custom metadata**: Toggles custom metadata on and off.
* **Artist**: Insert your custom artist metadata here, your DJ name for example.
* **Title**: Insert your custom title metadata here.

Icecast vs. Shoutcast
---------------------

Both essentially serve the same purpose. An Icecast server can stream either
:term:`MP3` or :term:`Ogg Vorbis`. However, although Ogg is more efficient and
effective (you get higher-fidelity sound than MP3 at lower data rates) not all
players can play Ogg streams. As a result MP3 is probably a safe choice unless
you know your listeners can hear an Ogg stream successfully.

Broadcast directories
---------------------

Generally your streaming server host adds your radio station to the
Shoutcast/Icecast directory, if you enable the :guilabel:`Public Stream` option
in :menuselection:`Preferences --> Live Broadcasting --> Stream Settings`.

* **Shoutcast radio directory**: `www.shoutcast.com <https://www.shoutcast.com/>`_
* **Icecast radio directory**: `dir.xiph.org <http://dir.xiph.org/>`_

Often streaming hosts will run their own directories. Check your host's FAQ to
find out. If you want to promote your streaming radio station even more,
register at services like `streamfinder.com <https://www.streamfinder.com/>`_.
An overview of different internet radio directories is available at
`shoutcheap.com <https://www.shoutcheap.com/internet-radio-directories-submitting-and-promoting/>`_

Troubleshooting
===============

* If you have trouble connecting to your streaming server, check the
  configuration in the :ref:`live-broadcasting-preferences`.
* You may have selected the :term:`Ogg Vorbis` format that is unsupported by
  Shoutcast servers.
* You may need to check your firewall settings. Both Icecast and Shoutcast use
  two ports. If you are streaming on a port (for example, port 8000) then you
  need to open up the next port (port 8001) as well.
* You may need to configure port forwarding if you are behind a router or your
  router will block requests to your streaming port (for example, port 8000)
