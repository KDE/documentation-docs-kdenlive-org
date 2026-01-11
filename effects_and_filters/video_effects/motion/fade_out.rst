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
             - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 24.08
..     easing method added


Fade Out
========

.. figure:: /images/effects_and_compositions/effects-fade_out-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
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

This effect/filter fades out the source similar to the :doc:`Wipe </compositing/transitions/wipe>` transition. A checkbox switches to fade from black. It used to be called "Fade to Black".

This effect does not have keyframes but a slider controlling the duration of the fade.

The applied easing method curve is shown on the clips fade.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 20 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Duration
     - Slider
     - Set the duration via the slider or the time code (using the format :abbr:`hh:mm:ss:ff(hours:minutes:seconds:frames)`)
   * - Fade to black
     - Switch
     - If checked, fades in the source to black. Default is **off**
   * - Easing Method
     - Selection
     - See below

The following selection values are available:

:guilabel:`Fade to black`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Linear
     - Add a linear fade
   * - Cubic in
     - Add a cubic-in fade
   * - Exponential in
     - Add an exponential-in fade
   * - Cubic out
     - Add a Cubic-out fade
   * - Exponential out
     - Add an exponential-out fade


.. hint:: 
   Since version 17.04 you can add the **Fade Out** effect with a single click using the fade handles (see screenshot below). And you can adjust the length of the fade with a drag of the mouse. Move the mouse over a selected clip in the timeline and click on the red dot in the top corner at the end of the clip. That creates a default fade-out of 3 seconds. In order to adjust the duration of the fade-out you can drag the red dot or use the :guilabel:`Duration` slider in the **Fade Out** effect panel in the clip's effect stack.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-fade_in_out_dots.webp
   :align: left
   
.. figure:: /images/effects_and_compositions/kdenlive2304_effects-fade_out_dot.webp
   