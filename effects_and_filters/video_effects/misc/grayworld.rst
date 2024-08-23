.. meta::

   :description: Kdenlive Video Effects - Grayworld
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, grayworld

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Grayworld
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-grayworld.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-grayworld

.. sidebar:: |kdenlive-show-video| Grayworld

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      grayworld
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is color constancy filter that applies color correction (adjusting the white balance) based on the gray-world assumption\ [1]_.

The LAB gray-world algorithm uses linear light, so input data should be linearized beforehand (and possibly correctly tagged).


----

.. |grayworld| raw:: html

   <a href="https://www.researchgate.net/publication/275213614_A_New_Color_Correction_Method_for_Underwater_Imaging" target="_blank">grayworld assumption</a>

.. [1] For more details refer to the |grayworld| publication at researchgate.net
