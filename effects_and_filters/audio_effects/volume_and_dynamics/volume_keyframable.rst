.. meta::
   :description: Kdenlive Audio Effects - Volume (keyframable)
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics, keyframe
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Volume (keyframable)
====================

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-volume_keyframable.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Volume (keyframable)

   :Status:
      Maintained
   :Keyframes:
      Yes
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

Changes the volume of a clip using keyframes (change of effect over time). The filter/effect uses decibels as opposed to the :doc:`Gain <gain>` effect (percentage).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Gain**
     - Integer
     - Defines the volume decrease or increase in :abbr:`dB (decibels)`.
