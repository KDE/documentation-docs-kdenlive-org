.. meta::

   :description: Kdenlive Video Effects - Mask Apply
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, chroma key, keying, mask apply

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan  (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Mask Apply
==========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-sec_color_corr_area_select.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-sec_color_corr_area_select

.. sidebar:: |kdenlive-show-video| Mask Apply

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      mask_apply
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Apply the previous effects starting with an effect with "(Mask)" in its name.


.. rubric:: Notes

This is a very powerful effect function as it does not do anything itself but instruct Kdenlive to apply the effects beginning with the (Mask) effect only to the area defined by that (Mask) effect.

See the :ref:`Masking Effects <effects-masking_effects>` section for more details.

In the *Template* effects category there is a pre-setup *Secondary Color Correction* that uses a (Mask) effect and the Mask Apply effect.
