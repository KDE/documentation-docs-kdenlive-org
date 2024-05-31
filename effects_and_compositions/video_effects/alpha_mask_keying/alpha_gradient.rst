.. meta::

   :description: Kdenlive Video Effects - Alpha Gradient
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha gradient

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

Alpha Gradient
==============

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-alpha_gradient.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Alpha Gradient

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      alphagrad
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Fill the alpha channel with a specified gradient (frei0r.alphagrad)\ [1]_. Its purpose is to enable, together with alpha controlled color manipulation, the use of graduated neutral-density filters similar to what one uses in photography\ [2]_.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Operation
     - Selection
     - Defines the compositing operation
   * - Position
     - Integer
     - Position where the gradient starts (range is 0-1000, default is 500)
   * - Transition width
     - Integer
     - Width of the gradient (range is 0-1000, default is 500)
   * - Tilt
     - Integer
     - Rotation of the gradient (range is 0-1000, default is 500). Values below 500 rotate counter clockwise, values above rotate clockwise. 0 means a rotation of -180 degrees, 1000 a rotation of +180 degrees.
   * - Min
     - Integer
     - Sets the density at the bottom / start of the gradient (range is 0-1000, default is 0)
   * - Max
     - Integer
     - Sets the density at the top / end of the gradient (range is 0-1000, default is 1000)

The following selection items are available:

:guilabel:`Operation`

.. list-table::
   :width: 100%
   :widths: 30 70
   :class: table-simple

   * - Write on clear
     - Overlay the image (default)
   * - Add
     - Add the existing pixel and the calculated gradient values
   * - Min
     - Take the minimum of existing pixel and calculated gradient values
   * - Max
     - Take the maximum of existing pixel and calculated gradient values
   * - Subtract
     - Subtract from the existing pixel the calculated gradient value
   

.. rubric:: Notes

In the example below a `.png` image has been overlayed to a video clip and the Alpha Gradient effect applied with its default values. You can see how the gradient darkens the video. Note the Operation **Add** to make the text opaque.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_gradient_before.webp
   :align: left
   :width: 90%
   :alt: kdenlive2304_effects-alpha_gradient_before

   Alpha Gradient effect - before


.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_gradient_after.webp
   :align: left
   :width: 90%
   :alt: kdenlive2304_effects-alpha_gradient_after

   Alpha Gradient effect - after

.. rst-class:: clear-both


----

.. |wiki_graduated_nd_filter| raw:: html

   <a href="https://en.wikipedia.org/wiki/Graduated_neutral-density_filter" target="_blank">graduated neutral-density filter</a>

.. |alphaops| raw:: html

   <a href="https://github.com/dyne/frei0r/blob/master/src/filter/alpha0ps/readme" target="_blank">frei0r alpha0ps plugins</a>

.. [1] The description of this effect has been taken in parts from the readme file for the |alphaops|. You find much more detailed information there.

.. [2] For more details about this topic refer to the Wikipedia entry about the |wiki_graduated_nd_filter|.
