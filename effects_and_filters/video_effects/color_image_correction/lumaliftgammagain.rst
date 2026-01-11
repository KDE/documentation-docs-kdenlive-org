.. meta::

   :description: Kdenlive Video Effects - Luma Lift Gain Gamma
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, lumaliftgammagain, luma, lift, gamma, gain

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |color_grading_terminology| raw:: html

   <a href="http://www.digital-intermediate.co.uk/colour/colourterminology.htm" target="_blank">color grading terminology</a>


LumaLiftGainGamma
=================

.. figure:: /images/effects_and_compositions/effects-lumaliftgaingamma-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| LumaLiftGainGamma

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      lumaliftgaingamma
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter can be used to apply lift, gain and :term:`gamma` correction to :term:`luma` values of the source image.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Lift
     - Integer
     - Adjusts the darker areas
   * - Gain
     - Integer
     - Adjusts the brighter areas
   * - Gamma
     - Integer
     - Adjusts the midtone areas


.. rubric:: Notes

There is good section of |color_grading_terminology| available at the digital-intermediate.co.uk site.
