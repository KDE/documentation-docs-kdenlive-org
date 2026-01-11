.. meta::

   :description: Kdenlive Video Effects - HSV Hold 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color image correction, color, image, correction, hsvhold, hsv, hold

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


HSV Hold
========

.. figure:: /images/effects_and_compositions/effects-hsvhold-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| HSV Hold

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      hsvhold
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter turns a certain :abbr:`HSV (Hue, Saturation, Value)` range into gray values.

This filter measures color difference between set HSV color in options and the ones measured in the video stream. Depending on options, output colors can be changed to be gray or not.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Hue
     - Degrees
     - Set the :term:`hue` value which will be used in color difference calculation. Allowed range is from -360.000 to 360.000. Default value is 0.000.
   * - Saturation
     - Float
     - Set the :term:`saturation` value which will be used in color difference calculation. Allowed range is from -1.000 to 1.000. Default value is 0.000.
   * - Value
     - Float
     - Set the value which will be used in color difference calculation. Allowed range is from -1.000 to 1.000. Default value is 0.000.
   * - Similarity
     - Percentage
     - Set similarity percentage with the key color. Allowed range is from 0.000% to 100.000%. Default value is 0.010.  0.001 matches only the exact key color, while 1.000 matches everything.
   * - Blend
     - Percentage
     - Blend percentage. Allowed range is from 0.0% to 100.0%. Default value is 0.0%. 0.0% makes pixels either fully gray, or not gray at all. Lower values result in more gray pixels, with a higher value the more similar the pixel's color is to the key color.
