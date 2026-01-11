.. meta::

   :description: Kdenlive Video Effects - Technicolor
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, technicolor

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |gentlemen_prefer_blondes| raw:: html

   <a href="https://en.wikipedia.org/wiki/Technicolor#/media/File:Gentlemen_Prefer_Blondes_Movie_Trailer_Screenshot_(34).jpg" target="_blank">Gentlemen Prefer Blondes</a>


Technicolor
===========

.. figure:: /images/effects_and_compositions/effects-technicolor-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Technicolor

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      tcolor
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter over-saturates the color in the video source and gives it the old Technicolor film appearance\ [1]_.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Blue/Yellow axis
     - Integer
     - Adjust the factor for the Blue/Yellow axis. Allowed values are from -400 to 400, default is 190.
   * - Red/Green axis
     - Integer
     - Adjust the factor for the Red/Green axis. Allowed values are from -400 to 400, default is 190.


----

.. [1] See this still from |gentlemen_prefer_blondes| in Wikipedia as an example of Technicolor filming.
