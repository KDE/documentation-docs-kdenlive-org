.. meta::

   :description: Kdenlive Video Effects - White Balance (LMS)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, white balance (LMS)

   :authors: - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


White Balance (LMS)
===================

.. figure:: /images/effects_and_compositions/effects-white_balance_lms-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| White Balance (LMS)

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      colgate
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter does simple color correction, in a physically meaningful way. For more detailed about white balance see :doc:`/tips_and_tricks/how-tos/tutorial-white_balance_lms` in the :doc:`/tips_and_tricks/how-tos/index` section of the documentation.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Neutral Color
     - Picker
     - Choose the color from the source image that should be white
   * - Color Temperature
     - Integer
     - Choose an output color temperature in degrees :term:`Kelvin<kelvin>`. Default is 6,500K


.. rubric:: Notes

Color temperature is measured in degrees Kelvin. Lower values correct for "warmer" lighting, higher values correct for "cool" lighting. The default value of +6,500K is unity.
