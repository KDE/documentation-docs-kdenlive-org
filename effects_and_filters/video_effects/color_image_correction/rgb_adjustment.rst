.. meta::

   :description: Kdenlive Video Effects - RGB Adjustment
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, rgb adjustment

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Marko (https://userbase.kde.org/User:Marko)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


RGB Adjustment
==============

.. figure:: /images/effects_and_compositions/effects-rgb_adjustment-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| RGB Adjustment

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      coloradj_RGB
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This filter is for simple manual color adjustment by RGB channel, either through adding constants, or changing the channel :term:`gammas<gamma>` or gains.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Action
     - Selection
     - Set the action to be performed\ [1]_
   * - Keep luma
     - Switch
     - Set to keep the luma value and the R/G/B sliders only affect the respective color channel
   * - Alpha controlled
     - Switch
     - Check this if only areas with non-zero alpha are to be affected
   * - Luma formula
     - Selection
     - Set the color space to operate in
   * - Red / Green / Blue
     - Integer
     - Determines the change in each of the three color channels

The following selection items are available:

:guilabel:`Action`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Add constant
     - Adds a fixed value between -150 and +150 (this is sometimes called "black level" or "setup").
   * - 
     - Simply shifts the RGB "cube" :term:`color space`. This means, that on one end we are left with empty space, which is filled with zeros, and on the other end, values can "fall outside", and in this case they will be truncated to max (255).
   * - Change gamma
     - Changes channel gamma between 0.3333 and 3.0.
   * - 
     - Keeps the whole cube in the same place, just stretches and squeezes its interior, so no zero filling or truncation is necessary.
   * - Multiply
     - Multiplies channel with a value between 0.3333 and 3.0 (sometimes called "gain" or "contrast")
   * - 
     - Changes the size of the cube, keeping the "black" corner fixed, affecting predominately highlights, but the other end can still "fall out" and get 255 truncated.

:guilabel:`Luma formula`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Rec. 709
     - Default
   * - Rec. 601
     - 


.. rst-class:: clear-both


----

.. [1] To apply more than one action, use stacked instances of the effect. Note that Kdenlive executes the stack from top down so sequence is important.


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
      :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
      :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
      :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
      :class: no-scaled-link
