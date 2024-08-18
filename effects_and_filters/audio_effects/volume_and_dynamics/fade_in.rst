.. meta::
   :description: Kdenlive Audio Effects - Fade In
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics, fade in
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Fade In
=======

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-fade_in.webp
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Fade In

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

Fades in the audio track. Instead of keyframes the effect uses duration (hh:mm:ss:ff). In addition to using the slider the duration can be entered manually, or in the timeline by dragging the green handle\ [1]_.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Duration**
     - Time
     - Defines the duration for the fade in starting at the beginning of the clip.

----

.. [1] The handle is always available in the timeline clip. In fact, dragging the handle automatically adds the fade in effect to the clip's effect stack if it is not there already.