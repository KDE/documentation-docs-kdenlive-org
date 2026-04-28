.. meta::
   :description: Kdenlive Documentation - Configuration Playback
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, playback, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Playback
--------

This section configures the options for playback.

.. attention:: Changing drivers can have unwanted and unexpected results and make Kdenlive unstable. Change things here only if you know what you are doing.

.. figure:: /images/getting_started/configure_playback_2604.webp
   :width: 700px
   :figwidth: 700px
   
   Configure Playback section

.. .. versionadded:: 26.04 :3: mirror monitor 

:1: :guilabel:`Play/pause monitor on mouse click`. If checked, clicking anywhere in the clip or project monitor starts or stops the playback. If unchecked, you can use the mouse to perform other operations in the monitors but need to use keyboard shortcuts to start or stop playback (e.g. J-K-L or Space).

:2: :guilabel:`Monitor full screen output`. Set to **auto** to let Kdenlive determine the best device to use. Otherwise, specify the device to be used for monitor output when switched to full screen (:kbd:`F11`).

:3: :guilabel:`Mirror monitor on fullscreen`. If checked, allows to mirror the project monitor on full-screen (only useful with at least a second monitor)

:4: :guilabel:`GPU processing (Movit library)`. This is currently disabled due to incompatibility issues between MLT (the engine Kdenlive uses for all effects/filters, transitions, and compositing) and movit (a library to enable GPU acceleration for effects etc.).

:5: :guilabel:`Audio Backend`. Select the audio backend to use for audio playback. The list of available backends depends on your :abbr:`OS (Operating System)`.

:6: :guilabel:`Audio Driver`: Select the driver to be used for audio playback. The list of available drivers depends on your :abbr:`OS (Operating System)`.

:7: :guilabel:`Audio Device`: Select the device to be used for audio playback. The list of available drivers depends on your :abbr:`OS (Operating System)`.

:8: :guilabel:`External display (Blackmagic card)`. If you have the Blackmagic DeckLink card installed you can enable it here and select the appropriate output device. Click on |view-refresh| to refresh the list of output devices.

.. rubric:: Windows
   
If you have any audio issue or playback stuttering you may change to another audio driver. The most commonly available are WinMM (Win7), Wasapi (Win10), and DirectSound.

