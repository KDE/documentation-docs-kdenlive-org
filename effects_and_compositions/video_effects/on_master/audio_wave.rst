.. meta::

   :description: Do your first steps with Kdenlive video editor, using the audio wave effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, audio wave

.. metadata-placeholder

   :authors: - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-audio_wave:

Audio Wave
==========

This effect/filter is an audio visualization effect that displays the audio waveform instead of the video.

.. versionchanged:: 17.04 Up until that version, the effect was in the effects category :ref:`effects-utility`.

.. .. image:: /images/Kdenlive_Audio_wave.png

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_wave.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_wave

   Audio Wave effect

..

.. The way the effect works seems to have changed profoundly. Hence the below is no longer valid. Shall we keep this for reference for (much) older versions of Kdenlive?

.. Overlaying the Wave
   -------------------

   This effect replaces the video. If you want the effect overlaying the video you can do something like shown below.

.. .. image:: /images/Kdenlive_Audio_wave_overlayed.png

   Duplicate the video track on a track below the one with the Audio wave on it.

   Add a composite transition.

   On the top video track (the one with the audio wave effect) add a :ref:`effects-chroma_key_advanced` effect.

   Make the color you are selecting black and check the invert selection.

.. rst-class:: clear-both


.. warning:: This effect will overlay over everything.


**Example**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_wave_example.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_wave_example

   Example of the Audio Wave effect

..
