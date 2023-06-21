.. meta::

   :description: Do your first steps with Kdenlive video editor, using the chroma hold effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, chroma hold

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. |chromahold| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#chromahold" target="_blank">avfilter.chromahold</a>


.. https://youtu.be/dXnFsOjS734


.. _effects-chroma_hold:

Chroma Hold
===========

This effect [1]_ removes all color information for all colors except the selected one.

This effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-chroma_hold.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-chroma_hold

   Chroma Hold effect

* **Similarity** - Similarity percentage with the selected color. 0.01 matches only the exact key color, 1.0 matches everything.

* **Blend** - Blend percentage. 0.0 makes pixels either fully grey, or not grey at all. Higher values result in more preserved color

* **For YUV color** - Select this if the clip has YUV data instead of RGB

.. rst-class:: clear-both


.. note:: This effect is not as effective and easy to apply as the :ref:`effects-chroma_keep` effect.


**Notes**

.. [1] This is the |chromahold| MLT filter.
