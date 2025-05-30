.. meta::

   :description: Kdenlive Video Effects - Levels
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, levels

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - micha (https://discuss.kde.org/u/micha)

   :license: Creative Commons License SA 4.0


Levels
======

.. figure:: /images/effects_and_compositions/effects-levels-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-levels-2504.webp

.. sidebar:: |kdenlive-show-video| Levels

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      levels
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is very useful and important for correcting color levels. This is achieved by setting the darkest areas (black level) and the brightest (white level), thus adjusting contrast. With :guilabel:`Gamma` you set the overall brightness. To assist in making the adjustments, the effect has a built-in small histogram (see the warning below).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Channel
     - Selection
     - Set the color channel you want to adjust
   * - Show histogram
     - Switch
     - Switches the built-in small histogram on and off
   * - Histogram position
     - Selection
     - Defines where the histogram is shown in the monitor
   * - Input black level
     - Percentage
     - Moves the black point to the right: all pixels with that value or less will be black. This makes the dark areas even darker, influences the mid-tones a little and the highlights not at all. Increases contrast.
   * - Input white level
     - Percentage
     - Moves the white point to the left: all pixels with that value or higher will be white. This makes bright areas even brighter, influences the mid-tones a little and the dark areas not at all. Increases contrast.
   * - Gamma
     - Percentage
     - Changes the overall brightness of the image. Affects only the mid-tones, black and white are not influenced. Default is 25%, equivalent to Gamma 1.0). Lower values (moving the bar to the left) make the image darker, higher values (moving the bar to the right) make it brighter.
   * - Black output
     - Percentage
     - Opposite of Input black level\ [1]_
   * - White output
     - Percentage
     - Opposite of Input white level\ [1]_

The following selection items are available:

:guilabel:`Channel`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Red
     - 
   * - Green
     - 
   * - Blue
     - 
   * - Luma
     - Default. :term:`Luma` adjusts the pure color channels all at the same time.

:guilabel:`Histogram position`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Top Left
     - 
   * - Top Right
     - 
   * - Bottom Left
     - 
   * - Bottom Right
     - Default

.. rst-class:: clear_both


.. rubric:: Notes
   
**Built-in Histogram**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-levels_histogram.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-levels_histogram

   Color Levels effect built-in histogram

The histogram shows the color distribution and the position of the black and white points (black and white triangles) and gamma (grey triangle). Input levels are shown above the greyscale bar; output points are shown below. Initially, the black and white triangles are all at the same position.

Recall that the black triangle shows where the black point is and how many pixels of the same brightness there are; likewise for the grey and white triangle. This example shows a typical soft exposure profile, and that you have to adjust the **Black input level** and **White input level** to improve the contrast. The rule of thumb is to move the **Black input level** to where the histogram starts; similarly, you move the **White input level** to where the histogram ends.

If needed, you adjust the overall brightness of the image by adjusting the **Gamma** value.

The triangles at the bottom, as mentioned before, determine the output values. If you move the black output level up (or to the right) it brightens the dark areas reducing the contrast and taking true black out of the image making it more bland. On the other end of the scale is the white output level. If you move it down (or left) the bright areas become darker making the image more bland, too.

As you can see, the output levels are rarely changed. However, there are situations where they come in handy:

* The final product requires a color range from 16 to 235. This can be achieved by setting the output levels accordingly.

* You want the video to have a foggy or hazy atmosphere. Fog does not have black or white, as you know, so you can use the output levels here too.

* There was a significant gamma correction in the original video which lead to shadows being drowned in black. Adjusting the black output level can help to differentiate the dark areas more subtly without completely losing black. As mentioned before, black and white output levels counteract contrast changes through the respective input levels.

.. warning::
  If you switch on the built-in histogram, any other scope widget (e.g. :ref:`view-histogram` or :ref:`view-rgb_parade`) does not work accurately anymore as it takes the histogram overlay into account, unfortunately. If you want to use the scope :term:`widgets<widget>` due to them being bigger and more versatile, simply switch off the built-in histogram.


----

.. [1] There is no point in using :guilabel:`Input white level` and :guilabel:`White output` as they eliminate each other. The same applies to :guilabel:`Black input level` and :guilabel:`Black output` even though they do not completely eliminate each other.
