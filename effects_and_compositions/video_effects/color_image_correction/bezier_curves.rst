.. meta::

   :description: Do your first steps with Kdenlive video editor, using the bezier curves effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, bezier curves

   :authors: - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. |frei0r_curves| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-curves/" target="_blank">frei0r.curves</a>

.. |thediveo_grading| raw:: html

   <a href="http://thediveo-e.blogspot.de/2013/10/grading-of-hero-3-above-waterline.html" target="_blank">TheDiveO</a>


.. _effects-bezier_curves:

Bezier Curves
=============

This effect\ [1]_ is used to adjust the color levels similar to the :ref:`effects-3_point_balance` but with finer control. Although the effect defaults to the RGB channel, it is mostly used with the Luma channel. See also the :ref:`effects-curves` effect that does the same thing but doesn't have the curve handles.

Adjusts luminance or color channel intensity with curve level mapping.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-bezier_curves.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-bezier_curves

   Bezier Curves effect

Note the extended handles on the red dot in the middle with which you can adjust the steepness of the curve leading to and leaving the point.

.. rst-class:: clear-both

See |thediveo_grading| blog for an example of how to use this effect to colour grade clips.


**Notes**

.. [1] This is the |frei0r_curves| MLT filter by Maksim Golovkin and Till Theato.
