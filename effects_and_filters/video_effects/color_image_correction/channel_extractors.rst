.. meta::

   :description: Kdenlive Video Effects - Channel Extractor
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, channel extractor red, channel extractor green, channel extractor blue

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Channel Extractor BLUE / GREEN / RED
====================================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-channel_extractor_RGB.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Channel Extractor B / G / R

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      B / G / R
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

These three separate effects extract the respective color channels from the clip. There are no further parameters or keyframes.

These filters essentially isolate the individual color channels (red, green, blue) from the clip and generate a greyscale image where the intensity represents the specific color channel. The result can be used for color analysis (understanding the distribution of colors in the clip), further image processing (using the greyscale as a mask), or segmentation (separating objects based on their color characteristics).

You typically put the same clip in three adjacent tracks in the timeline, add the effect to each clip (one for RED, one for GREEN, and for one BLUE), and then add additional effects to create the desired (artistic) look.

.. figure:: /images/effects_and_compositions/effects-channel_extractor_RGB_timeline-2504.webp
   :width: 400px
   :figwidth: 400px
   :align: left

   Example of bringing a clip back together after using Channel Extractor

In order to bring the channels back together, use either the :kbd:`Addition` composition or the :kbd:`Cairo blend` composition with :kbd:`Composition Type` **Add** between the two top tracks, and one added to the bottom track.

.. rst-class:: clear-both


.. rubric:: Screenshots

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-channel_extractor.webp
   :width: 400px
   :figwidth: 400px
   :align: left

   Original clip before


.. figure:: /images/effects_and_compositions/kdenlive2304_effects-channel_extractor_RED.webp
   :width: 400px
   :figwidth: 400px
   :align: left

   Result of Channel Extractor RED


.. figure:: /images/effects_and_compositions/kdenlive2304_effects-channel_extractor_GREEN.webp
   :width: 400px
   :figwidth: 400px
   :align: left

   Result of Channel Extractor GREEN


.. figure:: /images/effects_and_compositions/kdenlive2304_effects-channel_extractor_BLUE.webp
   :width: 400px
   :figwidth: 400px
   :align: left

   Result of Channel Extractor BLUE
