.. meta::

   :description: Kdenlive Video Effects - Fade out
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, fade out, fade to black

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Fade Out
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-fade_out.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-fade_out

.. sidebar:: |kdenlive-show-video| Fade Out

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      brightness
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter fades out the source similar to the :ref:`wipe` transition. A checkbox switches to fade to black. It used to be called "Fade to Black".

This effect does not have keyframes but a slider controlling the duration of the fade.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Duration
     - Slider
     - Set the duration via the slider or the time code (using the format hh:mm:ss:ff)
   * - Fade to black
     - Switch
     - If checked, fades out the source to black. Default is **off**


.. hint:: 
   Since version 17.04 you can add the **Fade Out** effect with a single click using the fade handles (see screenshot below). And you can adjust the length of the fade with a drag of the mouse. Move the mouse over a selected clip in the timeline and click on the red dot in the top corner at the end of the clip. That creates a default fade-out of 3 seconds. In order to adjust the duration of the fade-out you can drag the red dot or use the :guilabel:`Duration` slider in the **Fade Out** effect panel in the clip's effect stack.

.. image:: /images/effects_and_compositions/kdenlive2304_effects-fade_in_out_dots.webp
   :align: left
   :alt: kdenlive2304_effects-fade_in

.. image:: /images/effects_and_compositions/kdenlive2304_effects-fade_out_dot.webp
   :alt: kdenlive2304_effects-fade_in
