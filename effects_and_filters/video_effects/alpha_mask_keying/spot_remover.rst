.. meta::

   :description: Kdenlive Video Effects - Spot Remover
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, spot, remove

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. |spot_remover| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterSpot_remover/" target="_blank">spot_remover</a>


Spot Remover
============

.. figure:: /images/effects_and_compositions/effects-spot_remover-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Spot Remover

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      |spot_remover|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Replace an area with interpolated pixels. The new pixel values are interpolated from the nearest pixels immediately outside of the specified area. Adjust the size and the position according to your needs using the red rectangle\ [1]_ in the project monitor.


.. rubric:: Example

This example shows how to use the Spot Remover effect: A bird is crossing the viewport and is removed from the final video. For demonstration purposes the original video is on the left, the one with the bird removed is on the right. The bird's position is indicated by the yellow circle.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-spot_remover_1.webp
   :align: left
   :width: 90%

   Spot Remover effect panel with example

   Note the keyframe panel and the keyframe positions in the Project Monitor. Edit Mode must be enabled to see the red edit points and handles.

.. rst-class:: clear-both

----

.. [1] Enable |edit-mode|\ :guilabel:`Edit Mode` see the red rectangle.


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
   :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
   :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
   :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
   :class: no-scaled-link

   .. |edit-mode| image:: /images/icons/kdenlive-edit-mode.svg
   :width: 22px
   :class: no-scaled-link
