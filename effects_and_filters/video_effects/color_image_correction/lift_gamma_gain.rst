.. meta::

   :description: Kdenlive Video Effects - Lift/Gamma/Gain
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, lift/gamma/gain, lift gamma gain, lift, gamma, gain

   :authors: - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Lift/Gamma/Gain
===============

.. figure:: /images/effects_and_compositions/effects-liftgammagain-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-liftgammagain-2504.webp

.. sidebar:: |kdenlive-show-video| Lift/Gamma/Gain

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      lift_gamma_gain
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter allows you to adjust the lift (impacting mainly shadows), gain (impacting mainly highlights) and :term:`gamma` (impacting mainly midtones). The color wheel inputs allow to control the degree to which these effects apply to the R, G & B color channels. By default, the white color at the centre of the color wheel is selected, meaning the effect applies equally to all three color channels. By choosing another color on the color wheel, the effect will be applied on the R, G & B channels in proportion to the RGB components that make up that color.


.. rubric:: Notes

.. seealso::
   How-to :doc:`/tips_and_tricks/how-tos/lift_gamma_gain`
