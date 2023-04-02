.. include:: /shortcuts.rstext

.. _appendix-command-line-options:

Launching Mixxx from the Command Line
=====================================
To launch Mixxx using the command line:

**Windows**
  Locate the folder where Mixxx is installed and copy the file path. You can also obtain the file path by right clicking on the Mixxx icon and then choosing 'Properties'.
  Copy the path and paste it in terminal and add ``\mixxx`` at the end - everything should be inside quotes. Press Enter. The entire command will look like this ::

    "C:\Program Files\Mixxx\mixxx"

**macOS**
  Similarly, for macOS, the command will be ::

    /Applications/Mixxx.app/Contents/MacOS/mixxx

**GNU/ Linux**
  If Mixxx is in your system's search path (``$PATH``), you can just type ::

   mixxx

Command line options
--------------------

Mixxx is designed to be as user-friendly as possible. As such, its command line
options are only useful for development or debugging, as they make these tasks
easier. Command line options are case-sensitive.

To launch Mixxx with any of these command line options, simply append the option to the base command for your operating system. For example, to launch Mixxx in developer mode on Windows, type this in terminal ::

  "C:\Program Files\Mixxx\mixxx" --developer

In addition to these options, it is possible to specify one or more music
file(s) on the command line. These will be loaded at start-up.  Each file you
specify will be loaded into the next virtual deck. For a list of supported file
types, go to :ref:`file-format-compatibility`.



--resourcePath PATH     Top-level directory where Mixxx will look for
                        its resource files such as MIDI mappings,
                        overriding the default installation location.
--settingsPath PATH     Top-level directory where Mixxx will look for
                        user settings files such as the library database
                        and preferences configuration file.
--controllerDebug       Log all controller data Mixxx sends and receives
                        as well as scripts it loads.
--developer             Enable developer mode. Includes extra logs, stats
                        on performance and the Developer tools menu as
                        well as tooltips and logs useful for skin
                        developers.
--safeMode              Disable OpenGL widgets (scrolling waveforms,
                        spinnies) to work around GPU driver bugs.
                        If Mixxx is crashing on startup, try using this.

                        * Automatically loads empty waveforms
                        * Disables spinning vinyl widgets
                        * Disables synchronization polling
                        * Doesn't open controllers by default
--locale LOCALE         Use a custom locale for loading translations
                        (e.g ``fr``)
-f, --fullScreen        Start Mixxx in full-screen mode.
--logLevel LEVEL        Set the verbosity of command line logging.

                        ============  ==========================
                        Value         Meaning
                        ============  ==========================
                        ``critical``  Critical/Fatal only
                        ``warning``   Above + Warnings
                        ``info``      Above + Informational messages
                        ``debug``     Above + Debug/Developer messages
                        ``trace``     Above + Profiling messages
                        ============  ==========================
--logFlushLevel LEVEL   Set the logging level at which the log buffer
                        is flushed to ``mixxx.log``.
                        ``LEVEL`` is one of the values defined at ``--logLevel``
                        above.
--debugAssertBreak      Breaks (``SIGINT``) Mixxx if a ``DEBUG_ASSERT`` evaluates
                        to false. A debugger can then be used to continue.
                        This disables the ``MIXXX_DEBUG_ASSERTIONS_FATAL``
                        flag which can otherwise lead to a time consuming
                        full rebuild.
-h, --help              Display this help message and exit

Developer tools
===============

To start Mixxx in Developer mode with a custom resource directory with
:term:`MIDI` and :term:`HID` logging enabled, type the following line into the
terminal and hit return: ::

  ./mixxx --controllerDebug --developer --resourcePath res


Experiment modes for rapid development and testing
---------------------------------------------------

  * Adds a static Experiment class with a tri-state mode flag that indicates
    whether the experiment mode is OFF, BASE, or EXPERIMENT.

  * Adds :menuselection:`Developer --> Stats:Experiment Bucket` and
    :menuselection:`Developer --> Stats:Base Bucket`. Each one toggles between
    OFF and BASE/EXPERIMENT so you can choose exactly what time spans you would
    like to collect in your base and experiment buckets.

  * Updates StatsManager to segment collected stats into a base and experiment
    bucket. This allows you to quickly measure the difference a code change has
    on relevant counters / timers within the same execution of Mixxx.

This is useful for quickly enabling and disabling a code change without
a re-compile/re-run cycle to get an anecdotal sense of how it "feels" as
well as a quantified sense of how it differs in terms of stats Mixxx
collects.

All stats collected via the usual Counter/Timer/ScopedTimer/etc. tools
are segmented into a BASE STATS and EXPERIMENT STATS section printed to
the log on exit.
