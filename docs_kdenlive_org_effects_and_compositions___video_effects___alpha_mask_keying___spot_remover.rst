.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. |mlt.spot_remover| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterSpot_remover/" target="_blank">MLT spot_remover</a>


.. _effects-spot_remover:

Spot Remover
============

Replace an area with interpolated pixels. The new pixel values are interpolated from the nearest pixels immediately outside of the specified area. (|mlt.spot_remover|)

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-spot_remover.webp
   :align: left
   :width: 90%
   :alt: kdenlive2304_effects-spot_remover

   Spot Remover effect panel with example

This example shows how to use the Spot Remover effect. A bird is crossing the viewport and is removed from the final video. For demonstration purposes the original video is on the left, the one with the bird removed is on the right. The bird's position is indicated by the yellow circle.

Note the keyframe panel and the keyframe positions in the Project Monitor. Edit Mode must be enabled to see the red edit points and handles.
