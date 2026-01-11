.. meta::

   :description: Kdenlive Video Effects - Fade in
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, fade in, fade from black

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 24.08
..     easing method added


Fade In
=======

.. figure:: /images/effects_and_compositions/effects-fade_in-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Fade In

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

This effect/filter fades in the source similar to the :doc:`Wipe </compositing/transitions/wipe>` transition. A checkbox switches to fade from black. It used to be called "Fade from Black".

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
   * - Fade from black
     - Switch
     - If checked, fades in the source from black. Default is **off**
   * - Easing Method
     - Selection
     - See below

The following selection values are available:

:guilabel:`Fade from black`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Linear
     - Add a linear fade
   * - Cubic in
     - Add a cubic in fade
   * - Exponential in
     - Add an exponential-in fade
   * - Cubic out
     - Add a Cubic out fade
   * - Exponential out
     - Add an exponential-out fade


.. hint:: 
   Since version 17.04 you can add the **Fade In** effect with a single click using the fade handles (see screenshot below). And you can adjust the length of the fade with a drag of the mouse. Move the mouse over a selected clip in the timeline and click on the green dot in the top corner at the beginning of the clip. That creates a default fade-in of 3 seconds. In order to adjust the duration of the fade-in you can drag the green dot or use the :guilabel:`Duration` slider in the **Fade In** effect panel in the clip's effect stack.

.. image:: /images/effects_and_compositions/kdenlive2304_effects-fade_in_out_dots.webp
   :align: left
   
.. image:: /images/effects_and_compositions/kdenlive2304_effects-fade_in_dot.webp
   