.. meta::

   :description: Kdenlive Video Effects - RGB Splitter
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, rgb splitter, rgbsplit0r

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


RGB Splitter
============

.. figure:: /images/effects_and_compositions/effects-rgbsplit0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-rgbsplit0r-2504.webp

.. sidebar:: |kdenlive-show-video| RGB Splitter

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      rgbsplit0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter takes the red, green and blue channels in the video and separates them by a given x and y amount to produce a rainbowish effect similar to the Tik Tok logo. Compare the :doc:`/effects_and_filters/video_effects/stylize/rgba_shift` effect which essentially does the same but allows individual shifting of the RGB and Alpha channels and has the ability to determine the edge operation. Also compare the :doc:`/effects_and_filters/video_effects/stylize/chroma_shift` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Vertical Split Distance
     - Float
     - How far should layers be moved vertically from each other
   * - Horizontal Split Distance
     - Float
     - How far should layers be moved horizontally from each other
