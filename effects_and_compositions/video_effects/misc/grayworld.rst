.. meta::

   :description: Do your first steps with Kdenlive video editor, using grayworld effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, grayworld

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |grayworld| raw:: html

   <a href="https://www.researchgate.net/publication/275213614_A_New_Color_Correction_Method_for_Underwater_Imaging" target="_blank">grayworld assumption</a>


.. _effects-grayworld:

Grayworld
=========

This effect/filter is color constancy filter that applies color correction (adjusting the white balance) based on the gray-world assumption\ [1]_.

The LAB gray-world algorithm uses linear light, so input data should be linearized beforehand (and possibly correctly tagged).

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-grayworld.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-grayworld

   Grayworld effect

..

.. rst-class:: clear-both


**Notes**

.. [1] For more details refer to the |grayworld| publication at researchgate.net
