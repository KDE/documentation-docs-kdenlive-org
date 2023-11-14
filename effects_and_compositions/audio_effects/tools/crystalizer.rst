.. meta::
   :description: Kdenlive Audio Effects - Crystalizer
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, tools, crystalizer
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Crystalizer
===========

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-crystalizer.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Crystalizer

   :Status:
      Maintained
   :Keyframes:
      No
   :Source library:
      avfilter 
   :Available:
      |linux| |appimage| |windows| |apple|
   :On Master only:
      No
   :Known bugs:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect performs simple audio noise sharpening by linearly increasing differences between each audio sample. 


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Intensity**
     - Float
     - Sets the intensity of effect. Range is -10.0 to 0 (unchanged sound) to 10.0 (maximum effect);  default is 2.0. To inverse filtering use negative values.
   * - **Enable Clipping**
     - Switch
     - Enables clipping (default is enabled)


.. .. rubric:: Notes