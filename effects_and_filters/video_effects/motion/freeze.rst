.. meta::

   :description: Kdenlive Video Effects - Freeze 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, freeze

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Freeze
======

.. figure:: /images/effects_and_compositions/effects-freeze-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Freeze

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      freeze
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect causes the video to freeze. By default, the clip will be frozen for its entire length when the effect is added to the clip. To change this, check either the :guilabel:`Freeze Before` or :guilabel:`Freeze After` option and move the :guilabel:`Freeze at` slider to the time where you want the freeze to start or end. The audio in the video plays for the entire length, i.e. the **Freeze** effect does *not* affect the audio.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Freeze at
     - 
     - Set the position via the slider or the time code (using the format :abbr:`hh:mm:ss:ff(hours:minutes:seconds:frames)`)
   * - Freeze Before
     - 
     - If checked, freezes the video from the start of the clip to the set :guilabel:`Freeze at` position. Default is **off**
   * - Freeze After
     - 
     - If checked, freezes the video from set :guilabel:`Freeze at` position to the end of the clip. Default is **off**
