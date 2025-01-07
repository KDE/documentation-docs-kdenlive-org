.. meta::
   :description: Kdenlive Documentation - Project Bin - Generators
   :keywords: KDE, Kdenlive, add clips, generator, counter, color bars, white noise, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan.. .. versionadded:: 17.04
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Simon Eugster <simon.eu@gmail.com>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

     
Generators
==========

As the name suggests, **Generators** generate a short video clip or still images for specific purposes. Many of you will recognize them from the good old days of bulky TV sets.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_generator.webp
      :width: 318px
      :figwidth: 318px
      :align: left
      :alt: project_bin_generator

      Using generators

   There are three generators available:
   
   `Counter`_
   
   `Color Bars`_
   
   `White Noise`_

.. rst-class:: clear-both


Counter
-------

This generates a counter timer video clip in various formats.

.. figure:: /images/project_and_asset_management/project_bin_generator_counter.png
   :align: left
   :width: 360px
   :figwidth: 360px
   :alt: project_bin_generator_counter

   Counter generator

.. rst-class:: clear-both

:guilabel:`Count up`:
   You can choose to have the clip count up by checking that option, otherwise it will count down.
   
.. .. versionadded:: 17.04

:guilabel:`No Background`:
   This option will remove the black lines and the white circles from the counter leaving only the grey background.

:guilabel:`Counter Style`:
   Choose the display style for the counter

   * Seconds to 1 (default)
   * Seconds to 0
   * Frames
   * Timecode
   * Clock

:guilabel:`Sound`:
   Choose whether and what sound to playback

   * Silent
   * 1 kHz before end
   * 1 kHz each second

:guilabel:`Drop frame timecode`:
.. .. to be documented

To change the size and position of the clip, you can add an effect to the clip on the timeline or in the project bin such as the :doc:`/effects_and_filters/video_effects/transform_distort_perspective/position_and_zoom` or the :doc:`/effects_and_filters/video_effects/transform_distort_perspective/transform`.


Color Bars
----------

.. .. versionadded:: 17.04

Generates a color test pattern of various types.

.. figure:: /images/project_and_asset_management/project_bin_generator_color_bars.gif
  :align: left
  :width: 360px
  :figwidth: 360px
  :alt: project_bin_generator_color_bars

  Color Bars generator

.. rst-class:: clear-both

:guilabel:`Bar Type`:
   
   * PAL color bars
   * PAL color bars with red
   * BBC color bars
   * EBU color bars
   * SMPTE color bars
   * Philips PM5544
   * FuBK
   * Simplified FuBK


White Noise
-----------

.. .. versionadded:: 17.04
                     audio white noise

This generates a video noise clip - like the "snow" on an out-of-tune analogue TV including the audio white noise

.. figure:: /images/project_and_asset_management/project_bin_generator_white_noise.webp
  :width: 360px
  :figwidth: 360px
  :alt: project_bin_generator_white_noise
