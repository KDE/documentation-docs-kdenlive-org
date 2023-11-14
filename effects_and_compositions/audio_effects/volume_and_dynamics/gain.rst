.. meta::
   :description: Kdenlive Audio Effects - Gain
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics, gain
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Gain
====

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-gain.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Gain

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

Increases or decreases the volume of a clip using percentage instead of :abbr:`dB (decibels)` (see :doc:`/effects_and_compositions/audio_effects/volume_and_dynamics/volume_keyframable`).


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
     - Defines the volume decrease or increase in % (min 0, max 1000).
